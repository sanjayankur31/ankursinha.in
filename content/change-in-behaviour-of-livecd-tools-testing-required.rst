Change in behaviour of livecd-tools: Testing required
#####################################################
:date: 2012-04-19 12:57
:author: ankur
:category: Tech
:tags: Fedora
:slug: change-in-behaviour-of-livecd-tools-testing-required

.. raw:: html

   <div>

Hi folks,

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

There has been a change in the way livecd-iso-to-disk works when using a

.. raw:: html

   </div>

.. raw:: html

   <div>

DVD image. In the past, you had to have one bootable partition on the

.. raw:: html

   </div>

.. raw:: html

   <div>

USB media you chose to use, and livecd-iso-to-disk would use it to set

.. raw:: html

   </div>

.. raw:: html

   <div>

up the media. It would copy the required files and the ISO image to this

.. raw:: html

   </div>

.. raw:: html

   <div>

partition that the user specified. 

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Due to some changes in anaconda in F17, anaconda can no longer read the

.. raw:: html

   </div>

.. raw:: html

   <div>

ISO from the same partition. Therefore, upstream has made changes to

.. raw:: html

   </div>

.. raw:: html

   <div>

livecd-iso-to-disk. It is now necessary to use the --format option while

.. raw:: html

   </div>

.. raw:: html

   <div>

creating USB media from DVD ISO images. This \*formats\* the \*entire\*
USB

.. raw:: html

   </div>

.. raw:: html

   <div>

media (don't use a HDD you use for backups!) and creates two partitions:

.. raw:: html

   </div>

.. raw:: html

   <div>

"LIVE" and "LIVE-REPO". The ISO image is copied to the "LIVE-REPO"

.. raw:: html

   </div>

.. raw:: html

   <div>

partition. 

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

The earlier command was:

.. raw:: html

   </div>

.. raw:: html

   <div>

``$ livecd-iso-to-disk <path to iso> /dev/sdb1 #(the attachment point of``

.. raw:: html

   </div>

.. raw:: html

   <div>

``the *partition*)``

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

The new command is:

.. raw:: html

   </div>

.. raw:: html

   <div>

``$ livecd-iso-to-disk --format --reset-mbr --msdos <path to iso> /dev/sdb #(the``

.. raw:: html

   </div>

.. raw:: html

   <div>

``attachment point of the *device*)``

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

I personally feel this is a usability failure, as it restricts the usage

.. raw:: html

   </div>

.. raw:: html

   <div>

of USB media for installation. One will now have to keep aside a special

.. raw:: html

   </div>

.. raw:: html

   <div>

USB stick for installations. One cannot use one partition from an

.. raw:: html

   </div>

.. raw:: html

   <div>

already in-use external HDD. I've filed a bug here[1] as a proposed

.. raw:: html

   </div>

.. raw:: html

   <div>

F17Blocker. 

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

In the mean time, livecd-tools needs testing. I've updated the docs on

.. raw:: html

   </div>

.. raw:: html

   <div>

how to use it[2], but there are areas in there that I'm not well versed

.. raw:: html

   </div>

.. raw:: html

   <div>

with, such as the part about the media not being bootable, and the use

.. raw:: html

   </div>

.. raw:: html

   <div>

of "askmethod". I do not know if this method works for boot and netinst

.. raw:: html

   </div>

.. raw:: html

   <div>

ISO images either since I don't use them regularly. I'm not even sure if

.. raw:: html

   </div>

.. raw:: html

   <div>

--reset-mbr is necessary.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

I'd be grateful if you folks could please test this method of

.. raw:: html

   </div>

.. raw:: html

   <div>

installation, and file relevant bugs, or update the documentation as

.. raw:: html

   </div>

.. raw:: html

   <div>

needed. 

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

I'd like to stress why it is imperative to test this. Since the

.. raw:: html

   </div>

.. raw:: html

   <div>

documentation was not up to date, users didn't use the --format option.

.. raw:: html

   </div>

.. raw:: html

   <div>

This resulted in \*no\* DVD ISO image being copied at all (It got copied

.. raw:: html

   </div>

.. raw:: html

   <div>

to / instead, something upstream has fixed now). Therefore, after the

.. raw:: html

   </div>

.. raw:: html

   <div>

disk partitioning step in anaconda (after it wipes the drives you

.. raw:: html

   </div>

.. raw:: html

   <div>

select), users were completely caught off-guard when Anaconda popped up

.. raw:: html

   </div>

.. raw:: html

   <div>

saying, "I need network to continue installation. I can't find any

.. raw:: html

   </div>

.. raw:: html

   <div>

packages to install on this USB media!". Since the disks had been wiped,

.. raw:: html

   </div>

.. raw:: html

   <div>

no OS remained, broken system, clear usability #fail. (I was fortunate

.. raw:: html

   </div>

.. raw:: html

   <div>

enough to have another system to burn a DVD off of, but I personally

.. raw:: html

   </div>

.. raw:: html

   <div>

know folks who don't have DVD drives in their systems any more, and were

.. raw:: html

   </div>

.. raw:: html

   <div>

without working systems for a while.)

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

[1] https://bugzilla.redhat.com/show_bug.cgi?id=813905

.. raw:: html

   </div>

.. raw:: html

   <div>

[2]

.. raw:: html

   </div>

.. raw:: html

   <div>

https://fedoraproject.org/wiki/How_to_create_and_use_Live_USB#Preparing_the_USB_stick

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

