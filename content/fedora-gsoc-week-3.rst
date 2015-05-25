Fedora GSoC : Week 3
####################
:date: 2011-05-15 20:19
:author: ankur
:category: Tech
:tags: Fedora
:slug: fedora-gsoc-week-3

SO! We are picking up steam! This week was way more constructive than
the `last one`_.

To start with, I finished updating the `wiki pages`_, which was pending
from last week. Following this, I went ahead and tried packaging
`dcm4che`_ and `mayam`_. These are both high on the priority list.
dcm4che is just a little stuck. There are some `test images`_ that are
build dependencies for the package. As per fedora policies, these must
be built from source, and, sadly enough, I can't find the source. Mayam
in turn, depends on dcm4che, and therefore will have to wait.

Top on my TODO list for this week is to mail upstream and get sources
for the test images, so we can move the dcm4che packaging (and mayam)
along. I'm going to accept other tickets and start writing up specs.
This will give us a much better idea of what other builddeps we need
packaged.

The board elections are coming up, and **all** my votes are going to my
friend `EvilBob`_ (Robert 'Bob' Jensen for those who don't know)!! He's
an absolutely amazing person and I can't help looking up to him for this
and all his contributions to Fedora and FOSS!

Cheers!

.. _last one: http://dodoincfedora.wordpress.com/2011/05/09/fedora-gsoc-week-2/
.. _wiki pages: http://fedoraproject.org/wiki/SIGs/FedoraMedical
.. _dcm4che: https://fedorahosted.org/fedora-medical/ticket/11
.. _mayam: https://fedorahosted.org/fedora-medical/ticket/11
.. _test images: http://lists.fedoraproject.org/pipermail/java-devel/2011-May/004172.html
.. _EvilBob: http://blogs.fedoraunity.org/bobjensen/fedora-project-and-the-fedora-board
