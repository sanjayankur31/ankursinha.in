NeuroFedora update: week 42
###########################
:date: 2018-10-20 16:05:16
:author: ankur
:category: Research
:tags: Community, Computational neuroscience, Free software, NEST, Fedora, NeuroFedora
:slug: neurofedora-update-week-42
:summary: A quick update on NeuroFedora_ at the end of week 42.

.. figure:: {static}/images/20181005-NeuroFedoraLogo01.png
    :alt: NeuroFedora logo!
    :target: {static}/images/20181005-NeuroFedoraLogo01.png
    :width: 30%
    :class: text-center img-responsive pagination-centered

    `NeuroFedora logo by Terezahl from the Fedora Design Team <https://pagure.io/design/issue/602>`__


In week 42:

- NEST_ 2.16.0 has hit the stable repositories. The different variants (with
  and without MPI) can now be easily installed using one or two DNF commands.
  You can find more information on installing NEST_ on Fedora `here
  <https://src.fedoraproject.org/rpms/nest>`__.
- libneurosim_ has been submitted for `review
  <https://bugzilla.redhat.com/show_bug.cgi?id=1638968>`__. I expect it'll be
  approved soon. I learned a few new things about building RPM packages while I
  was at it too. Once libneurosim_ is approved and built, NEST_ will be rebuilt
  to support it too, and then I intend to work on PyNN_.
- I almost have MUSIC_ ready for review. I expect to submit a review ticket
  soon.

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
.. _MUSIC: https://github.com/INCF/MUSIC
