Compiling the cp210x module for use with the NAO
################################################
:date: 2012-08-23 12:00
:author: ankur
:category: Tech
:tags: Fedora
:slug: compiling-the-cp210x-module-for-use-with-the-nao

I've been recently working on trying to get a `NavChip`_\ to work with
the `NAO`_. (The NAO is very cool btw!) To start with, I was delighted
to see that the NAO uses a Linux OS on it's `Geode`_ processor. (The
newer NAOs are using an Atom processor though) The issue was that this
kernel that Aldebaran (the manufacturer) uses is customized.
Specifically, it lacks the cp210x driver that the NavChip requires. I've
been trying to build/compile this driver for the past week, and the one
before. I'm really not a kernel developer. In fact, this is the first
time I've come close to touching the kernel sources and well, running
make!

Anyway, as a note to self (yes, another!), and as some documentation for
folks who'd try to use the NAO with more hardware, here's what I've done
so far. I haven't tested the final module yet, but it looks okay. I'll
only know tomorrow when I try it out on the robot if I were successful.

Download the Nao kernel from `Aldebaran's github`_. Please be careful.
It has two branches. Download the one for your Nao: either the Geode or
the Atom version. Download the `cp210x source from the Silabs page`_.
Untar it in your kernel source tree.

Get the kernel configuration from the Nao. It should be **/boot/config**
on the file system. Copy this to your downloaded kernel source tree as
**.config (DOT config)**.

Run:

::

    make oldconfig ARCH=i386 #My system is an x86_64, so the ARCH argument is needed

The Nao's kernel is 2.6, so you need to use the Makefile26 file in the
cp210x directory. Run configure. It'll create a defaults.mk file. Modify
this file to correct the KVER etcetera variables (You can also modify
the configure script instead. Whatever you prefer):

::

    # Makefile.config
    # Automatically generated
    KVER=2.6.29.6-rt24
    KVER1=2
    KVER2=6
    KVER3=29.6-rt24
    EXT=.ko
    KOFILE=cp210x.ko
    KDIR=/home/ankur/Documents/work/code/NAO/OS/linux-aldebaran
    MODFILE=cp2101.ko
    MODDIR=/home/ankur/Documents/work/code/NAO/OS/linux-aldebaran
    PWD=/home/ankur/Documents/work/code/NAO/OS/linux-aldebaran/cp210x-3.1.0/cp210x

In the Makefile, under "default:", I added ARCH=i386 (again, since my
host is an x86\_64). Now, just run

::

    make

That should be it. Check if your module is okay using "file" and
"modinfo". It looks okay. I've got to try it on the Nao tomorrow though
to confirm.

.. _NavChip: http://www.intersense.com/pages/16/16/
.. _NAO: http://en.wikipedia.org/wiki/Nao_(robot)
.. _Geode: http://en.wikipedia.org/wiki/Geode_(processor)
.. _Aldebaran's github: https://github.com/aldebaran/linux-aldebaran/tree/release-1.12/geode
.. _cp210x source from the Silabs page: http://www.silabs.com/products/mcu/Pages/USBtoUARTBridgeVCPDrivers.aspx
