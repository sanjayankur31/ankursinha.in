Fedora GSoC: Week 7
###################
:date: 2011-06-14 14:09
:author: ankur
:category: Tech
:tags: Fedora
:slug: fedora-gsoc-week-7

This one's a little later than usual. I've been travelling and just
arrived at my destination.

I'd describe the week as eventful, but we'll come back to that later.
First, the progress:

I submitted `Aeskulap`_ and `kradview`_ for review. I also packaged
`Fiji`_ (most of it anyway), until I ran into `j3d`_. J3d is a build
dependency for Fiji which isn't in the Fedora repository as of now. When
attempting to package Fiji, I came across issues that might spoil the
pie here:  J3d makes use of components that have non free licenses. I've
`mailed the -legal list regarding this and already received a reply`_. I
need to work more on this.

Other than this, I've just finished "unbundling" quazip from freediams.
It now uses the fedora package. freediams used a qmake build system, and
it took me a while to uncover how to make it point to the fedora
package. It turned out to be quite simple actually:

#. Remove all mentions of the quazip project files in the main project
   file
#. Append %{\_includedir}/quazip to the INCLUDEPATH variable in the main
   project file

Mario and Narasim have accepted `dcm4che`_ and `freemedforms`_ for
review respectively. I expect to have these packages approved by the end
of this week.

This week, I'm going after `tickets`_ 18 through 22. Let us see how it
goes!

.. _Aeskulap: https://bugzilla.redhat.com/show_bug.cgi?id=aeskulap
.. _kradview: https://bugzilla.redhat.com/show_bug.cgi?id=kradview
.. _Fiji: https://fedorahosted.org/fedora-medical/ticket/17
.. _j3d: https://java3d.dev.java.net/
.. _mailed the -legal list regarding this and already received a reply: http://lists.fedoraproject.org/pipermail/legal/2011-June/001678.html
.. _dcm4che: https://bugzilla.redhat.com/show_bug.cgi?id=dcm4che
.. _freemedforms: https://bugzilla.redhat.com/show_bug.cgi?id=freemedforms
.. _tickets: https://fedorahosted.org/fedora-medical/report/1
