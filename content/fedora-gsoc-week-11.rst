Fedora GSoC: Week 11
####################
:date: 2011-07-10 11:10
:author: ankur
:category: Tech
:tags: Fedora
:slug: fedora-gsoc-week-11

The project is steadily building up, brick by brick. Aeskulap was
approved and a bunch of other packages submitted for review. GoFigure2
is one of them, Ginkgo-CADx is almost done, and freemedforms will be
approved anyday now :)

A complete table is below:

+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `710212`_   | medium   | medium   | Linux   | mrceresa AT gmail.com           | NEW        | Review Request: dcm4che - A DICOM implementation in Java                                                       |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `570224`_   | medium   | medium   | Linux   | nobody AT fedoraproject.org     | NEW        | Review Request: InsightApplications - Collection of medial image applications built with the Insight Toolkit   |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `666656`_   | medium   | medium   | Linux   | nobody AT fedoraproject.org     | NEW        | Review Request: praat - analyze, synthesize, and manipulate speech.                                            |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `705104`_   | medium   | medium   | Linux   | nobody AT fedoraproject.org     | NEW        | Review Request: freediams - Pharmaceutical Drugs Prescriptor                                                   |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `710995`_   | medium   | medium   | Linux   | nobody AT fedoraproject.org     | NEW        | Review Request: kradview - An image viewer oriented to images obtained by X-Ray machines                       |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `714047`_   | medium   | medium   | Linux   | nobody AT fedoraproject.org     | NEW        | Review Request: nifticlib - A set of i/o libraries for reading and writing files in the nifti-1 data format    |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `714326`_   | medium   | medium   | Linux   | nobody AT fedoraproject.org     | NEW        | Review Request: libtpcmisc - Miscellaneous PET functions                                                       |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `714327`_   | medium   | medium   | Linux   | nobody AT fedoraproject.org     | NEW        | Review Request: libtpcimgio - Turku PET Centre for image file input and output procedures                      |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `714328`_   | medium   | medium   | Linux   | nobody AT fedoraproject.org     | NEW        | Review Request: xmedcon - A medical image conversion utility and library                                       |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `715154`_   | medium   | medium   | Linux   | nobody AT fedoraproject.org     | NEW        | Review Request: o-palm - A coupler for all the applications built upon existing independent models             |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `715496`_   | medium   | medium   | Linux   | nobody AT fedoraproject.org     | NEW        | Review Request: elmer-matc - Open Source Finite Element Software for Multiphysical Problems                    |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `715498`_   | medium   | medium   | Linux   | nobody AT fedoraproject.org     | NEW        | Review Request: elmer-hutiter - Open Source Finite Element Software for Multiphysical Problems                 |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `715503`_   | medium   | medium   | Linux   | nobody AT fedoraproject.org     | NEW        | Review Request: elmer-meshgen2d - Open Source Finite Element Software for Multiphysical Problems               |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `715618`_   | medium   | medium   | Linux   | nobody AT fedoraproject.org     | NEW        | Review Request: elmer-eio - Open Source Finite Element Software for Multiphysical Problems                     |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `715619`_   | medium   | medium   | Linux   | nobody AT fedoraproject.org     | NEW        | Review Request: elmer-elmergrid - Open Source Finite Element Software for Multiphysical Problems               |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `715620`_   | medium   | medium   | Linux   | nobody AT fedoraproject.org     | NEW        | Review Request: elmer-fem - Open Source Finite Element Software for Multiphysical Problems                     |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `720121`_   | medium   | medium   | Linux   | nobody AT fedoraproject.org     | NEW        | Review Request: GoFigure2 - a software for visualizing, processing and analysing of bioimages                  |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `691774`_   | medium   | medium   | Linux   | sanjay.ankur AT gmail.com       | NEW        | Review Request: elastix - Toolbox for rigid and nonrigid registration of images                                |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `666726`_   | medium   | medium   | Linux   | cwickert AT fedoraproject.org   | ASSIGNED   | Review Request: amide - A Medical Image Data Examiner:                                                         |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `712624`_   | medium   | medium   | Linux   | hobbes1069 AT gmail.com         | ON\_QA     | Review Request: aeskulap - A full open source replacement for commercially available DICOM viewer              |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `707002`_   | medium   | medium   | Linux   | lakshminaras2002 AT gmail.com   | ASSIGNED   | Review Request: FreeMedForms - An open Electronic Medical Record Manager                                       |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `713677`_   | medium   | medium   | Linux   | mrceresa AT gmail.com           | ASSIGNED   | Review Request: klt - An implementation of the Kanade-Lucas-Tomasi feature tracker.                            |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `597755`_   | medium   | medium   | Linux   | panemade AT gmail.com           | ASSIGNED   | Review Request: openmolar - Open Source Dental Practice Management Software                                    |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `567086`_   | medium   | medium   | Linux   | sanjay.ankur AT gmail.com       | ASSIGNED   | Review Request: VXL - C++ Libraries for Computer Vision Research and Implementation                            |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `539387`_   | medium   | low      | Linux   | sanjay.ankur AT gmail.com       | ASSIGNED   | Review Request: InsightToolkit - Medical imaging processing library                                            |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `604005`_   | medium   | low      | Linux   | sanjay.ankur AT gmail.com       | ASSIGNED   | Review Request: ledgersmb - Financial accounting program                                                       |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+
| `716352`_   | medium   | medium   | Linux   | mariobl AT freenet.de           | MODIFIED   | Review Request: toothchart - A PHP script which graphically shows how a baby's primary teeth have erupted      |
+-------------+----------+----------+---------+---------------------------------+------------+----------------------------------------------------------------------------------------------------------------+

**27 bugs found.**

There are still quite a few packages waiting for review. **If you have
some time to spare, or would like a review swap, please ping me :)**

.. _710212: https://bugzilla.redhat.com/show_bug.cgi?id=710212
.. _570224: https://bugzilla.redhat.com/show_bug.cgi?id=570224
.. _666656: https://bugzilla.redhat.com/show_bug.cgi?id=666656
.. _705104: https://bugzilla.redhat.com/show_bug.cgi?id=705104
.. _710995: https://bugzilla.redhat.com/show_bug.cgi?id=710995
.. _714047: https://bugzilla.redhat.com/show_bug.cgi?id=714047
.. _714326: https://bugzilla.redhat.com/show_bug.cgi?id=714326
.. _714327: https://bugzilla.redhat.com/show_bug.cgi?id=714327
.. _714328: https://bugzilla.redhat.com/show_bug.cgi?id=714328
.. _715154: https://bugzilla.redhat.com/show_bug.cgi?id=715154
.. _715496: https://bugzilla.redhat.com/show_bug.cgi?id=715496
.. _715498: https://bugzilla.redhat.com/show_bug.cgi?id=715498
.. _715503: https://bugzilla.redhat.com/show_bug.cgi?id=715503
.. _715618: https://bugzilla.redhat.com/show_bug.cgi?id=715618
.. _715619: https://bugzilla.redhat.com/show_bug.cgi?id=715619
.. _715620: https://bugzilla.redhat.com/show_bug.cgi?id=715620
.. _720121: https://bugzilla.redhat.com/show_bug.cgi?id=720121
.. _691774: https://bugzilla.redhat.com/show_bug.cgi?id=691774
.. _666726: https://bugzilla.redhat.com/show_bug.cgi?id=666726
.. _712624: https://bugzilla.redhat.com/show_bug.cgi?id=712624
.. _707002: https://bugzilla.redhat.com/show_bug.cgi?id=707002
.. _713677: https://bugzilla.redhat.com/show_bug.cgi?id=713677
.. _597755: https://bugzilla.redhat.com/show_bug.cgi?id=597755
.. _567086: https://bugzilla.redhat.com/show_bug.cgi?id=567086
.. _539387: https://bugzilla.redhat.com/show_bug.cgi?id=539387
.. _604005: https://bugzilla.redhat.com/show_bug.cgi?id=604005
.. _716352: https://bugzilla.redhat.com/show_bug.cgi?id=716352
