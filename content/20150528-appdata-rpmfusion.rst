Appstream data for RPMFusion - now available!
#############################################
:date: 2015-05-28 21:56
:author: ankur
:category: Tech
:tags: Fedora, RPMFusion
:summary: Appstream data for RPMFusion repositories for Fedora 22 packages are now available as easy to install RPM packages.

`I've been working on generating appstream data for RPMFusion packages recently <{filename}/20150525-appdata-for-rpmfusion.rst>`_. At the moment, since only Fedora packages provide appstream data, only they can be installed using Gnome software - for RPMFusion packages, a user must use another package manager - DNF and so on. Considering that a lot of the packages in RPMFusion are media player front-ends and things, it'd make it a lot easier for users if these were also listed in Gnome software. I spent a number of hours today writing appstream data files for the RPMFusion packages - both in the free and non free repositories. I believe I've written appstream data files for all packages that could be listed in Gnome software now. (They're hosted here in the `Github repository I set up for this purpose`_). I had already generated initial RPM packages for the free and non free repositories and submitted review tickets to RPMFusion. They're still unassigned, so if you are a package maintainer with a few free cycles, please consider reviewing them. They are really simple reviews.

- `Package review: rpmfusion-nonfree-appstream-data - Appstream metadata for the RPMFusion nonfree repository`_
- `Package review: rpmfusion-free-appstream-data - Appstream metadata for the RPMFusion free repository`_

I've now updated the packages submitted for review to use meta data from the new appstream information I wrote. A majority of the RPMFusion GUI packages are now included. You can install the RPMs from here:

- `rpmfusion-free-appstream-data-22-4.fc22.noarch.rpm`_
- `rpmfusion-nonfree-appstream-data-22-4.fc22.noarch.rpm`_

If you'd like to use the terminal, you can run:

.. code-block:: bash

    sudo dnf install http://ankursinha.in/files/misc/rpmfusion/rpmfusion-free-appstream-data-22-4.fc22.noarch.rpm http://ankursinha.in/files/misc/rpmfusion/rpmfusion-nonfree-appstream-data-22-4.fc22.noarch.rpm


You'll need to kill and restart Gnome software to get it to load the new appstream data.

Now, for example, you can now install Mixxx_ from RPMFusion using Gnome software! 

.. image:: {static}/images/20150528-mixx-gs.png
    :width: 500px
    :alt: Screenshot showing Mixxx in Gnome software
    :align: center
    :target: {static}/images/20150528-mixx-gs.png

or, you can pick which of the many Xine front ends that are available in RPMFusion you'd like to install:

.. image:: {static}/images/20150528-xine-search-gs.png
    :width: 500px
    :alt: Screenshot showing multiple Xine front ends available in RPMFusion in Gnome software.
    :align: center
    :target: {static}/images/20150528-xine-search-gs.png

The screen-shots are currently hosted on my fedora people space, but once the packages are added to RPMFusion, we'll probably move them there too. 

Please note that I've written about **a hundred** appdata files at a stretch, so there probably will be a few typos, formatting errors, and so on in them. If you do run into any, please open a pull request at the Github repository and help improve them. 

Since RPMFusion's package set is much smaller than Fedora's, and there aren't too many updates and things in general, I don't think the appstream data will need to be regenerated frequently - but I will update them once a fortnight, just in case.

Enjoy the amazing `Fedora 22 release`_. Cheerio!

.. _Github repository I set up for this purpose: https://github.com/sanjayankur31/rpmfusion-appdata
.. _Package review\: rpmfusion-free-appstream-data - Appstream metadata for the RPMFusion free repository: https://bugzilla.rpmfusion.org/show_bug.cgi?id=3657
.. _Package review\: rpmfusion-nonfree-appstream-data - Appstream metadata for the RPMFusion nonfree repository: https://bugzilla.rpmfusion.org/show_bug.cgi?id=3658
.. _rpmfusion-free-appstream-data-22-4.fc22.noarch.rpm: http://ankursinha.in/files/misc/rpmfusion/rpmfusion-free-appstream-data-22-4.fc22.noarch.rpm
.. _rpmfusion-nonfree-appstream-data-22-4.fc22.noarch.rpm: http://ankursinha.in/files/misc/rpmfusion/rpmfusion-nonfree-appstream-data-22-4.fc22.noarch.rpm
.. _Mixxx: http://www.mixxx.org/
.. _Fedora 22 release: http://fedoramagazine.org/fedora-22-alpha-released/
