Installing Fedora 17 on my EEEpc using a kickstart!
###################################################
:date: 2012-05-13 19:15
:author: ankur
:category: Tech
:tags: Fedora
:slug: installing-fedora-17-on-my-eeepc-using-a-kickstart

I've been trying to do this for a few days now. Figuring out the correct
kickstart options, and then making the kickstart availble was a little
work. It wasn't difficult, it just required some experimentation really.

Here's how I went about it:

The kickstart file looks like this (I install KDE on my eeepc to keep in
touch with it. I use gnome on my main system):

.. code-block:: bash

    #version=DEVEL
    install
    lang en\_US.UTF-8
    keyboard us
    network --onboot no --device p1p2 --bootproto dhcp --noipv6
    --hostname guest.pc
    network --device wlan0 --noipv4 --noipv6 --hostname guest.pc
    timezone Asia/Kolkata
    rootpw --iscrypted foo-bar
    selinux --enforcing
    authconfig --enableshadow --passalgo=sha512
    firewall --service=ssh
    ignoredisk --drives=sdb,sdc
    clearpart --all --drives=sda
    autopart --type=lvm

    firstboot --enabled

    bootloader --location=mbr --timeout=5 --driveorder=sda --append="rhgb
    quiet"

    %packages
    @core
    @KDE Software Compilation
    @X Window System
    firefox
    firstboot
    vim\*
    %end

    reboot

I used two pen drives. One for the installer, and another to provide the
kickstart. Get the UUID of your pen drive using the **'blkid'** command.
This will be required.

To make the kickstart available to your eeepc during installation, hit
ESCAPE when you get to the installer screen. You'll be dropped to a
**boot:** prompt.

.. code-block:: bash

    linux ks=hd:UUID=:/

Tha'ts all really. Sit back, or go take a walk. When you get back, you
have Fedora ready to use!

The page on the wiki with more information is here:
http://fedoraproject.org/wiki/Anaconda/Kickstart

Oh! **system-config-kickstart** appears to be broken. `Here's the bug I filed.`_

.. _Here's the bug I filed.: https://bugzilla.redhat.com/show_bug.cgi?id=820748
