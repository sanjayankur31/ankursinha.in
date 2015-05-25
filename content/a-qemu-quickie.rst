A qemu quickie!
###############
:date: 2011-05-19 18:23
:author: ankur
:category: Tech
:tags: Fedora
:slug: a-qemu-quickie

This one's intended for myself actually. I keep forgetting how to use
qemu, and pass files to it etc.

First off, `here's`_ how you go about setting up a guest. (That page has
it all actually!)

This is how you transfer files to your qemu image. There are lots of
ways, google will tell you to use samba etc. I came across this and it
suits me greatly:

1. Get the offset of the partition using parted:

::

    su -
    parted , unit, B, p

The start of the non boot partition is the offset you need.

Then, mount it as a loop device:

::

    su -
    mkdir /tmp/qemu-img
    mount -o loop,offset= [[qemu-image]] /tmp/qemu-img (or whatever dir you created)

and, once you're done:

::

     umount /tmp/qemu-image

That's all! Ciao!

.. _here's: http://fedoraproject.org/wiki/Testing/qemu
