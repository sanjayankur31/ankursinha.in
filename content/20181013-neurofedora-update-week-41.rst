NeuroFedora update: week 41
###########################
:date: 2018-10-13 18:11:53
:author: ankur
:category: Research
:tags: Community, Computational neuroscience, Free software, NEST, Fedora,
       NeuroFedora
:slug: neurofedora-update-week-41
:summary: A quick update on NeuroFedora_ at the end of week 41.

.. figure:: {static}/images/20181005-NeuroFedoraLogo01.png
    :alt: NeuroFedora logo!
    :target: {static}/images/20181005-NeuroFedoraLogo01.png
    :width: 30%
    :class: text-center img-responsive pagination-centered

    `NeuroFedora logo by Terezahl from the Fedora Design Team <https://pagure.io/design/issue/602>`__


In week 41, we finally announced NeuroFedora_ to the community on the `mailing
list <https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/VXN4UBCNIL6BUCDRN55IGVK3IMO3HF6C/>`__
and on the `Fedora Community Blog <https://communityblog.fedoraproject.org/neurofedora-sig-call-for-participation/>`__.
So, it is officially a thing!

There is a lot of software available in NeuroFedora_ already. You can see the
list `here <https://fedoraproject.org/wiki/SIGs/NeuroFedora/PackageSet>`__. If
you use software that is not on our list, please suggest it to us using the
`suggestion form <https://goo.gl/forms/j6AJ82yOh78MPxby1>`__.

In week 41:

- NEST_ was updated to `version 2.16.0
  <https://github.com/nest/nest-simulator/releases/tag/v2.16.0>`__. It is in
  testing for both `Fedora 28
  <https://bodhi.fedoraproject.org/updates/FEDORA-2018-22afaeeee4>`__ and
  `Fedora 29
  <https://bodhi.fedoraproject.org/updates/FEDORA-2018-6a80c3dbb1>`__. They
  should both move to the stable repositories in a few days. This new version
  does not support 32 bit architectures, so I've had to drop support for those.
- libneurosim_ has now been submitted for `review
  <https://bugzilla.redhat.com/show_bug.cgi?id=1638968>`__. NEST_ must be
  built with libneurosim_ support for PyNN_ to work with it properly. So PyNN_
  will have to wait until this review is approved and NEST_ rebuilt.

I am hoping to spend some time on NeuroFedora_ every week, and I will provide
regular updates as I do. Feedback is always welcome. You can get in touch with
us `here <https://fedoraproject.org/wiki/SIGs/NeuroFedora#Communication_and_getting_help>`__.

.. _NeuroFedora: https://neuro.fedoraproject.org
.. _NEST: http://nest-simulator.org
.. _PyNN: https://github.com/NeuralEnsemble/PyNN
.. _libneurosim: https://github.com/INCF/libneurosim
