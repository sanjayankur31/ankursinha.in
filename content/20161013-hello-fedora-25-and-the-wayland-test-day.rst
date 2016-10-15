Hello Fedora 25! (and the Wayland test day)
###########################################
:date: 2016-10-15 20:25:03
:author: ankur
:category: Tech
:tags: Fedora
:slug: hello-fedora-25-and-the-wayland-test-day
:summary: I recently upgraded to `Fedora 25`_ Beta and participated in the `Wayland test day`_!

You must've read somewhere or the other that `Fedora 25`_ Beta was released a few days ago. I went ahead and upgraded both my systems last evening using :code:`dnf system-upgrade`. Complete instructions on how you can upgrade using :code:`dnf` too are on `this wiki page <https://fedoraproject.org/wiki/DNF_system_upgrade>`__. One's my laptop, and the other is my workstation in the lab at university. Both upgrades went off almost without a hitch. I had a minor issue with a :code:`python-mpd` package that was solved easily enough by removing the package for the upgrade and reinstalling it after. I filed a bug `here <https://bugzilla.redhat.com/show_bug.cgi?id=1383983>`__ anyway. Seems to be a simple packaging fix.

Fedora 25 works quite well. I haven't had any weird issues just yet. My workstation at university has an Intel graphics card 

.. code::

    lspci | grep -i graphics
    00:02.0 VGA compatible controller: Intel Corporation Xeon E3-1200 v3/4th Gen Core Processor Integrated Graphics Controller (rev 06)

Not surprisingly, Wayland works quite well on it. I went ahead and participated in the `Wayland test day`_ from this one already.

My laptop, on the other hand, has a hybrid Nvidia card, though, and runs on nouveau. It didn't handle Wayland too well but `it's a WIP <https://fedoraproject.org/wiki/Wayland_features#Outputs_on_secondary_GPUs>`__. I've had to switch back to X in the meantime:

.. code::

    lspci | grep -i vga
    00:02.0 VGA compatible controller: Intel Corporation Core Processor Integrated Graphics Controller (rev 18)
    01:00.0 VGA compatible controller: NVIDIA Corporation GT218M [GeForce 310M] (rev ff)

A couple of issues with Wayland seem to be known already and are being worked on as I write. So, please do check the bugs folks have filed in the test day matrix and the `Wayland tracker bug <https://bugzilla.redhat.com/1277927>`__ before you file any new ones. The ones I ran into are below. Most of them are known already:

- Thumbnail "border" seems misaligned in activities overview - https://bugzilla.redhat.com/show_bug.cgi?id=1384616
- Dragging application from dash to new workspace does not open app window in new workspace - https://bugzilla.redhat.com/show_bug.cgi?id=1384534
- Opening a new gnome-software window creates a new entry without a proper icon - https://bugzilla.redhat.com/show_bug.cgi?id=1384537
- Places dropdown search does not function if Gnome Weather is open on secondary monitor - https://bugzilla.redhat.com/show_bug.cgi?id=1384569
- Places dropdown search does not function if Gnome Clocks is open on secondary monitor - https://bugzilla.redhat.com/show_bug.cgi?id=1384572
- Screenshot does not appear to capture the secondary monitor in my dual monitor setup: https://bugzilla.redhat.com/show_bug.cgi?id=1384539
- Screenshot of Gnome Maps does not show the map part at all - https://bugzilla.redhat.com/show_bug.cgi?id=1384560
- Removing an application does not bring back the "install" icon immediately in Gnome Software - https://bugzilla.redhat.com/show_bug.cgi?id=1384546 
- Printing directions using Gnome Maps do not show the marked path - https://bugzilla.redhat.com/show_bug.cgi?id=1384551


`Adam's written up a detailed report of the test day here <https://www.happyassassin.net/2016/10/14/fedora-25-workstation-wayland-by-default-test-day-report/>`__ . Please check it out for more information on bugs and the status of Wayland.

Of course, even though the test day is over, you can still upgrade to `Fedora 25`_ and test out Wayland!!

.. _Wayland test day: https://fedoraproject.org/wiki/Test_Day:2016-10-13_Wayland
.. _Fedora 25: https://fedoramagazine.org/announcing-release-fedora-25-beta/
