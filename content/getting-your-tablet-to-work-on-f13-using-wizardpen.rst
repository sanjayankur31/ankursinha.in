Getting your tablet to work on F13 using WizardPen
##################################################
:date: 2010-09-22 20:07
:author: ankur
:category: Tech
:tags: Fedora
:slug: getting-your-tablet-to-work-on-f13-using-wizardpen

As a lot of you would remember, HAL was dropped in favour of udev in
Fedora 13. (More info `here`_). I own a "UC-LOGIC Tablet WP5540U" which
I had successfully configured on Fedora 12 using HAL. Since I upgraded,
and the HAL configuration worked no more, a new configuration was
needed. For those still on Fedora 12, you can refer to this `awesome
post`_ to get your tablet working.

My post will describe the changes needed for Fedora 13.

**Using wizardpen to get your tablet working on Fedora 13**
-----------------------------------------------------------

#. Please check the \ `project page`_ to see if your tablet is supported
#. Download the
   rpm \ `here <http://ankursinha.fedorapeople.org/tablet/>`__ (you can
   also download the srpm and \ `rebuild`_ it). I had added
   this \ `patch`_ to the SRPM that enables it to build correctly with
   xorg-1.7. ( I haven't updated this in a while, maybe when I get more
   time)

Doing the work:
~~~~~~~~~~~~~~~

#. As root, install the package using
#. Connect the tablet and run the following command to determine the
   name of the tablet
#. We look for the event associated with the tablet
#. Calibrate the tablet using:
#. You now need to add a configuration file for Xorg for the tablet. You
   can refer to the `Fedora Documentation on this`_. This is what my
   `wizardpen.conf`_ looks like:

.. _here: http://fedoraproject.org/wiki/Input_device_configuration#Fedora_13
.. _awesome post: http://blog.kagesenshi.org/2009/09/genius-g-pen-4500-and-fedora.html
.. _project page: http://code.google.com/p/linuxgenius/
.. _rebuild: https://fedoraproject.org/wiki/How_to_create_an_RPM_package
.. _patch: http://code.google.com/p/linuxgenius/issues/detail?id=5
.. _Fedora Documentation on this: http://fedoraproject.org/wiki/Input_device_configuration
.. _wizardpen.conf: http://ankursinha.fedorapeople.org/tablet/wizardpen.conf
