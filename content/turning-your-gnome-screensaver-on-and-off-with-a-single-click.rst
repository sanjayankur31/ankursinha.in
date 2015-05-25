Turning your gnome-screensaver on and off with a single click!
##############################################################
:date: 2011-01-14 10:52
:author: ankur
:category: Tech
:tags: Fedora
:slug: turning-your-gnome-screensaver-on-and-off-with-a-single-click

Recently, I found myself wondering what the easiest, laziest way of
toggling the screen saver state would be.

Scenario:
---------

You're not interacting with your system, but, you are still using it.
You may be watching a film, or taking notes off a document or website. I
frequently need to refer to documents.

Logic:
------

The default method of toggling the screen saver state would be to go to
System>Preferences>Screen saver and make changes. That's too much work,
and I'm too lazy for it. Here's what I came up with:

::

     $ gconftool-2 --toggle /apps/gnome-screensaver/idle_activation_enabled

Method:

Create a simple shell script:

::

    gconftool-2 --toggle /apps/gnome-screensaver/idle_activation_enabled
    notify-send "Screen Saver status is" `gconftool-2 -g /apps/gnome-screensaver/idle_activation_enabled`

    exit 0

Make it executable:

::

     $ chmod a+x screenSaverToggle.sh

| Make a new launcher:\ |image0|
|  This is what you get:

|image1|

.. |image0| image:: http://dodoincfedora.files.wordpress.com/2011/01/screenshot1.png?w=300
   :target: http://dodoincfedora.files.wordpress.com/2011/01/screenshot1.png
.. |image1| image:: http://dodoincfedora.files.wordpress.com/2011/01/screenshot-1.png?w=300
   :target: http://dodoincfedora.files.wordpress.com/2011/01/screenshot-1.png
