NeuroFedora update: week 47
###########################
:date: 2018-11-24 18:37:28
:author: ankur
:slug: neurofedora-update-week-47
:category: Research
:tags: Community, Computational neuroscience, Free software, NEST, Fedora, NeuroFedora, Planet
:summary: A quick update on NeuroFedora_ at the end of week 47. We've made more
          progress on the software that we're trying to provide. More
          importantly, more volunteers have joined the core team!


.. figure:: {static}/images/20181005-NeuroFedoraLogo01.png
    :alt: NeuroFedora logo!
    :target: {static}/images/20181005-NeuroFedoraLogo01.png
    :width: 30%
    :class: text-center img-responsive pagination-centered

    `NeuroFedora logo by Terezahl from the Fedora Design Team <https://pagure.io/design/issue/602>`__

In week 47:

- python-dipy_ was included and is in testing.
- pygiftiio_ was included and is in testing.
- python-pybids_ went stable and is now in testing
- python-pyphi_ was included and is in testing.
- python-efel_ was included and is in testing.
- python-pymatreader_ was included and is in testing.
- python-mne_ was included and is in testing.
- fsleyes_ went stable and is now ready for use.
- NEST_ has now been built with libneurosim_ support and is in testing.
- python-pyemd_ went stable and is now ready for use
- Brian_ went stable and is now ready for use


----

Quite a few Fedora community members have helped us out again this week.
lbazan_, blackfile_, and mhough_ have all joined the `core team
<https://pagure.io/group/neuro-sig>`__ too. In another news:

- upstream `clarified <https://github.com/nest/nest-simulator/issues/1063>`__
  how libneurosim_ was to be used with NEST_. We can now work on PyNN_ so that
  it can at least be used with NEST_ and Brian_.
- NEST_ has been `tweaked to support 32 bit hardware again
  <https://github.com/nest/nest-simulator/pull/1065>`__.
- NEURON_ has been updated to use a more recent version of SUNDIALS_. Once this
  has been merged into the main codebase, we can proceed with packaging NEURON_
  too.
- We've set up a Telegram group for NeuroFedora_ here: https://t.me/NeuroFedora
  We'll bridge this to the `IRC channel
  <https://webchat.freenode.net/?channels=#fedora-neuro>`__ in the near future.
  These channels can be used to get in touch with the team for troubleshooting
  and so on.

----

There is a lot of software available in NeuroFedora_ already. You can see the
complete list `here on Fedora SCM
<https://src.fedoraproject.org/group/neuro-sig>`__. Software that is currently
being worked on is listed `on our Pagure project instance
<https://pagure.io/neuro-sig/NeuroFedora/issues>`__. If you use software that
is not on our list, please suggest it to us using the `suggestion form
<https://goo.gl/forms/j6AJ82yOh78MPxby1>`__.

Feedback is always welcome. You can get in touch with us `here
<https://fedoraproject.org/wiki/SIGs/NeuroFedora#Communication_and_getting_help>`__.


.. _NeuroFedora: https://neuro.fedoraproject.org
.. _fsleyes: https://src.fedoraproject.org/rpms/python-fsleyes
.. _python-dipy: https://src.fedoraproject.org/rpms/python-dipy
.. _python-pybids: https://src.fedoraproject.org/rpms/python-pybids
.. _python-pyphi: https://src.fedoraproject.org/rpms/python-pyphi
.. _python-efel: https://src.fedoraproject.org/rpms/python-efel
.. _python-pymatreader: https://src.fedoraproject.org/rpms/python-pymatreader
.. _python-mne: https://src.fedoraproject.org/rpms/python-mne
.. _python-pyemd: https://src.fedoraproject.org/rpms/python-pyemd
.. _pygiftiio: https://src.fedoraproject.org/rpms/python-pygiftiio
.. _NEURON: https://pagure.io/neuro-sig/NeuroFedora/issue/27
.. _SUNDIALS: https://computation.llnl.gov/projects/sundials
.. _NEST: https://src.fedoraproject.org/rpms/nest
.. _Brian: https://src.fedoraproject.org/rpms/brian
.. _libneurosim: https://src.fedoraproject.org/rpms/libneurosim
.. _PyNN: https://github.com/NeuralEnsemble/PyNN
.. _lbazan: https://fedoraproject.org/wiki/User:Lbazan
.. _blackfile: https://fedoraproject.org/wiki/User:Blackfile
.. _mhough: https://fedoraproject.org/wiki/User:Mhough
