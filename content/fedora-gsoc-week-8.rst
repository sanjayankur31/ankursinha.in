Fedora GSoC: Week 8
###################
:date: 2011-06-18 20:07
:author: ankur
:category: Tech
:tags: Fedora
:slug: fedora-gsoc-week-8

One cannot have a better work environment than to be at home with a
singular task to focus on. I worked quite a bit this week, and I'm still
neck deep in work. As lot of the work is to do with fixing upstream
source, rather than packaging them up and submitting reviews.
Apparently, a while ago, people preferred using static libraries to
shared objects. I've come across four libraries in the past two days
that only provide static libraries. As per the fedora guidelines, if
upstream only provides static libraries, it is okay to package them up
for fedora. However, it isn't suggested. As for now, I'm going to
package the upstream sources as they are, with the static libraries. A
lot of applications that I need to package for my `fedora medical GSoC`_
project are in the queue, and these libraries are acting as bottle
necks. Once all these applications are packaged, I'll spend time on
correcting these libraries and sending patches upstream.

This weeks work list:

#. Susmit took over `ledgersmb`_ which I'm reviewing.
#. I communicated with `Freemedforms`_ and `freediams`_ upstream Eric,
   and luckily got replies. Fixes coming up :)
#. I submitted `klt`_ for review.
#. I submitted `nifticlib`_ for review.
#. I submitted `libtpcmisc`_ and `libtpcimgio`_ for review.
#. I submitted `xmedcon`_ for review. `Amide`_ depends on this.
#. I submitted `tetgen`_ for review.

The irony is that out of the packages that I submitted for review, 90%
are merely build dependencies. Until these pass review, the actual
software on the list are stuck. And yes, we need more reviewers. **These
review tickets aren't much use if you folks don't review them :D**

Have a great weekend!

.. _fedora medical GSoC: https://fedorahosted.org/fedora-medical/report/1
.. _ledgersmb: https://bugzilla.redhat.com/show_bug.cgi?id=604005
.. _Freemedforms: https://bugzilla.redhat.com/show_bug.cgi?id=707002
.. _freediams: https://bugzilla.redhat.com/show_bug.cgi?id=705104
.. _klt: https://bugzilla.redhat.com/show_bug.cgi?id=713677
.. _nifticlib: https://bugzilla.redhat.com/show_bug.cgi?id=714047
.. _libtpcmisc: https://bugzilla.redhat.com/show_bug.cgi?id=714326
.. _libtpcimgio: https://bugzilla.redhat.com/show_bug.cgi?id=714327
.. _xmedcon: https://bugzilla.redhat.com/show_bug.cgi?id=714328
.. _Amide: https://bugzilla.redhat.com/show_bug.cgi?id=666726
.. _tetgen: https://bugzilla.redhat.com/show_bug.cgi?id=714336
