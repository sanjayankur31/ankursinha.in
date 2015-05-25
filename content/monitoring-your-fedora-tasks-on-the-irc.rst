Monitoring your Fedora tasks on the IRC
#######################################
:date: 2013-08-26 23:02
:author: ankur
:category: Tech
:tags: Fedora
:slug: monitoring-your-fedora-tasks-on-the-irc

This is probably common knowledge by now, but I thought I'd put it up
anyway.

`Fedmsg`_ is a great method that infra uses to get updates on what's
going on in Fedora. One can use the `gnome shell extension`_ to get a
set of updates from it. I don't use the extension though, since I'm
almost always on IRC. Here's how to do it on IRC:

1. Join the #fedora-fedmsg channel on Freenode
2. Configure your IRC client to highlight your FAS username. On
    **irssi**, this can be done using the **hilight** command:

``/hilight USERNAME``

You might need to save your config so this happens when you quit and
reuse irssi:

``/save``

That's it. Get updates. Here's an image of two messages on one of my
builds:

|fedmsg-irc|

As an extra, you can use the `irssi-notify`_ to get notifications
whenever something is highlighted in **irssi**.

Have fun!

.. _Fedmsg: http://fedmsg.com
.. _gnome shell extension: https://apps.fedoraproject.org/packages/gnome-shell-extension-fedmsg
.. _irssi-notify: http://code.google.com/p/irssi-libnotify/

.. |fedmsg-irc| image:: http://ankursinha.in/wp/wp-content/uploads/2013/08/fedmsg-irc.png
   :target: http://ankursinha.in/wp/wp-content/uploads/2013/08/fedmsg-irc.png
