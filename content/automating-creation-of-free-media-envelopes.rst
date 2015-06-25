Automating creation of free-media envelopes
###########################################
:date: 2011-04-19 15:59
:author: ankur
:category: Tech
:slug: automating-creation-of-free-media-envelopes

I've accepted a lot of requests this month. It's because Rahul sent me
100 fedora 14 DVDs which I could use! (Thanks Rahul!!)

I'm lazy, and I really didn't want to write out the addresses by hand,
so I ran around looking for ways to automate it. I've come up with
something. It isn't anywhere near perfect, but it works, and generates
the free-media mailer envelopes for you with addresses, so you can print
them, cut them, insert the dvd, and send them! (I haven't come up with
an idea to automate the cutting/folding/inserting/sending yet, got any
ideas ? 3:) )

Here goes:

#. Log on to http://fedorahosted.org/free-media with your credentials.
#. Go to "view tickets > custom query". The custom query by default
   shows tickets owned by you. Check the "Show full description under
   each result" and "update" the page. It will now show your tickets
   with their addresses.
#. Go to the bottom of the page and download the RSS-feed. (Is there a
   process of automating this portion? If you have something, let us
   know!!)
#. Download it to a known location. Preferably make a new directory for
   this work.
#. Download `this script`_. Make it executable (**chmod a+x script.sh**)
#. Run the script on the downloaded xml file (**./script.sh query.xml**)
   . You will get a file with the extracted addresses called
   **adds.txt**
#. Manually check the formatting of the addresses. (There are some lines
   that are pretty long, and go off the front of the envelope. This can
   be automated too, maybe later.)
#. Download `this cpp file`_, compile it so : ( **g++ free-media.cpp
   -Wall -Wextra -W -pedantic -O2  -o free-media**)
#. Download the `free-media mailer`_, fill in your address using
   inkscape, **export it as a png** into this directory.
#. Run the programme: **./free-media png file> adds.txt**
#. You would now have different pngs filled up with both the sender's
   and receiver's address!

It looks huge doesn't it? 11 steps is a lot of work. What you need to
notice is that most of these are one time steps. From the next month,
all you need to do is download the RSS feed and run the script and the
program (ONLY!)

Points to note: You need to have the "convert" command on your system.
It's in the "ImageMagick" package.

If this doesn't work for you, please drop me a mail at ankursinha AT
fp.o or find me on the IRC at #fedora, #fedora-ambassadors, and I'll
help you out!

Have fun. Remember to send your two media a month :)

EDIT:

So a src file that says:

::

    Ankur Sinha
    I live in this street,
    I live in this town,
    PIN 0000000
    This is the country.
    =
    Will give you this envelope!

.. _this script: http://ankursinha.fedorapeople.org/free-media/script.sh
.. _this cpp file: http://ankursinha.fedorapeople.org/free-media/free-media.cpp
.. _free-media mailer: https://fedoraproject.org/wiki/File:free-media-mailer.svgz
