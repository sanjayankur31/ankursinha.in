unoconv : a handy tool for converting your OO.o files to pdfs on the terminal
#############################################################################
:date: 2010-11-29 02:36
:author: ankur
:category: Other
:tags: Fedora
:slug: unoconv-a-handy-tool-for-converting-your-oo-o-files-to-pdfs-on-the-terminal

I prefer reading a pdf in evince than the .doc or .od? in OO.o. Evince
is much lighter than OO.o. In order to convert your .od? files to .pdfs,
you can export them from OO.o. Here's another way of doing it, and you
don't need to run OO.o for this.

::

    $ yum install unoconv -y
    $ man unoconv
    $ unoconv -d document -f pdf -v filename.doc
    $ evince filename.pdf &

You might need to run unoconv twice initially, to get a listening
instance up. Cheers!
