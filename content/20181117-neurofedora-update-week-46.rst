NeuroFedora update: week 46
###########################
:date: 2018-11-17 15:53:58
:author: ankur
:slug: neurofedora-update-week-46
:category: Research
:tags: Community, Computational neuroscience, Free software, NEST, Fedora, NeuroFedora, Planet
:summary: A quick update on NeuroFedora_ at the end of week 46. Brian_ and
          more software are now ready to use.



.. figure:: {static}/images/20181005-NeuroFedoraLogo01.png
    :alt: NeuroFedora logo!
    :target: {static}/images/20181005-NeuroFedoraLogo01.png
    :width: 30%
    :class: text-center img-responsive pagination-centered

    `NeuroFedora logo by Terezahl from the Fedora Design Team <https://pagure.io/design/issue/602>`__

In week 46:

- python-nitime_ was pushed to stable, and is ready to use.
- python-nilearn_ was pushed to stable, and is ready to use.
- python-petlink_ was pushed to stable, and is ready to use.
- python-duecredit_ was pushed to stable, and is ready to use.
- PyLEMS_ was pushed to stable, and is ready to use.
- python-visionegg-quest_ was pushed to stable, and is ready to use.
- python-pyemd_ was approved and is in testing.
- python-pybids_ was approved and is in testing.
- nineML-python_ was approved and is in testing.
- Brian_ (the Brian simulator) was approved and is in testing.
- fsleyes_ was approved and is in testing.
- dcm2niix_ was updated to the latest version.


----

While we were working on these:

- NEURON_ is still a work in progress, but until it is updated to work with a
  new SUNDIALS version, it cannot be packaged. There's an issue open `here
  <https://github.com/neuronsimulator/nrn/issues/113>`__ for this.
- vxl_ needs to be updated, but unfortunately, it is another software that
  bundles an old version of a library, DCMTK_. I've filed a ticket about this
  `here <https://github.com/vxl/vxl/issues/550>`__. As I've mentioned in the
  ticket, I  have neither the experience with DCMTK_ nor the free cycles to
  look into this issue presently.
- A `bug <https://github.com/INCF/nineml-python/issues/40>`__ in nineml-python_
  was fixed.
- There are still a few kinks to clear up before NEST_ can be build with
  `libneurosim <https://github.com/nest/nest-simulator/issues/1063>`__ and
  `MUSIC <https://github.com/INCF/MUSIC/issues/56>`__.

We'll keep at it.

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
.. _python-nitime: https://src.fedoraproject.org/rpms/python-nitime
.. _python-nilearn: https://src.fedoraproject.org/rpms/python-nilearn
.. _python-petlink: https://src.fedoraproject.org/rpms/python-petlink
.. _python-visionegg-quest: https://src.fedoraproject.org/rpms/python-visionegg-quest
.. _python-pyemd: https://src.fedoraproject.org/rpms/python-pyemd
.. _python-duecredit: https://src.fedoraproject.org/rpms/python-duecredit
.. _python-pybids: https://src.fedoraproject.org/rpms/python-pybids
.. _Brian: https://src.fedoraproject.org/rpms/python-brian2
.. _PyLEMS: https://src.fedoraproject.org/rpms/python-PyLEMS
.. _nineML-python: https://src.fedoraproject.org/rpms/python-nineml
.. _dcm2niix: https://src.fedoraproject.org/rpms/dcm2niix
.. _vxl: https://src.fedoraproject.org/rpms/vxl
.. _DCMTK: https://src.fedoraproject.org/rpms/dcmtk
.. _NEURON: https://pagure.io/neuro-sig/NeuroFedora/issue/27
.. _NEST: https://github.com/nest/nest-simulator
