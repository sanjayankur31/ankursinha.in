Extracting small chunks of data from EXTREMELY LARGE files - say hello to memory mapped files
#############################################################################################
:date: 2015-02-20 18:12
:author: ankur
:category: Research
:tags: Programming, Computational neuroscience
:slug: extracting-small-chunks-of-data-from-extremely-large-files-say-hello-to-memory-mapped-files
:summary: Memory mapped files are brilliant when you need to extract tiny bits of data from files that are much much larger than the total memory your system has.

The story so far ...
~~~~~~~~~~~~~~~~~~~~

*Beware - lots of PhDcomics links in the text!*

The first post on my research blog, finally - wait! I mean "Hello
World"!

Research is going really well - `the supervisors seem happy`_ and I
haven't considered `killing myself out of frustration yet`_ or even
worse - `I haven't once wondered if a research career was a mistake to
take up`_. I've now been signed up as a visiting lecturer and after my
first stint with `marking undergraduate examination papers`_, I'm a lot
happier supervising BSc final year projects. (The marking didn't
actually go that bad - most of them scored more than 75%, and no, I'm
not a lenient marker!). I am looking forward to teaching, though - I
expect to thoroughly enjoy putting an entire class to sleep!

Anyway, on to the sciency stuff!

Memory mapped files?
~~~~~~~~~~~~~~~~~~~~

Some background on how I came across `memory mapped files`_ before we
begin. On a typical day, I run multiple iterations of simulations. Each
of these simulations deals with about **10,000 neurons and runs for a
total simulation time of about 8 hours**. I specify simulation time
because the library I use, `Auryn`_, is written in C++ and uses `MPI`_
to speed this up and reduces the actual running time to about an hour
and a half. Anyway, to cut the long story short, my simulation produces
a lot of data - generally in the order of 30Gbs - one simulation had
produced more than 200Gbs, even. This is only spike data, as explained
`here`_. I've only begun my PhD and I expect my simulations to get
longer and more complicated, which logically implies that the amount of
data that I'll have to post process will also increase accordingly.

The information I usually need from my simulation data is the spike
information of individual neurons (number of spikes in a time period -
the firing rate) in between certain times - simulation snapshots, we
call them. **So, from 30Gigs of data, I need to search, process and
actually only plot a couple of hundred MBs at the most, generally tens
of MBs or less**. The simplest way of doing this is - read all your data
in, find the required snapshots, extract them and move on with the post
processing. With 30Gigs of data, I could probably do this - my server
has more RAM than that, but, it'll still take the system time to read
all this data into memory. This is what I was doing a month back, though
- before I started looking for more efficient techniques. An **R
script** (the supposed standard language for big data) was used for a
while - still read all the data into memory. **Databases** were
considered and duly dismissed - I'm not going to save 30Gigs of data for
each simulation when I only need a few MBs. The database will anyway run
indexing operations on the data which will still make it take a while to
load the data and the data loading part was what I was really looking to
quicken.

After looking around for quick disc access, I found **memory mapped
files**. As the wikipedia article says, "**A memory-mapped file is a
segment of virtual memory which has been assigned a direct byte-for-byte
correlation with some portion of a file or file-like resource.**\ " The
useful bit is where it says, "**Once present, this correlation between
the file and the memory space permits applications to treat the mapped
portion as if it were primary memory.**\ ". So, basically, you have a
large file, but you don't need to read it into memory - you simply
**map** it into memory. Once you've done that, you use **pointer
arithmetic** to calculate and **extract only the required chunks**.
Simple? Yes! Well, almost. Since you're going to be using pointer
arithmetic to calculate your data locations, data where each entry is of
a **uniform size** is quite important. You can still do it without
uniform data, but that'll require you to use a sentinel like a "n" to
find each line and you'll have to go through the entire file anyway -
it'll just be more complicated. To use my memory mapped file method, I
first got the simulator to output data in binary format - where I could
ensure that the size of each record was the same. This is really simple
to do with a **struct**, like this:

.. code-block:: c

    struct spikeEvent_type {  AurynTime time;  NeuronID neuronID; };

As long as you're running both the read and write operations on the same
machine, with the same compiler, you can be quite certain that the size
of the struct will not change between the time you write the data and
then read it from your post-processing script. Memory mapped files can
be used for a lot more, of course, but we only require multi-threaded
reads which means we don't need to use locks or mutexes or the sort to
prevent race conditions at all.

The code
~~~~~~~~

If you've made it this far, here's your reward - the code (snippets)!

I use `boost's implementation of memory mapped files`_. I couldn't find
any tutorials, but a post or two gave me the idea on how to use the API.
So, you need this inclusion:

.. code-block:: c

    #include <boost/iostreams/device/mapped_file.hpp>

Each MPI rank produces a separate file, so I have 16 files here, since
I use 16 ranks. Instead of sorting and merging them, I simply map them
all. A vector, therefore appears, and holds my memory mapped file
objects:

.. code-block:: c

    std::vector<boost::iostreams::mapped_file_source> raster_data_source_E;     std::ostringstream converter;

    for (unsigned int i = 0; i < parameters.mpi\_ranks; ++i)
    {
    converter.str("");
    converter.clear();
    converter << parameters.output\_file << "." << i << "\_e.ras";

    raster\_data\_source\_E.emplace\_back(boost::iostreams::mapped\_file\_source());
    raster\_data\_source\_E[i].open(converter.str());
    }

Now, we have the files mapped. Let's say my files have data from 0 to
3600 seconds. I need to count the firing rate of my neurons at 2000
seconds. So, I need to get chunks from my 16 files that contain data
from 1999 to 2000 seconds. If you've studied computer science at all,
you should've had a "**BINARY SEARCH**\ " neon light light up in your
head at this point. I used something similar - **upper and lower
bounds**. Luckily, their algorithms, along with pseudo code are
documented
`here <http://www.cplusplus.com/reference/algorithm/upper_bound/>`__ and
`here <http://www.cplusplus.com/reference/algorithm/lower_bound/>`__
respectively.

My implementations look like this:

.. code-block:: c

    /* 
     * ===  FUNCTION  ======================================================================
     *         Name:  binary_upper_bound
     *  Description:  Last occurence of a key using binary search
     * =====================================================================================
     */
        char *
    binary_upper_bound (double timeToCompare, boost::iostreams::mapped_file_source &openMapSource )
    {
        char *spikesStart = NULL;
        unsigned long int numStart = 0;
        unsigned long int numEnd = 0;
        char *currentSpike = NULL;
        unsigned long int numCurrent = 0;
        unsigned long int numdiff = 0;
        unsigned long int step = 0;
        unsigned long int sizeofstruct = sizeof(struct spikeEvent_type);
        struct spikeEvent_type *currentRecord = NULL;

        /*  start of last record */
        spikesStart =  (char *)openMapSource.data();
        numStart = 0;
        /*  end of last record */
        numEnd = (openMapSource.size()/sizeofstruct -1);

        /*  Number of structs */

        numdiff = numEnd - numStart;
    #ifdef DEBUG
        std::cout << "Finding last of " << timeToCompare << "n";
        unsigned long int sizediff = 0;
        char *spikesEnd = NULL;
        spikesEnd =  (spikesStart + openMapSource.size() - sizeofstruct);
        sizediff = spikesEnd - spikesStart;
        std::cout << "Struct size is: " << sizeofstruct << "n";
        std::cout << "Char size is: " << sizeof(char)  << "n";
        std::cout << "size of int is: " << sizeof(int)  << "n";
        std::cout << "Number of records in this file: " << (openMapSource.size() - sizeofstruct)/sizeofstruct << "n";
        std::cout << "Number of records in this file: " << (spikesEnd - spikesStart)/sizeofstruct << "n";
        printf("With printf subtraction %zun",(spikesEnd - spikesStart));
        std::cout << "Proper subtraction : " << (spikesEnd - spikesStart) << "n";
        std::cout << "sizediff : " << sizediff << "n";
        printf("With printf sizediff %zun",sizediff);
        std::cout << "multiplier " << (spikesEnd - spikesStart)/sizediff << "n";
        std::cout << "Number of struct records in this file: " << numdiff < 0)
        {
            numCurrent = numStart;
            step = (numdiff/2);

            numCurrent += step;
            currentSpike = spikesStart + numCurrent * sizeofstruct;
            currentRecord = (struct spikeEvent_type *)currentSpike;
    #ifdef DEBUG
            std::cout << "Current record is: " <time << "t" <neuronID << " at line" << numCurrent << "n";
    #endif

            if (!(timeToCompare time))
            {
                numStart = ++numCurrent;
                numdiff -= step + 1;
            }
            else
                numdiff = step;
        }

        currentSpike = spikesStart + (numStart * sizeofstruct);
        currentRecord = (struct spikeEvent_type *)currentSpike;
    #ifdef DEBUG
        std::cout << "Returning: " <time << "t" <neuronID << "n";
    #endif
        return currentSpike;
    }       /* -----  end of function binary_upper_bound  ----- */

    /* 
     * ===  FUNCTION  ======================================================================
     *         Name:  binary_lower_bound
     *  Description:  First occurence of a key using binary search
     * =====================================================================================
     */
        char *
    binary_lower_bound (double timeToCompare, boost::iostreams::mapped_file_source &openMapSource )
    {
        char *spikesStart = NULL;
        unsigned long int numStart = 0;
        unsigned long int numEnd = 0;
        char *currentSpike = NULL;
        unsigned long int numCurrent = 0;
        unsigned long int numdiff = 0;
        unsigned long int step = 0;
        unsigned long int sizeofstruct = sizeof(struct spikeEvent_type);
        struct spikeEvent_type *currentRecord = NULL;

        /*  start of last record */
        spikesStart =  (char *)openMapSource.data();
        numStart = 0;
        /*  end of last record */
        numEnd = (openMapSource.size()/sizeofstruct -1);

        /*  Number of structs */
        numdiff = numEnd - numStart;

    #ifdef DEBUG
        std::cout << "Finding first of " << timeToCompare << "n";
        unsigned long int sizediff = 0;
        char *spikesEnd = NULL;
        spikesEnd =  (spikesStart + openMapSource.size() - sizeofstruct);
        sizediff = spikesEnd - spikesStart;
        std::cout << "Struct size is: " << sizeofstruct << "n";
        std::cout << "Char size is: " << sizeof(char)  << "n";
        std::cout << "size of int is: " << sizeof(int)  << "n";
        std::cout << "Number of records in this file: " << (openMapSource.size() - sizeofstruct)/sizeofstruct << "n";
        std::cout << "Number of records in this file: " << (spikesEnd - spikesStart)/sizeofstruct << "n";
        printf("With printf subtraction %zun",(spikesEnd - spikesStart));
        std::cout << "Proper subtraction : " << (spikesEnd - spikesStart) << "n";
        std::cout << "sizediff : " << sizediff << "n";
        printf("With printf sizediff %zun",sizediff);
        std::cout << "multiplier " << (spikesEnd - spikesStart)/sizediff << "n";
        std::cout << "Number of struct records in this file: " << numdiff < 0)
        {
            numCurrent = numStart;
            step = (numdiff/2);

            numCurrent += step;
            currentSpike = spikesStart + numCurrent * sizeofstruct;
            currentRecord = (struct spikeEvent_type *)currentSpike;
    #ifdef DEBUG
            std::cout << "Current record is: " <time << "t" <neuronID << " at line" << numCurrent <time < timeToCompare)
            {
                numStart = ++numCurrent;
                numdiff -= step + 1;
            }
            else
                numdiff = step;
        }

        currentSpike = spikesStart + (numStart * sizeofstruct);
        currentRecord = (struct spikeEvent_type *)currentSpike;
    #ifdef DEBUG
        std::cout << "Returning: " <time << "t" <neuronID << "n";
    #endif
        return currentSpike;
    }       /* -----  end of function binary_lower_bound  ----- */

The rest is quite simple, really. I ask a thread to go over all my 16
memory mapped files, find the chunks and store it in a vector. This is
then sorted and the frequency of occurrence of each neuron counted -
which is the firing rate. It looks like this:

.. code-block:: c

        /*  Fill up my vectors with neurons that fired in this period */
        for (unsigned int i = 0; i  0)
            {
                chunkit = chunk_start;
                while (chunkit neuronID);
                    chunkit += sizeof(struct spikeEvent_type);

                }
            }
            else
            {
                std::cout << timeToFly << " not found in E file "  << i < 0)
            {
                chunkit = chunk_start;
                while (chunkit neuronID);
                    chunkit += sizeof(struct spikeEvent_type);
                }
            }
            else
            {
                std::cout << timeToFly << " not found in I file "  << i << "!n";
                return;
            }

        }
        /*  Sort - makes next operations more efficient, or I think it does */
        std::sort(neuronsE.begin(), neuronsE.end());
        std::sort(neuronsI.begin(), neuronsI.end());

        /*  Get frequencies of inhibitory neurons */
        std::vector::iterator search_begin = neuronsI.begin();
        for(unsigned int i = 1; i <= parameters.NI; ++i)
        {
            int rate = 0;
            rate = (std::upper_bound(search_begin, neuronsI.end(), i) != neuronsI.end()) ?  (std::upper_bound(search_begin, neuronsI.end(), i) - search_begin) : 0;

            search_begin = std::upper_bound(search_begin, neuronsI.end(), i);
            neuronsI_rate.emplace_back(rate);
        }
        /*  We have the inhibitory firing rate! */

        /* Get frequencies of excitatory neurons */
        search_begin = neuronsE.begin();
        for(unsigned int i = 1; i <= parameters.NE; ++i)
        {
            int rate = 0;
            rate = (std::upper_bound(search_begin, neuronsE.end(), i) != neuronsE.end()) ?  (std::upper_bound(search_begin, neuronsE.end(), i) - search_begin) : 0;
            search_begin = std::upper_bound(search_begin, neuronsE.end(), i);
            neuronsE_rate.emplace_back(rate);
        }

The main method where I call my many threads would look something like
this:

.. code-block:: c

        /* To see how long it takes, which I forgot to save to add to the post */
        clock_start = clock();
        int task_counter = 0;
        /* graphing_times holds the times at which I need to extract chunks */
        for(std::vector::const_iterator i = graphing_times.begin(); i != graphing_times.end(); ++i)
        {
            std::vector<std::vector > extracted_data_temp;
            /*  Only start a new thread if less than thread_max threads are running */
            if (task_counter < doctors_max)
            {
                /* Just a vector that keeps the currently running threads */
                timeLords.emplace_back(std::thread (tardis, std::ref(raster_data_source_E), std::ref(raster_data_source_I), std::ref(patterns), std::ref(recalls), *i, parameters));
                /* I called my main worker method tardis - always good to make your code fun - there may be a dalek somewhere in my file too ;) */
                task_counter++;
            }
            /* Original comment from the source file below */
            /*  If thread_max threads are running, wait for them to finish before
             *  starting a second round.
             *
             *  Yes, this can be optimised by using a thread pool but I really
             *  don't have the patience to look into ThreadPool or a
             *  boost::thread_group today! 
             */
            else
            {
                for (std::thread &t: timeLords)
                {
                    if(t.joinable())
                    {
                        t.join();
                        task_counter--;
                    }
                }
                timeLords.clear();
            }
        }

        /*  Wait for remaining threads to finish */
        for (std::thread &t: timeLords)
        {
            if(t.joinable())
            {
                t.join();
            }
        }
        timeLords.clear();
        clock_end = clock();

I'm not using a threadpool since the C++ standard doesn't provide one,
and quite frankly, since I'm only making my threads read, I didn't need
an implementation with mutexes and locks. I just use a certain number of
threads at a time and wait for them to finish before starting the next
batch.

The last time I ran my post processing script without memory mapped
files, it took my system quite a while just to load the files. Once the
files were loaded into memory, the processing bit was quite quick,
obviously. However, with memory mapped files, I recently pulled out
4000+ chunks (I had a total of 11000+ graphs generated, so yeah, 4000+
chunks) in a tiny 230seconds. I'll try and benchmark it again when I run
it next and provide "official" figures.

Conclusion
~~~~~~~~~~

Well, in conclusion, memory mapped files are awesome - spend some time
on them if you're processing large amounts of structured information -
you'll take some time to learn how to use them, but your code will scale
as your data gets larger and larger.

.. _the supervisors seem happy: http://phdcomics.com/comics.php
.. _killing myself out of frustration yet: http://www.phdcomics.com/comics/archive.php?comicid=1495
.. _I haven't once wondered if a research career was a mistake to take up: http://www.phdcomics.com/comics/archive.php?comicid=1490
.. _marking undergraduate examination papers: http://www.phdcomics.com/comics/archive.php?comicid=974
.. _memory mapped files: https://en.wikipedia.org/wiki/Memory-mapped_file
.. _Auryn: http://www.fzenke.net/auryn/doku.php
.. _MPI: https://en.wikipedia.org/wiki/Message_Passing_Interface
.. _here: http://www.fzenke.net/auryn/doku.php?id=manual:ras
.. _boost's implementation of memory mapped files: http://www.boost.org/doc/libs/1_50_0/libs/iostreams/doc/classes/mapped_file.html
