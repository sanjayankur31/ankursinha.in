NeuroFedora update: week 43
###########################
:date: 2018-10-27 10:56:49
:author: ankur
:category: Research
:tags: Community, Computational neuroscience, Free software, NEST, Fedora, NeuroFedora
:slug: neurofedora-update-week-43
:summary: A quick update on NeuroFedora_ at the end of week 43.

.. figure:: {static}/images/20181005-NeuroFedoraLogo01.png
    :alt: NeuroFedora logo!
    :target: {static}/images/20181005-NeuroFedoraLogo01.png
    :width: 30%
    :class: text-center img-responsive pagination-centered

    `NeuroFedora logo by Terezahl from the Fedora Design Team <https://pagure.io/design/issue/602>`__


In week 43:

- libneurosim_ was `reviewed and approved
  <https://bugzilla.redhat.com/show_bug.cgi?id=1638968>`__ and is `currently in
  testing <https://bodhi.fedoraproject.org/updates/?packages=libneurosim>`__.
  PyNN_ needs NEST_ to be built with libneurosim_ support, so that'll have to
  be done before PyNN_ can be submitted for review. That's next on the list.
- libNeuroML_ was also `reviewed and approved this week
  <https://bugzilla.redhat.com/show_bug.cgi?id=1643266>`__, and is `now in
  testing <https://bodhi.fedoraproject.org/updates/?packages=python-libNeuroML>`__. It
  should be available for use in the stable repositories in a week.  I can now
  work on packaging up pyNeuroML_.

There is a lot of software available in NeuroFedora_ already. You can see the
list `here <https://fedoraproject.org/wiki/SIGs/NeuroFedora/PackageSet>`__. If
you use software that is not on our list, please suggest it to us using the
`suggestion form <https://goo.gl/forms/j6AJ82yOh78MPxby1>`__.

Feedback is always welcome. You can get in touch with us `here
<https://fedoraproject.org/wiki/SIGs/NeuroFedora#Communication_and_getting_help>`__.


.. _NeuroFedora: https://neuro.fedoraproject.org
.. _NEST: http://nest-simulator.org
.. _PyNN: https://github.com/NeuralEnsemble/PyNN
.. _libneurosim: https://github.com/INCF/libneurosim
.. _libNeuroML: https://github.com/NeuralEnsemble/libNeuroML
.. _pyNeuroML: https://github.com/NeuroML/pyNeuroML
