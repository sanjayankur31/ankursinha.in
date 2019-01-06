Testing out Sumatra: a tool for managing iterations of simulations/analyses
############################################################################
:date: 2018-05-12 20:53:25
:author: ankur
:category: Research
:tags: Python, Reproducible research, Computational neuroscience, Sumatra,
       Fedora, Planet
:slug: testing-out-sumatra-a-tool-for-managing-iterations-of-simulations-analyses
:summary: When working on projects that require multiple iterations of
          simulations and/or analyses, it's really quite hard to keep track of
          the changes one makes and how the results vary. Sumatra_ is a tool
          that is developed to help researchers manage such projects.


In the ~4 years that I've spent on my PhD now, I've run hundreds, nay,
thousands of simulations. Research work is incredibly iterative. I (and I
assume others too) make small changes to their methods and then study how these
changes produce different results, and this cycle continues until a
proposed hypothesis has either been accepted or refuted (or a completely new
insight gained, which happens quite often too!).

Folders, and Dropbox? Please, no.
---------------------------------

Keeping track of all these iterations is quite a task. I've seen multiple
methods that people use to do this. A popular method is to make a different
folder for each different version of code, and then use something like Dropbox
to store them all.

Since I come from a computing background, I firmly believe that this is not a
good way of going about it. It may work for folks---people I know and work with
use this method---but it is simply a bad way of going about it. This PhDComic_
does a rather good job of showing an example situation. Sure, this is about a
document, but when source code is kept in different folders, a similar
situation arises. You get the idea.

.. image:: http://www.phdcomics.com/comics/archive/phd101212s.gif
    :alt: PhDComic!
    :target: http://phdcomics.com/comics/archive.php?comicid=1531
    :width: 80%
    :class: text-center img-responsive pagination-centered


Version control, YES!
----------------------

If there weren't tools designed to track and manage such projects, one could
still argue for using such methods, but the truth is that there is a plethora
of `version control tools
<https://en.wikipedia.org/wiki/List_of_version_control_software>`__ available
under `Free/Open Source`_ licenses. Not only do these tools manage projects,
they also make collaborating over source code simple.

All my simulation code, for example, lives in a Git_ repository (which will be
made available under a `Free/Open source`_ license as soon as my paper goes out
to ensure that others can read, verify, and build on it). The support scripts
that I use to set up simulations and then analyse the data they produce already
live `here on GitHub <https://github.com/sanjayankur31/Sinha2016-scripts>`__,
for example. Please go ahead and use them if they fit your purpose.

I have different Git_ branches for different features that I add to the
simulations---the different hypothesis that I'm testing out. I also keep a
rather meticulous record of everything I do in a research journal in LaTeX_ that
also lives in a Git_ repository, and uses Calliope_ (a simple helper script to
manage various journaling tasks). Everything goes in here---graphs, images,
sometimes patches and source code even, and the deductions and other
comments/thoughts too.

My rather simple system is as follows:

- Each new feature/hypothesis gets its own Git_ branch.
- Each version of its implementation, therefore, gets its own unique `commit
  <https://github.com/sanjayankur31/Sinha2016-scripts/blob/master/runners/stri-cluster/start-nest-job.sh#L93>`__
  (a snapshot of code that Git_ saves for the user with a unique identifier and
  a complete record of the changes that were made to the project, when they
  were made and so on.)
- For each run of a snapshot, the generated data is stored in a folder that is
  named `YYYYMMDDHHMM (Year, month, day, time)
  <https://github.com/sanjayankur31/Sinha2016-scripts/blob/master/runners/stri-cluster/start-nest-job.sh#L27>`__,
  which, unless you figure out how to go back in time, is also unique.
- The commit hash + YYYYMMDD become a unique identifier for each code snapshot
  and the results that it generated.
- A new chapter in my research journal holds a summary of the simulation, and
  all the analysis that I do. I even name the chapter "git-hash/YYYYMMDDHHMM".

.. image:: https://imgs.xkcd.com/comics/git.png
    :alt: XKCD on Git.
    :target: https://xkcd.com/1597/
    :width: 50%
    :class: text-center img-responsive pagination-centered

I know that learning a version control system has a steep initial curve, but I
really do think that this is one tool that is well worth the time.

Using a version control system has many advantages, some of which are:

- It lets you keep the full history of your source code, and go back to any
  previous version.
- You know exactly what you changed between two snapshots.
- If multiple people work on the code, everyone knows exactly who authored
  what.
- These tools make changing code, trying out things, and so on, very very easy.
  Try something out in a different branch, if it worked, yay, keep the branch
  running; maybe even merge it to the main branch? If it didn't make a note,
  delete the branch, and move on!
- With services like GitHub_, BitBucket_, and GitLab_, collaboration becomes
  really easy.
- Ah, and note, that every collaborator has a copy of the source code, so it
  has been backed up too! Even if you work alone, there's always another copy
  on GitHub_ (or whatever service you use).

Here's a quick beginners guide to using Git_ and GitHub_:
http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004668
There are many more all over the WWW, of course. Duckduckgo_ is your friend.
(`Why Duckduckgo and not Google? <http://qr.ae/TU1wA9>`__)


What's Sumatra about, then?
----------------------------

.. image:: http://neuralensemble.org/static/photos/sumatra_logo.png
    :alt: Sumatra: a tool to manage and track simulation runs.
    :target: http://neuralensemble.org/static/photos/sumatra_logo.png
    :width: 30%
    :class: text-center img-responsive pagination-centered


I've been meaning to try Sumatra_ out for a while now. What Sumatra_ does is
sort of bring the functions of all my scripts together into one well-designed
tool.  Sumatra_ can do the running bit, then save the generated data in a
unique location, and it even lets users add comments about the simulation.
Sumatra_ even has a web based front end for those that would prefer a graphical
interface instead of the command line.  Lastly, Sumatra_ is written in Python_,
so it works on pretty much all systems. Note that Sumatra_ forces the use of a
version control system (from what I've seen yet).

A quick walk-through
~~~~~~~~~~~~~~~~~~~~

The `documentation <http://sumatra.readthedocs.io/en/0.7.4/index.html>`__
contains all of this already, but I'll show the steps here too. I used a `dummy
repository <https://github.com/sanjayankur31/sumatra-nest-cluster-test>`__ to
test it out.

Installing Sumatra_ is as easy as a pip_ command. I would suggest setting up a
`virtual-environment <https://docs.python.org/3/library/venv.html>`__, though:

.. code::

    python3 -m venv --system-site-packages sumatra-virtual

We then activate the virtual-environment, and install Sumatra_:

.. code::

    source sumatra-virtual/bin/activate
    pip install sumatra


Once it finishes installing, simply mark a version controlled source
repository as managed by Sumatra_:

.. code::

    cd my-awesome-project
    smt init my-awesome-project

Then, one can see the information that Sumatra_ has on the project, for
example:

.. code::

    smt info
    Project name        : test-repo
    Default executable  : Python (version: 3.6.5) at /home/asinha/dump/sumatra-virt/bin/python3
    Default repository  : GitRepository at /home/asinha/Documents/02_Code/00_repos/00_mine/sumatra-nest-cluster-test (upstream: git@github.com:sanjayankur31/sumatra-nest-cluster-test.git)
    Default main file   : test.py
    Default launch mode : serial
    Data store (output) : /home/asinha/Documents/02_Code/00_repos/00_mine/sumatra-nest-cluster-test/Data
    .          (input)  : /
    Record store        : Django (/home/asinha/Documents/02_Code/00_repos/00_mine/sumatra-nest-cluster-test/.smt/records)
    Code change policy  : error
    Append label to     : None
    Label generator     : timestamp
    Timestamp format    : %Y%m%d-%H%M%S
    Plug-ins            : []
    Sumatra version     : 0.7.4


My test script only prints a short message. Here's how one would run it using
Sumatra_:

.. code::

    # so that we don't have to specify this for each run
    smt configure --executable=python3 --main=test.py

    smt run
    Hello Sumatra World!
    Record label for this run: '20180512-200859'
    No data produced.


One can now see all the runs of this simulation that have been made!


.. code::

    smt list --long
    --------------------------------------------------------------------------------
    Label            : 20180512-200859
    Timestamp        : 2018-05-12 20:08:59.761849
    Reason           :
    Outcome          :
    Duration         : 0.050611019134521484
    Repository       : GitRepository at /home/asinha/Documents/02_Code/00_repos/00_mine/sumatra-nest-
                     : cluster-test (upstream: git@github.com:sanjayankur31/sumatra-nest-cluster-
                     : test.git)
    Main_File        : test.py
    Version          : 6f4e1bf05f223a0100ca6f843c11ef4fd70490f3
    Script_Arguments :
    Executable       : Python (version: 3.6.5) at /home/asinha/dump/sumatra-virt/bin/python3
    Parameters       :
    Input_Data       : []
    Launch_Mode      : serial
    Output_Data      : []
    User             : Ankur Sinha (Ankur Sinha Gmail) <sanjay.ankur@gmail.com>
    Tags             :
    Repeats          : None
    --------------------------------------------------------------------------------
    Label            : 20180512-181422
    Timestamp        : 2018-05-12 18:14:22.668655
    Reason           :
    Outcome          : Well that worked
    Duration         : 0.05211901664733887
    Repository       : GitRepository at /home/asinha/Documents/02_Code/00_repos/00_mine/sumatra-nest-
                     : cluster-test (upstream: git@github.com:sanjayankur31/sumatra-nest-cluster-
                     : test.git)
    Main_File        : test.py
    Version          : 4f151a368b1fee1fa8f21026c3b6d2c6b2531da8
    Script_Arguments :
    Executable       : Python (version: 3.6.5) at /home/asinha/dump/sumatra-virt/bin/python3
    Parameters       :
    Input_Data       : []
    Launch_Mode      : serial
    Output_Data      : []
    User             : Ankur Sinha (Ankur Sinha Gmail) <sanjay.ankur@gmail.com>
    Tags             :
    Repeats          : None


There's a lot more that can be done, of course. I'll quickly show the GUI
version here.

One can run the webversion using:

.. code::

    smtweb -p 8001 #whatever port number one wants to use

Then, it'll open up in your default web-browser at http://127.0.0.1:8001/.

.. image:: {static}/images/20180512-sumatra1.png
    :alt: Sumatra initial interface.
    :target: {static}/images/20180512-sumatra1.png
    :width: 80%
    :class: text-center img-responsive pagination-centered


For each project, one can see the various runs, with all the associated
information too.

.. image:: {static}/images/20180512-sumatra2.png
    :alt: Records for a project in Sumatra
    :target: {static}/images/20180512-sumatra2.png
    :width: 80%
    :class: text-center img-responsive pagination-centered


One can then add more information about a run. Sumatra_ already stores lots of
important information as the image shows:

.. image:: {static}/images/20180512-sumatra3.png
    :alt: More information on each record in Sumatra
    :target: {static}/images/20180512-sumatra3.png
    :width: 80%
    :class: text-center img-responsive pagination-centered


Pretty neat, huh?

I run my simulations on a cluster, and so have my own system to submit jobs to
the queue system. Sumatra_ can run jobs in parallel on a cluster, but I've
still got to check if it also integrates with the queue system that our cluster
runs. Luckily, Sumatra_ also provides an API, so I should be able to write a
few Python_ scripts to handle that bit too. It's on my TODO list now.

Please use version control and a Sumatra style record keeper
------------------------------------------------------------

I haven't found another tool that does what Sumatra_ does yet. Maybe Jupyter
notebooks would come close, but one would have to add some sort of wrapper
around them to keep proper records. It'll probably be similar to my current
system.

In summary, please use version control, and use a record keeper to manage and
track simulations. Not only does it make it easier for you, the researcher, it
also makes it easier for others to replicate the simulation since the record
keeper provides all the information required to re-run the simulation.


Free/Open source software promotes Open Science
------------------------------------------------

.. raw:: html

    <video controls width="640" height="390" poster="//static.fsf.org/nosvn/FSF30-video/fsf30-poster.png">
    <source src="//static.fsf.org/nosvn/FSF30-video/FSF_30_720p.webm" type="video/webm">
    <track kind="subtitles" label="English" srclang="en" src="//static.fsf.org/nosvn/FSF30-video/captions/FSF_30_720p.en.vtt" default="default" />
    <track kind="subtitles" label="Spanish" srclang="es" src="//static.fsf.org/nosvn/FSF30-video/captions/FSF_30_es.vtt" />
    <track kind="subtitles" label="French" srclang="fr" src="//static.fsf.org/nosvn/FSF30-video/captions/FSF_30_720p.fr.vtt" />
    <track kind="subtitles" label="German" srclang="en" src="//static.fsf.org/nosvn/FSF30-video/captions/FSF_30_720p.de.vtt" />
    <track kind="subtitles" label="русский" srclang="ru" src="//static.fsf.org/nosvn/FSF30-video/captions/FSF_30_720p.ru.vtt" />
    <track kind="subtitles" label="italiano" srclang="it" src="//static.fsf.org/nosvn/FSF30-video/captions/FSF_30_720p.it.vtt" />
    <track kind="subtitles" label="português" srclang="pt" src="//static.fsf.org/nosvn/FSF30-video/captions/FSF_30_720p.pt.vtt" />
    <track kind="subtitles" label="српски" srclang="sr" src="//static.fsf.org/nosvn/FSF30-video/captions/FSF_30_720p.sr.vtt" />
    <track kind="subtitles" label="fārsi" srclang="fa" src="//static.fsf.org/nosvn/FSF30-video/captions/FSF_30_720p.fa.vtt" />
    <track kind="subtitles" label="nederlands" srclang="nl" src="//static.fsf.org/nosvn/FSF30-video/captions/FSF_30_720p.nl.vtt" />
    <track kind="subtitles" label="magyar" srclang="hu" src="//static.fsf.org/nosvn/FSF30-video/captions/FSF_30_720p.hu.vtt" />
    <track kind="subtitles" label="svenska" srclang="se" src="//static.fsf.org/nosvn/FSF30-video/captions/FSF_30_720p.se.vtt" />
    <track kind="subtitles" label="română" srclang="ro" src="//static.fsf.org/nosvn/FSF30-video/captions/FSF_30_720p.ro.vtt" />
    <track kind="subtitles" label="lietuvių" srclang="lt" src="//static.fsf.org/nosvn/FSF30-video/captions/FSF_30_720p.lt.vtt" />
    <track kind="subtitles" label="hebrew" srclang="lt" src="//static.fsf.org/nosvn/FSF30-video/captions/FSF_30_720p.he.vtt" />
    <track kind="subtitles" label="português do Brasil" srclang="pt-br" src="//static.fsf.org/nosvn/FSF30-video/captions/FSF_30_720p.pt-br.vtt" />
    <track kind="subtitles" label="chinese" srclang="lt" src="//static.fsf.org/nosvn/FSF30-video/captions/FSF_30_720p.zh-cn.vtt" />
    <p><a href="https://www.fsf.org/blogs/community/user-liberation-watch-and-share-our-new-video">
    User liberation video at the Free Software Foundation.
    </a></p>
    </video>

(The original video is at the `Free Software Foundation's website
<https://www.fsf.org/blogs/community/user-liberation-watch-and-share-our-new-video>`__.)

As a concluding plea, I request everyone to please use `Free/Open source`_
software for all research. Not only are these available free of cost, they
provide everyone with the right to read, validate, study, copy, share, and
modify the software. One can learn so much from reading how research tools are
built. One can be absolutely sure of their results if they can see the code
that carries out the analysis. One can build on others' work if the source is
available for all to use and change. How easy does replication become when the
source and all related resources are given out for all to use?

Do not use Microsoft Word, for example. Not everyone, even today, has access
to Microsoft software. Should researchers be required to buy a Microsoft
license to be able to collaborate with us? The tools are here to enable
science, not hamper it.  Proprietary software and formats do not enable
science, they restrict it to those that can pay for such software. This is not
a restriction we should endorse in any way.

Yes, I know that sometimes there aren't `Free/Open source`_ software
alternatives that carry the same set of features, but a little bit of extra
work, for me, is an investment towards Open Science. Instead of Word, as an
example, use Libreoffice_, or LaTeX_. Use `Open formats
<http://opendocumentformat.org/>`__. There will be bugs, but until we report
them, they will not be fixed. Until these `Free/Open source`_ tools replace
restricted software as the standard for science, they will only have small
communities around them that build and maintain them.

Open Science is a necessity.  Researchers from the neuroscience community
recently signed `this letter <http://opensourceforneuroscience.org/>`__
committing to the use of `Free/Open source`_ software for their research. There
are similar initiatives in other fields too, and of course, one must be aware
of the Open Access movement etc.

I've made this plea in the context of science, but the video should also show
you how in everyday life, it is important to use `Free/Open source`_ resources.
Please use `Free/Open source`_ resources, as much as possible.

.. _Sumatra: http://neuralensemble.org/sumatra/
.. _Git: https://git-scm.com/
.. _Calliope: https://github.com/sanjayankur31/calliope
.. _LaTeX: https://www.latex-project.org/
.. _PhDComic: http://phdcomics.com/
.. _Free/Open Source: https://www.gnu.org/philosophy/free-sw.en.html
.. _Bitbucket: https://bitbucket.org
.. _GitLab: https://gitlab.com
.. _GitHub: https://github.com
.. _Duckduckgo: https://duckduckgo.com
.. _Python: https://python.org
.. _pip: https://docs.python.org/3/installing/index.html
.. _Libreoffice: https://www.libreoffice.org/
.. _
