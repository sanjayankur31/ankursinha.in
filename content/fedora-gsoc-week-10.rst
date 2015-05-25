Fedora GSoC: Week 10
####################
:date: 2011-07-03 17:50
:author: ankur
:category: Tech
:tags: Fedora
:slug: fedora-gsoc-week-10

Like I had said, I didn't try to package any new applications this week.
(I did actually, but I haven't submitted any review tickets this week).
This week was about working on the existing review tickets.

To start with, "`toothchart`_\ " was reviewed and approved. I'm grateful
to Mario Blättermann, who swapped a review with me. I reviewed and
approved `**Bug 701079 (wmSun)**`_ for him in return.

I've made a few changes to the elmer related suites. I followed `Jussi's
suggestion`_ and removed the elmer metapackage. The `elmer-fem`_ package
now provides elmer and requires the other tools. Please note that the
updated elmer-fem package has not been put up for review yet. There were
quite a few rpmlint errors, and I've e-mailed upstream to try and solve
these before I submit a new package.

Richard has begun to review the `aeskulap`_ package for me. The build
process requires calling autoconf which is `advised against in the
guidelines`_. One of the solutions listed on the same page, suggests
running autoconf locally and then generating a patch. This worked for me
on F15, but `failed for Richard on his F14`_. I think I'll have to fall
back to calling autoconf in the spec here. I'll write a mail to the
devel list requesting input tonight.

I ran into FE-LEGAL issues with a few packages this week. `Metis is non
free, and I had to drop the review`_. I'm building elmer without metis
support. Upstream suggested it. `I had to let go of tetgen as well`_.
Fortunately, tetgen isn't a build dependency for any of the packages.
Tetgen was a little frustrating. The license is mainly the MIT license
with one `addition`_. The one line addition is enough to make it non
FOSS :/

I submitted a fresh `srpm for freemat with corrections`_. The only
rpmlint errors are "incorrect-fsf-address" errors which I've mailed
upstream about. It should get approved soon.

The `kradview package looks good too`_. I hope it's on the verge of
being approved.

I had an hour or two extra on my hands one of these days. `I used this
to patch the Makefile to generate shared objects for klt`_. The package
looks good too, reviewer needed.

**What you'll notice from all these packages is that they're waiting for
someone to review them. If you have time, I'll be more than happy to
swap reviews with you!!**

.. _toothchart: https://fedorahosted.org/fedora-medical/ticket/25#comment:2
.. _**Bug 701079 (wmSun)**: https://bugzilla.redhat.com/show_bug.cgi?id=701079
.. _Jussi's suggestion: https://bugzilla.redhat.com/show_bug.cgi?id=716344#c1
.. _elmer-fem: https://bugzilla.redhat.com/show_bug.cgi?id=715620
.. _aeskulap: https://bugzilla.redhat.com/show_bug.cgi?id=712624
.. _advised against in the guidelines: http://fedoraproject.org/wiki/PackagingDrafts/AutoConf
.. _failed for Richard on his F14: https://bugzilla.redhat.com/show_bug.cgi?id=712624#c6
.. _Metis is non free, and I had to drop the review: https://bugzilla.redhat.com/show_bug.cgi?id=715314#c4
.. _I had to let go of tetgen as well: https://bugzilla.redhat.com/show_bug.cgi?id=714336
.. _addition: https://bugzilla.redhat.com/show_bug.cgi?id=714336#c7
.. _srpm for freemat with corrections: https://bugzilla.redhat.com/show_bug.cgi?id=715180#c5
.. _kradview package looks good too: https://bugzilla.redhat.com/show_bug.cgi?id=710995#c2
.. _I used this to patch the Makefile to generate shared objects for klt: https://bugzilla.redhat.com/show_bug.cgi?id=713677
