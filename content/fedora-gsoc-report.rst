Fedora GSoC: Report
###################
:date: 2011-08-20 13:21
:author: ankur
:category: FOSS
:tags: fedora-gsoc, fedora-medical
:tags: fedora-gsoc, fedora-medical
:tags: fedora-gsoc, fedora-medical
:tags: fedora-gsoc, fedora-medical
:tags: fedora-gsoc, fedora-medical
:tags: fedora-gsoc, fedora-medical
:tags: fedora-gsoc, fedora-medical
:tags: fedora-gsoc, fedora-medical
:slug: fedora-gsoc-report

The soft pencils down date has passed. I'm to submit a report soon. I
thought I'd blog one first ;)

Here's the complete package list that I've worked on, with their current
statuses. There is a huge dependency chain here. Most of the packages
require their build deps to be packaged first.

.. raw:: html

   <table>

.. raw:: html

   <tbody>

.. raw:: html

   <tr>

.. raw:: html

   <th>

    Package

.. raw:: html

   </th>

.. raw:: html

   <th>

    Status

.. raw:: html

   </th>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    Aeskulap

.. raw:: html

   </td>

.. raw:: html

   <td>

    Packaged

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    ANTs

.. raw:: html

   </td>

.. raw:: html

   <td>

    Spec in progress. Waiting on ITK.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    bio-formats

.. raw:: html

   </td>

.. raw:: html

   <td>

    Spec in progress. Waiting on omero

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    bioimagexd

.. raw:: html

   </td>

.. raw:: html

   <td>

    Spec in progress

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    Conquest

.. raw:: html

   </td>

.. raw:: html

   <td>

    Patched makefile to add support for different data bases. Spec in
    progress

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    dcm4che

.. raw:: html

   </td>

.. raw:: html

   <td>

    `Review in progress`_

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    dcm4che-test

.. raw:: html

   </td>

.. raw:: html

   <td>

    Packaged. Was required for dcm4che

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    elmer-eio

.. raw:: html

   </td>

.. raw:: html

   <td>

    `Needs reviewer`_

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    elmer-fem

.. raw:: html

   </td>

.. raw:: html

   <td>

    `Needs reviewer <https://bugzilla.redhat.com/show_bug.cgi?id=715620>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    elmer-elmergrid

.. raw:: html

   </td>

.. raw:: html

   <td>

    `Needs reviewer <https://bugzilla.redhat.com/show_bug.cgi?id=715619>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    elmer-hutiter

.. raw:: html

   </td>

.. raw:: html

   <td>

    `Needs reviewer <https://bugzilla.redhat.com/show_bug.cgi?id=715498>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    elmer-matc

.. raw:: html

   </td>

.. raw:: html

   <td>

    `Needs reviewer <https://bugzilla.redhat.com/show_bug.cgi?id=715496>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    elmer-meshgen2d

.. raw:: html

   </td>

.. raw:: html

   <td>

    `Needs reviewer <https://bugzilla.redhat.com/show_bug.cgi?id=715503>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    fiji

.. raw:: html

   </td>

.. raw:: html

   <td>

    Bad license. Review closed WONTFIX

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    freediams

.. raw:: html

   </td>

.. raw:: html

   <td>

    `Review in progress <https://bugzilla.redhat.com/show_bug.cgi?id=freediams>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    FreeMat

.. raw:: html

   </td>

.. raw:: html

   <td>

    `Review in progress <https://bugzilla.redhat.com/show_bug.cgi?id=715180>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    freemedforms

.. raw:: html

   </td>

.. raw:: html

   <td>

    Packaged

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    Ginkgo-CADx

.. raw:: html

   </td>

.. raw:: html

   <td>

    `Needs reviewer <https://bugzilla.redhat.com/show_bug.cgi?id=726201>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    gnumed

.. raw:: html

   </td>

.. raw:: html

   <td>

    Packaged

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    GoFigure2

.. raw:: html

   </td>

.. raw:: html

   <td>

    `Needs reviewer <https://bugzilla.redhat.com/show_bug.cgi?id=720121>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    klt

.. raw:: html

   </td>

.. raw:: html

   <td>

    Packaged. Build dep for VXL

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    kradview

.. raw:: html

   </td>

.. raw:: html

   <td>

    `Needs reviewer <https://bugzilla.redhat.com/show_bug.cgi?id=710995>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    ledgersmb

.. raw:: html

   </td>

.. raw:: html

   <td>

    [STRIKEOUT:Spec in progress]\ `Needs Reviewer`_. Took over review from Rakesh

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    libtpcimgio

.. raw:: html

   </td>

.. raw:: html

   <td>

    Packaged. Build dep for xmedcon

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    libtpcmisc

.. raw:: html

   </td>

.. raw:: html

   <td>

    Packaged. Build dep for xmedcon

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    mayam

.. raw:: html

   </td>

.. raw:: html

   <td>

    Waiting on dcm4che

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    metis

.. raw:: html

   </td>

.. raw:: html

   <td>

    Bad License. Review closed WONTFIX

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    mood-track

.. raw:: html

   </td>

.. raw:: html

   <td>

    Ruby package. I got no clue on how to do this. Later

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    nifticlib

.. raw:: html

   </td>

.. raw:: html

   <td>

    Packaged. Build dep for xmedcon

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    omero

.. raw:: html

   </td>

.. raw:: html

   <td>

    Spec in progress. In dialogue with upstream

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    o-palm

.. raw:: html

   </td>

.. raw:: html

   <td>

    `Needs reviewer <https://bugzilla.redhat.com/show_bug.cgi?id=715154>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    opendental

.. raw:: html

   </td>

.. raw:: html

   <td>

    Mono package. Later

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    openemr

.. raw:: html

   </td>

.. raw:: html

   <td>

    `Needs reviewer <https://bugzilla.redhat.com/show_bug.cgi?id=730691>`__.  Took over review from Rakesh

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    OpenHRE

.. raw:: html

   </td>

.. raw:: html

   <td>

    Spec in progress

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    OpenNL

.. raw:: html

   </td>

.. raw:: html

   <td>

    Packaged. Build dep for vmtk

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    OSGI-bundle-ant-task

.. raw:: html

   </td>

.. raw:: html

   <td>

    Packaged. Build dep for bio-formats

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    python-hl7

.. raw:: html

   </td>

.. raw:: html

   <td>

    Packaged

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    tetgen

.. raw:: html

   </td>

.. raw:: html

   <td>

    `Review in progress <https://bugzilla.redhat.com/show_bug.cgi?id=714336>`__.  Probably a WONTFIX. Bad license

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    toothchart

.. raw:: html

   </td>

.. raw:: html

   <td>

    Packaged

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    vmtk

.. raw:: html

   </td>

.. raw:: html

   <td>

    `In review`_. Depends on vxl

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

    xmedcon

.. raw:: html

   </td>

.. raw:: html

   <td>

    Packaged

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

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
.. _Needs reviewer: https://bugzilla.redhat.com/show_bug.cgi?id=715618
.. _Needs Reviewer: https://bugzilla.redhat.com/show_bug.cgi?id=732232
.. _In review: https://bugzilla.redhat.com/show_bug.cgi?id=721112
