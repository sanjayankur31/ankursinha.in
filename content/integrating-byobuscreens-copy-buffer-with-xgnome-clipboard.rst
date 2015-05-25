Integrating byobu/screen's copy buffer with X/Gnome clipboard
#############################################################
:date: 2012-06-23 17:16
:author: ankur
:category: Tech
:tags: Fedora
:slug: integrating-byobuscreens-copy-buffer-with-xgnome-clipboard

I use `byobu`_ with a `screen`_ backend on xterm. I've been trying to
find an easy way of copying stuff from the terminal to my X/GNOME
clipboard. The one way that I came across was:

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

::

    echo "paste buffer here" | xsel #for X clipboard

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

or 

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

::

    echo "paste buffer here" | parcellite #for GNOME Clipboard

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

I even tried a script to make this a little better. However, this isn't
convenient enough. I looked around a little and found `a way to
integrate the screen and X clipboards`_. However, since I use byobu,
which uses it's own buffer (I think, since, there is no
/tmp/screen-exchange file on my system), this didn't work for me. I dug
up a little and found byobu's buffer file instead. It's kept at
**$BYOBU\_RUN\_DIR/printscreen**. Therefore, a tiny change in the screen
method works for byobu:

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Add this to **~/.byobu/keybindings**

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   <div>

::

    # Add cool line to make copying to x clipboard possible.

.. raw:: html

   </div>

.. raw:: html

   <div>

::

    # This binds C-a b to copy screen's copy buffer to the system clipboard.

.. raw:: html

   </div>

.. raw:: html

   <div>

::

    bind b eval writebuf 'exec /bin/sh -c "parcellite < $BYOBU_RUN_DIR/printscreen && xsel -i < $BYOBU_RUN_DIR/printscreen "'

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Now, after you've put something into the screen copy buffer, press Ctrl
a b (ctrl, then a, then b), and this buffer will be put into the X and
GNOME clipboards!

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

It's a hack. It works ;)

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. _byobu: https://launchpad.net/byobu
.. _screen: https://launchpad.net/byobu
.. _a way to integrate the screen and X clipboards: http://www.commandlinefu.com/commands/view/2276/getting-screens-copy-buffer-into-xs-copy-buffer-on-linux
