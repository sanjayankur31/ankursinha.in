NeuroFedora update: week 48
###########################
:date: 2018-12-02 15:26:50
:author: ankur
:slug: neurofedora-update-week-48
:category: Research
:tags: Community, Matlab, Computational neuroscience, Free software, Fedora, NeuroFedora, Planet
:summary: An update on NeuroFedora_ at the end of week 48.


.. figure:: {static}/images/20181005-NeuroFedoraLogo01.png
    :alt: NeuroFedora logo!
    :target: {static}/images/20181005-NeuroFedoraLogo01.png
    :width: 30%
    :class: text-center img-responsive pagination-centered

    `NeuroFedora logo by Terezahl from the Fedora Design Team <https://pagure.io/design/issue/602>`__

In week 48:

- `python-chaospy`_ was approved and is in testing.
- `python-pynwb`_ was approved and is in testing.
- `python-pyphi`_ was pushed to stable.
- we've started looking into packaging FSL_
- `PyNN does not support the latest version of NEST yet
  <https://github.com/NeuralEnsemble/PyNN/issues/611>`__, so we're waiting on
  upstream here.

Packaging MATLab tool boxes
----------------------------

The use of MATLab tool boxes is quite common in data-analysis. There's a
noticeable movement in the scientific community towards using Python, but the
work that has already been done, and the eco-systems that have developed around
MATlab will take time to migrate to a Python based eco-system.

A majority of the tool boxes in use are Free/Open Source, but MATLab itself is
not. As supporters of Free/Open source, we will not attempt to include MATLab
in Fedora, but the question remains on whether we provide the toolboxes.  We've
begun discussing this in the SIG, and we'll reach out to the broader Fedora
community before we decide on how to proceed.

Personal views
===============

Personally, I'd prefer if we only provided software that support Free/Open
source eco systems. The use of proprietary software in science, while currently
necessary, should be avoided.  Yes, it may make things a little harder to start
with, but the Free/Open source tools that will be used will be accessible by
all. Overtime, just like the Free software community, the eco system will
mature.

A example case is the use of Microsoft products that is common in developed
countries where universities can afford their licenses. In developing
countries, this is not the case. They cannot always afford these fees. A
solution, of course, is to use LaTeX_ which is free for all to use, extend,
study, and share. Similarly, while universities and laboratories in developed
countries may be able to pay for MATlab licenses, this financial requirement
can hold back others---smaller labs and independent researchers.

If proprietary tools such as MATlab are the norm, then science is not open to
all. It should be.

(I've signed the `Open source for Neuroscience letter that you can read
here <http://opensourceforneuroscience.org/>`__.)

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



.. _python-pyphi: https://src.fedoraproject.org/rpms/python-pyphi
.. _python-pynwb: https://src.fedoraproject.org/rpms/python-pynwb
.. _python-chaospy: https://src.fedoraproject.org/rpms/python-chaospy
.. _NeuroFedora: https://neuro.fedoraproject.org
.. _FSL: https://git.fmrib.ox.ac.uk/fsl
.. _LaTeX: https://www.latex-project.org
