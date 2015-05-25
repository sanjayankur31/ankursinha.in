Integrating mpd better with Gnome Shell
#######################################
:date: 2013-02-17 19:02
:author: ankur
:category: Tech
:tags: Fedora
:slug: integrating-mpd-better-with-gnome-shell

I personally like Gnome3 quite a bit. It works really well for me.
That's a story for another day, however.

|Gnome media player indicator extension screenshot|

I've been looking for ways to integrate `mpd (Media Player Daemon)`_
better with gnome-shell to improve my GUI experience. I use `ncmpcpp`_
in my terminal instance, but it's always nice to have multimedia keys
working and notifications too. Until now, I used to use indimpc (`a
Fedora review ticket that I filed is here`_). Tonight, I ran into the
`gnome-shell-mediaplayer-indicator extension`_. It supports quite a few
music applications via the `MPRIS2`_ specification. However, before you
can use this with mpd, you need to install the `mpDris2`_ package. It
isn't in the Fedora repositories, so I've filed a `review ticket`_
(**Package maintainer? Please review it!**). There's also an `rpm for
Fedora 18`_ that I've built and am currently using.

.. _mpd (Media Player Daemon): http://mpd.wikia.com/wiki/Music_Player_Daemon_Wiki
.. _ncmpcpp: http://ncmpcpp.rybczak.net/
.. _a Fedora review ticket that I filed is here: https://bugzilla.redhat.com/show_bug.cgi?id=765802
.. _gnome-shell-mediaplayer-indicator extension: https://extensions.gnome.org/extension/55/media-player-indicator/
.. _MPRIS2: http://specifications.freedesktop.org/mpris-spec/latest/
.. _mpDris2: https://github.com/eonpatapon/mpDris2
.. _review ticket: https://bugzilla.redhat.com/show_bug.cgi?id=912048
.. _rpm for Fedora 18: http://ankursinha.fedorapeople.org/mpDris2/mpDris2-0.4-1.fc18.noarch.rpm

.. |Gnome media player indicator extension screenshot| image:: https://extensions.gnome.org/static/extension-data/screenshots/screenshot_55_3.png
   :target: https://extensions.gnome.org/extension/55/media-player-indicator/
