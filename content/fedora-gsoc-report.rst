Fedora GSoC: Report
###################
:date: 2011-08-20 13:21
:author: ankur
:category: Tech
:tags: Fedora
:slug: fedora-gsoc-report

The soft pencils down date has passed. I'm to submit a report soon. I
thought I'd blog one first ;)

Here's the complete package list that I've worked on, with their current
statuses. There is a huge dependency chain here. Most of the packages
require their build deps to be packaged first.

+----------------------+--------------------------------------------------------------------------------------------------------------+
| Package              |   Status                                                                                                     |
+======================+==============================================================================================================+
| Aeskulap             | Packaged                                                                                                     |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| ANTs                 | Spec in progress. Waiting on ITK.                                                                            |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| bio-formats          | Spec in progress. Waiting on omero                                                                           |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| bioimagexd           | Spec in progress                                                                                             |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| Conquest             | Patched makefile to add support for different data bases. Spec in progress                                   |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| dcm4che              | `Review in progress`_                                                                                        |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| dcm4che-test         | Packaged. Was required for dcm4che                                                                           |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| elmer-eio            | `Needs reviewer - https://bugzilla.redhat.com/show_bug.cgi?id=715618`_                                       |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| elmer-fem            | `Needs reviewer - https://bugzilla.redhat.com/show_bug.cgi?id=715620`_                                       |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| elmer-elmergrid      | `Needs reviewer - https://bugzilla.redhat.com/show_bug.cgi?id=715619`_                                       |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| elmer-hutiter        | `Needs reviewer - https://bugzilla.redhat.com/show_bug.cgi?id=715498`_                                       |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| elmer-matc           | `Needs reviewer - https://bugzilla.redhat.com/show_bug.cgi?id=715496`_                                       |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| elmer-meshgen2d      | `Needs reviewer - https://bugzilla.redhat.com/show_bug.cgi?id=715503`_                                       |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| fiji                 | Bad license. Review closed WONTFIX                                                                           |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| freediams            | `Review in progress - https://bugzilla.redhat.com/show_bug.cgi?id=freediams`_                                |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| FreeMat              | `Review in progress - https://bugzilla.redhat.com/show_bug.cgi?id=715180`_                                   |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| freemedforms         | Packaged                                                                                                     |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| Ginkgo-CADx          | `Needs reviewer - https://bugzilla.redhat.com/show_bug.cgi?id=726201`_                                       |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| gnumed               | Packaged                                                                                                     |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| GoFigure2            | `Needs reviewer - https://bugzilla.redhat.com/show_bug.cgi?id=720121`_                                       |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| klt                  | Packaged. Build dep for VXL                                                                                  |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| kradview             | `Needs reviewer - https://bugzilla.redhat.com/show_bug.cgi?id=710995`_                                       |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| ledgersmb            | `Needs Reviewer - https://bugzilla.redhat.com/show_bug.cgi?id=732232`_. Took over review from Rakesh         |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| libtpcimgio          | Packaged. Build dep for xmedcon                                                                              |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| libtpcmisc           | Packaged. Build dep for xmedcon                                                                              |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| mayam                | Waiting on dcm4che                                                                                           |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| metis                | Bad License. Review closed WONTFIX                                                                           |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| mood-track           | Ruby package. I got no clue on how to do this. Later                                                         |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| nifticlib            | Packaged. Build dep for xmedcon                                                                              |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| omero                | Spec in progress. In dialogue with upstream                                                                  |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| o-palm               | `Needs reviewer - https://bugzilla.redhat.com/show_bug.cgi?id=715154`_                                       |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| opendental           | Mono package. Later                                                                                          |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| openemr              | `Needs reviewer - https://bugzilla.redhat.com/show_bug.cgi?id=730691`_. Took over review from Rakesh         |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| OpenHRE              | Spec in progress                                                                                             |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| OpenNL               | Packaged. Build dep for vmtk                                                                                 |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| OSGI-bundle-ant-task | Packaged. Build dep for bio-formats                                                                          |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| python-hl7           | Packaged                                                                                                     |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| tetgen               | `Review in progress - https://bugzilla.redhat.com/show_bug.cgi?id=714336`_. Probably a WONTFIX. Bad license  |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| toothchart           | Packaged                                                                                                     |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| vmtk                 | `In review - https://bugzilla.redhat.com/show_bug.cgi?id=721112`_. Depends on vxl                            |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| xmedcon              | Packaged                                                                                                     |
+----------------------+--------------------------------------------------------------------------------------------------------------+


**Summary**:

Packaged: 13

In review (or needs reviewer): 16

Wasted: 2

The rest are still in progress: Either waiting for a build dependency to
be approved, or in dialogue with upstream over the build process.

I've done a couple of reviews as well, swaps etc. but since they aren't
all fedora-medical related, I won't include them here.

*EDIT- Aug 21: Added links to bug reports needing reviewer ;)*

.. _Review in progress: https://bugzilla.redhat.com/show_bug.cgi?id=710212
.. _Needs reviewer - https://bugzilla.redhat.com/show_bug.cgi?id=715618: https://bugzilla.redhat.com/show_bug.cgi?id=715618
.. _Needs reviewer - https://bugzilla.redhat.com/show_bug.cgi?id=715620: https://bugzilla.redhat.com/show_bug.cgi?id=715620
.. _Needs reviewer - https://bugzilla.redhat.com/show_bug.cgi?id=715619: https://bugzilla.redhat.com/show_bug.cgi?id=715619
.. _Needs reviewer - https://bugzilla.redhat.com/show_bug.cgi?id=715498: https://bugzilla.redhat.com/show_bug.cgi?id=715498
.. _Needs reviewer - https://bugzilla.redhat.com/show_bug.cgi?id=715496: https://bugzilla.redhat.com/show_bug.cgi?id=715496
.. _Needs reviewer - https://bugzilla.redhat.com/show_bug.cgi?id=715503: https://bugzilla.redhat.com/show_bug.cgi?id=715503
.. _Review in progress - https://bugzilla.redhat.com/show_bug.cgi?id=freediams: https://bugzilla.redhat.com/show_bug.cgi?id=freediams
.. _Review in progress - https://bugzilla.redhat.com/show_bug.cgi?id=715180: https://bugzilla.redhat.com/show_bug.cgi?id=715180
.. _Needs reviewer - https://bugzilla.redhat.com/show_bug.cgi?id=726201: https://bugzilla.redhat.com/show_bug.cgi?id=726201
.. _Needs reviewer - https://bugzilla.redhat.com/show_bug.cgi?id=720121: https://bugzilla.redhat.com/show_bug.cgi?id=720121
.. _Needs reviewer - https://bugzilla.redhat.com/show_bug.cgi?id=710995: https://bugzilla.redhat.com/show_bug.cgi?id=710995
.. _Needs Reviewer - https://bugzilla.redhat.com/show_bug.cgi?id=732232: https://bugzilla.redhat.com/show_bug.cgi?id=732232
.. _Needs reviewer - https://bugzilla.redhat.com/show_bug.cgi?id=715154: https://bugzilla.redhat.com/show_bug.cgi?id=715154
.. _Needs reviewer - https://bugzilla.redhat.com/show_bug.cgi?id=730691: https://bugzilla.redhat.com/show_bug.cgi?id=730691
.. _Review in progress - https://bugzilla.redhat.com/show_bug.cgi?id=714336: https://bugzilla.redhat.com/show_bug.cgi?id=714336
.. _In review - https://bugzilla.redhat.com/show_bug.cgi?id=721112: https://bugzilla.redhat.com/show_bug.cgi?id=721112
