Appstream data for RPMFusion
#############################
:date: 2015-05-25 14:07
:author: ankur
:category: Tech
:tags: Fedora, Community
:slug: appdata-for-rpmfusion
:summary: I am trying to generate and provide appstream data for packages in the RPMFusion repository.

If you've been keeping up with `Fedora 22`_ and the workstation_, you'll know that Richard and the workstation SIG have been working hard to try and fix appstream_ data files for applications - so that users are exposed to more software in `Gnome Software`_.

Obviously, all of this work is being done for packages in the Fedora repositories. However, there is the very very important RPMFusion_ repository that contains quite a few applications that could benefit from appstream information too! Following the FOSS system of just finding some work to do and jumping head-on into it, I've started working on gathering appstream information for RPMFusion. 

The bare-bones information that can be extracted from the desktop files has already been collected and submitted as packages for inclusion into RPMFusion. No one has accepted the tickets yet, so if you do have some time, please consider reviewing them. I'll be more than happy to swap reviews, of course. The review tickets are here: nonfree_, free_. If you install the packages, you'll notice that very few packages actually have any appdata at all. Therefore, I've also started writing appstream data files manually and `hosting them in a github repository`_ - similar to what Richard does for Fedora packages. If you have some time, please consider adding an appdata file for your favourite application via a pull request. 

The goal here is to make as many applications available in Gnome Software as possible, and in the process, provide Fedora 22 users with an even better experience than Fedora 22 already is!

Enjoy the Fedora 22 release tomorrow, and if you have the time, please help me provide appstream information for as many RPMFusion packages as we possibly can!

Oh, if you do install Fedora 22 afresh tomorrow, we've set up posts on `Ask Fedora`_ that will tell you exactly how to get your music codecs, Skype and so on working. (Look at the right hand side bar!)

Cheerio!

.. _Fedora 22: http://fedoramagazine.org/fedora-22-go-may-26/
.. _workstation: https://getfedora.org/en_GB/workstation/
.. _appstream: http://www.freedesktop.org/wiki/Distributions/AppStream/
.. _Gnome Software: https://wiki.gnome.org/Apps/Software
.. _RPMFusion: http://rpmfusion.org/
.. _nonfree: https://bugzilla.rpmfusion.org/show_bug.cgi?id=3658
.. _free: https://bugzilla.rpmfusion.org/show_bug.cgi?id=3657
.. _hosting them in a github repository: https://github.com/sanjayankur31/rpmfusion-appdata
.. _Ask Fedora: http://ask.fedoraproject.org
