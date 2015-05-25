Fedora GSoC: Week 6
###################
:date: 2011-06-05 13:33
:author: ankur
:category: Tech
:tags: Fedora
:slug: fedora-gsoc-week-6

Since `dcm4che-test`_ was approved last week, I spent most of the week
on `dcm4che`_. It was a much larger package than I had expected with 30+
jar files (`which implies 30+ pom files`_). The thing about `java
packaging`_ is that one needs to manually install the generated jar
files and the pom files. After installing the pom files, one also needs
to look at each one individually and add them to the maven depmap. I
think I've done it correctly, but the reviewer will decide on that :)

I'm working on kradview currently. The spec is almost complete.

I have a bare spec for conquest too. Unfortunately,  it has a bunch of
bundled libraries and doesn't use a build system at all. This makes it a
tedious software to package.

The `freediams`_ spec was finished two weeks back. Volker `pointed out`_
that it has a bundled quazip library which needs to be replaced with
fedora's version. I'm working on it. The spec looks really ugly with
patches and sed commands which I've inserted to remove the bundled
quazip from the project build files now. I'll try and clean it up once I
can get it to build correctly.

I reviewed and approved the `gnumed-server`_ package for Susmit earlier.
He's now going to work on gnumed-client.

It was a decent week. Dcm4che was the "big one" really. Time to get back
to work :)

.. _dcm4che-test: https://bugzilla.redhat.com/show_bug.cgi?id=707613
.. _dcm4che: https://bugzilla.redhat.com/show_bug.cgi?id=710212
.. _which implies 30+ pom files: http://ankursinha.fedorapeople.org/dcm4che/dcm4che.spec
.. _java packaging: fedoraproject.org/wiki/Packaging/Java
.. _freediams: https://bugzilla.redhat.com/show_bug.cgi?id=705104
.. _pointed out: https://bugzilla.redhat.com/show_bug.cgi?id=705104#c5
.. _gnumed-server: https://bugzilla.redhat.com/show_bug.cgi?id=669146
