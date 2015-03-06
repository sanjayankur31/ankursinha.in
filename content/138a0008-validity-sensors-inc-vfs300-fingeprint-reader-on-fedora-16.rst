138a:0008 Validity Sensors, Inc. VFS300 Fingeprint Reader on Fedora 16
######################################################################
:date: 2012-03-23 15:21
:author: ankur
:category: Tech
:tags: Fedora
:slug: 138a0008-validity-sensors-inc-vfs300-fingeprint-reader-on-fedora-16

I've been looking to get my finger print reader working on Fedora for
quite a while now. Alas, fprint hasn't gotten down to writing drivers
for my hard-ware yet. However, `someone else`_ did the work for them.
The code isn't included in the libfprint mainline yet. I've `filed a
bug`_ hoping the maintainer will look into it and send cleaned up
patches upstream for inclusion. Nevertheless, I've `built the package
for F16 x86\_64`_ which folks can use in the time being. If you're on
another version, you can build yourself an rpm from the `srpm`_.

.. raw:: html

   <div>

Here's what the lsusb output looks like:

.. raw:: html

   <div>

.. raw:: html

   <div>

**Bus 001 Device 004: ID 138a:0008 Validity Sensors, Inc. VFS300
Fingeprint Reader**

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Here's a screenshot showing that it works:

.. raw:: html

   </div>

|validity vfs301 screenshot on gnome|

.. raw:: html

   <div>

.. raw:: html

   </div>

.. _someone else: https://github.com/andree182/vfs301/
.. _filed a bug: https://bugzilla.redhat.com/show_bug.cgi?id=806234
.. _built the package for F16 x86\_64: http://ankursinha.fedorapeople.org/libfprint-vfs301/libfprint-0.4.0-4.fc16.x86_64.rpm
.. _srpm: http://ankursinha.fedorapeople.org/libfprint-vfs301/libfprint-0.4.0-4.fc16.src.rpm

.. |validity vfs301 screenshot on gnome| image:: http://ankursinha.in/wp/wp-content/uploads/2012/03/validity-vfs301.png?w=300
   :target: http://ankursinha.in/wp/wp-content/uploads/2012/03/validity-vfs301.png
