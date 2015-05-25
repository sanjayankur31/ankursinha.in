Fedora GSoC : Week 5
####################
:date: 2011-05-30 01:32
:author: ankur
:category: Tech
:tags: Fedora
:slug: fedora-gsoc-week-5

I did quite a bit of work this week. I really did :P

dcm4che is finally on the verge of packaging. It builds correctly, and
there's a minor glitch in the javadoc generation which I think would be
corrected in a day or two. It's build dependency, `dcm4che-test`_ has
almost passed review. **Mario** has been awesome enough to review the
package for me, and the final version with tweaks is building on mock as
I type! I really must thank **Stanislav Ochotnicky** over at
#fedora-java who had the patience to almost walk me through Java
packaging. Even though I've been a fedora packager for more than 3 years
now, I had never packaged a Java package, and knew nothing about maven
and POMs. The folks at the fedora-java mailing list have been very very
helpful. (**Thanks Alex**!) I wouldn't have managed to package up
dcm4che without all their help.

In other news, **Susmit** (my mentor along with Mario) is going to send
me a list of already packaged software that would enable me to create
the comps group for fedora medical. I had mailed the -devel mailing list
a while back to give them a heads up. As soon as I have the list, I'll
make the required changes and send the diff to the list for review.

I had planned to package up GinkoCADx this week but it's build
dependencies, namely\ `ITK`_ and `VXL`_, are both under review. Mario's
updated the packages and they'd probably be approved in a day or two.

We've picked up momentum, as the critical build dependencies are
packaged  up, it'll take us less time to package the rest. :)

.. _dcm4che-test: https://bugzilla.redhat.com/show_bug.cgi?id=707613
.. _ITK: https://bugzilla.redhat.com/show_bug.cgi?id=539387
.. _VXL: https://bugzilla.redhat.com/show_bug.cgi?id=567086
