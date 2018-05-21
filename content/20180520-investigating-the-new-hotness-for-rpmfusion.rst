Investigating the-new-hotness for RPMFusion
###########################################
:date: 2018-05-20 13:47:51
:author: ankur
:category: Tech
:tags: Fedora, RPMFusion, Infrastructure, Ansible
:slug: investigating-the-new-hotness-for-rpmfusion
:status: draft
:summary: I was tinkering with the-new-hotness_ to see how it could be deployed
          for RPMFusion_. This document is a set of badly written notes on the
          subject.


.. image:: {filename}/images/20180520-release-monitoring.png
    :alt: Release monitoring at apps.fedoraproject.org
    :target: {filename}/images/20180520-release-monitoring.png
    :width: 80%
    :class: text-center img-responsive pagination-centered


The `Fedora Infrastructure`_ team develops and maintains `lots of tools <https://apps.fedoraproject.org>`__
that make it possible for the community to carry out its function---to spread
Free/Open source software via the awesome Fedora_ Linux distribution. One of
these tools that most of us are aware of is Anitya_, or as we better know it,
https://release-monitoring.org. While Anitya_ monitors upstream locations for
new versions of software and uses the `Fedora fedmsg bus`_ (which you can see
live in action here:
https://apps.fedoraproject.org/datagrepper/raw?rows_per_page=1&delta=127800, or
on `#fedora-fedmsg <https://webchat.freenode.net/?channels=#fedora-fedmsg>`__
on Freenode_) to send out notifications of any new versions it finds,
the-new-hotness_ acts as a Fedmsg consumer to take action based on the
notification.

The aptly named the-new-hotness_ consumes messages that Anitya_ generates to
file bugs notifying package maintainers that a new version of a package they
maintain is now available. the-new-hotness_ now also tries to `carry out
scratch builds
<https://fedoramagazine.org/rebase-helper-tool-rebases-upstream-monitoring-services/>`__
to give the maintainer an idea of how much work this package update may be.
More information on the whole process is `here, on the wiki
<https://fedoraproject.org/wiki/Upstream_release_monitoring>`__.


.. image:: https://rpmfusion.org/moin_static199/rpmfusion/logo.png
    :alt: Release monitoring at apps.fedoraproject.org
    :target: https://rpmfusion.org
    :class: text-center img-responsive pagination-centered


RPMFusion_ provides Fedora users with a lot of additional software that
unfortunately isn't Free/Open source but necessary in daily usage. The
community there is now trying to set up the-new-hotness_ to keep track of the
software it provides. A `tracker ticket is here
<https://bugzilla.rpmfusion.org/show_bug.cgi?id=4897>`__.


.. _the-new-hotness: https://github.com/fedora-infra/the-new-hotness
.. _RPMFusion: https://rpmfusion.org
.. _Fedora: https://getfedora.org
.. _Fedora Infrastructure: https://fedoraproject.org/wiki/Infrastructure
.. _Anitya: https://github.com/fedora-infra/anitya
.. _Fedora fedmsg bus: http://www.fedmsg.com/en/stable/
.. _Freenode: https://freenode.net
