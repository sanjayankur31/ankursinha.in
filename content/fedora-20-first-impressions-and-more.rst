Fedora 20: first impressions and more
#####################################
:date: 2013-09-18 17:30
:author: ankur
:category: Tech
:tags: Fedora
:slug: fedora-20-first-impressions-and-more

[caption id="attachment\_1445" align="aligncenter" width="638"]\ |I
accepted my fate.| I accepted my fate.[/caption]

I went ahead and updated to Fedora 20 using the Alpha RC3. One reason is
to help test it, provide karma etc., the other is that I simply couldn't
wait to use the new shiny packages!

Installation
------------

I used the Desktop Live media off a USB. The installation went off
without a hitch. It was quick, reused my ``/home`` partition and didn't
crash even once.

Post installation
-----------------

The new Gnome3.9 is pretty good. There are a couple of changes that I'm
still getting used to:

-  The new status menu is slightly buggy, but the issues are all known:
   the network icon tends to disappear.
-  The new status menu doesn't have the "disable notifications" switch
   any more. It's supposed to be moved to the notification settings in
   the left bottom corner of the notifications tray. `It didn't land in
   3.9 though`_
-  Gnome terminal doesn't let me use Alt as Meta in irssi. I'm still
   looking at how to configure this. Any one have any hints?
-  The new dhclient update was buggy, and `my negative karma to the
   update got it unpushed`_ ;)
-  mpd from rpmfusion isn't updated to work with the ffmpeg in F20. It
   `needs to be built from git`_, since the fixes required aren't
   present in the latest 0.7.15 release. I've `built an RPM here`_
   (`SPEC/SRPM here`_) that you can use until it's fixed in rpmfusion.
-  Byobu and gnome terminal both tend to crash randomly sometimes. It's
   something related to mc I think, but I haven't been able to reproduce
   it.

I'm going to keep testing and giving karma to packages. You can do it
too, you can just use a VM instead of an actual install. There is a lot
of work to be done in other areas too. If you have the time, consider
helping out. A good place to start with simple tasks is the `marketing
list`_. Just keep an eye out on the announce list and the planet and
you'll find something or the other to do. ;)

Anyway! Happy testing!

.. _It didn't land in 3.9 though: https://bugzilla.gnome.org/show_bug.cgi?id=707073
.. _my negative karma to the update got it unpushed: https://admin.fedoraproject.org/updates/FEDORA-2013-16955/dhcp-4.2.5-21.fc20
.. _needs to be built from git: http://bugs.musicpd.org/view.php?id=3814#bugnotes
.. _built an RPM here: http://ankursinha.fedorapeople.org/mpd/mpd-0.17.5.89d2d64-1.fc21.x86_64.rpm
.. _SPEC/SRPM here: http://ankursinha.fedorapeople.org/mpd/
.. _marketing list: https://fedorahosted.org/marketing-team/report/6

.. |I accepted my fate.| image:: http://ankursinha.in/wp/wp-content/uploads/2013/09/Screenshot-from-2013-09-17-04_26_25.png
   :target: http://ankursinha.in/wp/wp-content/uploads/2013/09/Screenshot-from-2013-09-17-04_26_25.png
