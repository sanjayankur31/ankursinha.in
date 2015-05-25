An applet for cricket lovers
############################
:date: 2010-05-12 08:25
:author: ankur
:category: Tech
:tags: Fedora
:slug: an-applet-for-cricket-lovers

Arun has already `blogged`_ about this. This is a more "technical" post
;)

I recently reviewed and approved an applet that displays cricket scores
on your GNOME panel. The bug report is ?\ `here`_. Since the cricket
20-20 world cup is on, I thought I'd request the community to try the
applet out so it can get pushed to stable asap.

Here are the required links on Bodhi

https://admin.fedoraproject.org/updates/cricscore-applet-1.1.0.3-1.fc13

https://admin.fedoraproject.org/updates/cricscore-applet-1.1.0.3-1.fc12

As always, to install it

su -c "yum --enablerepo=updates-testing install cricscore-applet"

If you do test it, please provide karma at Bodhi.

I thank `Arun SAG`_ for quickly submitting a package that was a pleasure
to review!

.. _blogged: http://arunsag.wordpress.com/2010/05/11/cricketscore-applet-available-in-fedora/
.. _here: https://bugzilla.redhat.com/show_bug.cgi?id=546686
.. _Arun SAG: http://fedoraproject.org/wiki/User:Sagarun
