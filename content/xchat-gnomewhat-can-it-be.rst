xchat-gnome..What can it be?
############################
:date: 2009-02-11 14:40
:author: ankur
:category: Tech
:tags: Fedora
:slug: xchat-gnomewhat-can-it-be

Another wierd experience..

While I was setting some preferences for Xchat-Gnome, it suddenly
crashed and will not restart..

I have already tried the following..

#. Remove the ~/.xchat-gnome  folder to remove config. files..
#. Re-install the app. after removing the config files..

This hasn't changed anything.. The app. still doesn't start.

The error :

.. code-block:: bash

    The program 'xchat-gnome' received an X Window System error.
    This probably reflects a bug in the program.
    The error was 'BadImplementation (server does not implement
    operation)'.
    (Details: serial 536 error\_code 17 request\_code 147 minor\_code
    5)
    (Note to programmers: normally, X errors are reported
    asynchronously;
    that is, you will receive the error a while after causing it.
    To debug your program, run it with the --sync command line
    option to change this behavior. You can then get a meaningful
    backtrace from your debugger if you break on the gdk\_x\_error()
    function.)

Even the --sync option gives the same thing. :(

More people are experiencing this..

http://forums.fedoraforum.org/showthread.php?p=1164564&posted=1#post1164564

I'm put it on bugzilla soon.. Looking for the bug mentioned in the posts
there..

Meanwhile, the "boon in disguise" :: I was looking for other IRC clients
and came across `irssi`_. It's great, and being in love with the
terminal (yes sir!!), I don't think I'm going to shift from it. :D

.. _irssi: http://irssi.org/
