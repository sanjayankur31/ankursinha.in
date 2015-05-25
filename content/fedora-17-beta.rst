Fedora 17 beta
##############
:date: 2012-04-14 12:33
:author: ankur
:category: Tech
:tags: Fedora
:slug: fedora-17-beta

To maintain tradition, I installed beta on my system yesterday. Fedora
17 beta is pretty good. It gave me both some pleasant and unpleasant
surprises. I'm just going to note some of them down here to give them
some visibility. 

.. raw:: html

   <div>

Broadcomm wireless working out of the box
-----------------------------------------

.. raw:: html

   </div>

.. raw:: html

   <div>

I'm really not sure how this happened. I haven't read about it any place
till now. This is my wireless hardware information:

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

``[root@ankur ~]# lspci | egrep -i network``

.. raw:: html

   </div>

.. raw:: html

   <div>

``12:00.0 Network controller: Broadcom Corporation BCM4313 802.11b/g/n Wireless LAN Controller (rev 01)``

.. raw:: html

   </div>

.. raw:: html

   <div>

``[root@ankur ~]#``

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

Until Fedora 16, I needed the kmod-wl from `RPMFusion`_ to get it
working. Great to have a better out of the box experience! Now the bad
news: It doesn't work very well :/ I get really bad speeds on my wifi,
so I've filed a bug `here`_. If you also observe the same issue, please
add your comments to the bug.

.. raw:: html

   </div>

.. raw:: html

   <div>

Move from /media to /run/media/$USER/
-------------------------------------

.. raw:: html

   </div>

.. raw:: html

   <div>

This one really caught me by surprise. It seems that `udisks2 has
modified the target location`_ of external mounted media. It is now
under /run/media/$USER instead of the traditional /media. Nothing about
this is present in the `latest FHS`_. `Systemd is probably going to get
rid of /media altogether`_. 

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Creating USB sticks from F17 DVD isos
-------------------------------------

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

The directions on `this page`_ are correct. There's a `bug in
livecd-tools`_ which has been fixed and pushed. Please ensure that you
have at least version 16.11 of livecd-tools before trying to create your
USB stick. If you don't, anaconda will ask you for network access after
your drives have been wiped, leaving you with a broken system without an
OS. (I was lucky to have another system to burn a DVD from.) 

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

This is all I have at the moment. If something else comes around, I'll
update the post as required.

.. raw:: html

   </div>

.. _RPMFusion: http://rpmfusion.org
.. _here: https://bugzilla.redhat.com/show_bug.cgi?id=812506
.. _udisks2 has modified the target location: http://cgit.freedesktop.org/udisks/tree/data/org.freedesktop.UDisks2.xml?id=aa02e5fc53efdeaf66047d2ad437ed543178965b#n1094
.. _latest FHS: http://www.pathname.com/fhs/pub/fhs-2.3.html
.. _Systemd is probably going to get rid of /media altogether: http://www.mail-archive.com/systemd-devel@lists.freedesktop.org/msg04728.html
.. _this page: https://fedoraproject.org/wiki/How_to_create_and_use_Live_USB#How_to_Make_a_bootable_USB_Drive_to_Install_Fedora_instead_of_using_a_physical_DVD
.. _bug in livecd-tools: https://bugzilla.redhat.com/show_bug.cgi?id=812141
