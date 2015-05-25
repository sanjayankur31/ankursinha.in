mpdE (0.0.2 release): A daemon that picks the currently playing song from mpd and sets it as your Empathy status
################################################################################################################
:date: 2011-09-03 10:49
:author: ankur
:category: Tech
:tags: Linux, Music
:slug: mpde-0-0-2-release-a-daemon-that-picks-the-currently-playing-song-from-mpd-and-sets-it-as-your-empathy-status

I use `Empathy`_. I also use `mpd`_. Now, the players I used earlier,
they'd have a convenient plugin that sent "Now playing" to Empathy. I
hadn't found one for mpd yet, so in true FOSS spirit, I jumped into it
and decided to write my own. I'm not particularly a fan of sending my
"Now Playing" to the world, but I just like to know that it can be done,
even if I'm on mpd.

One can checkout the 0.0.2 release from `gitorious`_ using the following
command. To compile it, one needs libmpd-devel and telepathy-glib-devel.
Building it is as simple as ../configure && make.

::

    git clone git://gitorious.org/mpde/mpde.git

I'd like to warn you, that this is a "just works" release. I need to
work a lot more on this. Please have a look at the TODO file for
information. Please send any bugs/feature requests to the emails listed
in the AUTHORS file.

.. _Empathy: http://live.gnome.org/Empathy
.. _mpd: http://mpd.wikia.com/wiki/Music_Player_Daemon_Wiki
.. _gitorious: https://gitorious.org/mpde
