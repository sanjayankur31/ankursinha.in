Yin and yang: dd and testdisk
#############################
:date: 2013-05-28 13:07
:author: ankur
:category: Tech
:tags: Fedora
:slug: yin-and-yang-dd-and-testdisk

Well, almost.

I maintain an external hard disk which has 2 partitions. One is
dedicated to backups where `deja-dup`_ backs up once a day. The other is
where all my TV/Films etc. go in. A few minutes back, in the excitement
of updating my EEE to Fedora 19, I stupidly gave the wrong argument to
``dd`` and ended up losing my partition table (and some data in the
first partition) to this HDD. Instead of ``of=/dev/sdc``, I gave
``of=/dev/sdb``. As it happens with everyone, I realized the minute I
pressed enter. Now, I'd probably lost some data on the first partition,
but I was pretty confident that my second partition still existed
untouched. I can make fresh backups and get my first partition back that
way, but collecting films and TV seasons from friends is a huge huge
pain.

**Lesson learnt: BE VERY CAREFUL WITH DD. It's safest to unplug all
devices other than the one you want to write to. I generally do this.
Excitement. Meh!**

Now, the recovery part. I first came across `this post on TLDP`_. I
really tried to follow it, but fdisk appears to have changed. My limited
knowledge about disks, such as sectors and cylinders and units and
tracks sort of made it difficult to follow though. Luckily, I found
`testdisk`_ in the Fedora repositories.

``sudo yum install testdisk -y``

I followed the steps outlined `here`_ and got my partition table back.
The second partition is fully functional, as I expected it would. The
first partition is still being checked. I expect to have to format it
and re-backup though.

Something is better than nothing really. Saving one partition out of two
isn't bad.

**Lesson Learnt: Learn how to recover data via fdisk/testdisk. It comes
in handy sometime or the other.**

Phew. Close one.

.. _deja-dup: https://live.gnome.org/DejaDup
.. _this post on TLDP: http://www.tldp.org/HOWTO/Partition/recovering.html
.. _testdisk: http://www.cgsecurity.org/wiki/TestDisk
.. _here: http://www.cgsecurity.org/wiki/TestDisk_Step_By_Step
