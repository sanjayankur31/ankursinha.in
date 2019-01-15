NeuroFedora update: week 45
###########################
:date: 2018-11-10 11:20:00
:author: ankur
:slug: neurofedora-update-week-45
:category: Research
:tags: Community, Computational neuroscience, Free software, NEST, Fedora, NeuroFedora, Planet
:summary: A quick update on NeuroFedora_ at the end of week 45. More software,
          some housekeeping, and a few upstream tickets.


.. figure:: {static}/images/20181005-NeuroFedoraLogo01.png
    :alt: NeuroFedora logo!
    :target: {static}/images/20181005-NeuroFedoraLogo01.png
    :width: 30%
    :class: text-center img-responsive pagination-centered

    `NeuroFedora logo by Terezahl from the Fedora Design Team <https://pagure.io/design/issue/602>`__

In week 45:

- libneurosim_ was pushed to the stable repositories. NEST_ does not build with
  it yet, because NEST_ tries to link with both libneurosim_ and its Python
  bindings during the build. I've filed a `ticket upstream
  <https://github.com/nest/nest-simulator/issues/1063>`__  to clarify if this
  is correct. I have already `filed a PR
  <https://github.com/INCF/libneurosim/issues/12>`__ that puts the libneurosim_
  Python bindings in the right location.
- python-libNeuroML_ was pushed to the stable repositories and is now ready to use.
- biosig_ is a WIP. It required libb64_ which was approved this week and is
  currently in testing.
- python-duecredit_ is currently in testing. It should be pushed to stable in a
  few days.
- python-visionegg-quest_ is currently in testing. It should be pushed to stable in a
  few days.
- python-nibabel_ was updated to the latest version and is currently in
  testing.
- python-grabbit_ was updated to the latest version and is currently in
  testing.
- On the way to building fsleyes_, fslpy_, fsleyes-props_, fsleyes-widgets_
  have all been reviewed, approved, and are now in testing.
- python-nitime_ was approved and is in testing.
- python-nilearn_ was approved and is in testing.
- python-petlink_ was approved and is in testing. This also required an update
  to python-simplewrap_. Upstream was really quick to `make the required fixes
  for us <https://github.com/spedemon/petlink/issues/2>`__.


All new packages must go through Fedora_'s QA (testing) process before being
made available to end users in the repositories. You can help test these
packages following the instructions `here
<https://fedoraproject.org/wiki/QA:Updates_Testing?rd=QA/Updates_Testing>`__.

A lot of the software we worked on this week was related to neuro-imaging, and
fortunately, a lot of it was Python based which is usually quite simple to
build. The coming week, though, I intend to work on NEURON_. Unfortunately,
NEURON_ isn't the easiest to build:

- It depends on iv_, which bundles a really old version of libtiff_. I've filed
  a ticket `here <https://github.com/neuronsimulator/iv/issues/3>`__ about
  this, but have not had the time to port the code to the newest version of
  libtiff_.
- NEURON_ bundles Random123_, which was relatively easy to remove. However,
  NEURON_ also bundles a really old version of the SUNDIALS_ libraries, and
  updating the code to use the latest versions is not straightforward. I have
  filed an issue about it `here
  <https://github.com/neuronsimulator/nrn/issues/113>`__ now. This is based on
  my initial investigations into building NEURON_. So there's a chance that
  more work will need to be done once these issues are solved.



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


The Fedora community: enabling Open Science
-------------------------------------------

While the NeuroFedora_ SIG is actively working on these packages, it would not
be possible without our friends in the Fedora_ community that have helped with
the various stages of the package maintenance pipeline.

- eclipseo_, churchyard_, blackfile_, zbyszek_ have reviewed these packages
  before approving them for inclusion in Fedora_.
- The awesome folks at releng_ have, of course, been super quick with SCM
  requests.

We're grateful to the various upstreams that we're bothering with issues, and
everyone in the Fedora_ community (including people I may have missed) for
enabling us to further `Open Science`_ via Fedora_.


.. _NeuroFedora: https://neuro.fedoraproject.org
.. _NEST: https://github.com/nest/nest-simulator/wiki/issue-labeling-scheme
.. _libneurosim: https://src.fedoraproject.org/rpms/libneurosim
.. _python-libNeuroML: https://src.fedoraproject.org/rpms/python-libNeuroML
.. _biosig: https://pagure.io/neuro-sig/NeuroFedora/issue/56
.. _libb64: https://src.fedoraproject.org/rpms/libb64
.. _python-duecredit: https://src.fedoraproject.org/rpms/python-duecredit
.. _python-visionegg-quest: https://src.fedoraproject.org/rpms/python-visionegg-quest
.. _python-nibabel: https://src.fedoraproject.org/rpms/python-nibabel
.. _python-grabbit: https://src.fedoraproject.org/rpms/python-grabbit
.. _fslpy: https://src.fedoraproject.org/rpms/python-fslpy
.. _fsleyes-widgets: https://src.fedoraproject.org/rpms/python-fsleyes-widgets
.. _fsleyes-props: https://src.fedoraproject.org/rpms/python-fsleyes-props
.. _fsleyes: https://pagure.io/neuro-sig/NeuroFedora/issue/3
.. _python-nitime: https://src.fedoraproject.org/rpms/python-nitime
.. _python-nilearn: https://src.fedoraproject.org/rpms/python-nilearn
.. _python-petlink: https://src.fedoraproject.org/rpms/python-petlink
.. _python-simplewrap: https://src.fedoraproject.org/rpms/python-simplewrap
.. _NEURON: https://pagure.io/neuro-sig/NeuroFedora/issue/27
.. _iv: https://github.com/neuronsimulator/iv
.. _libtiff: http://www.simplesystems.org/libtiff/
.. _SUNDIALS: https://computation.llnl.gov/projects/sundials
.. _Random123: https://src.fedoraproject.org/rpms/Random123
.. _blackfile: https://fedoraproject.org/wiki/User:Blackfile
.. _eclipseo: https://fedoraproject.org/wiki/User:Eclipseo
.. _zbyszek: https://fedoraproject.org/wiki/User:Zbyszek
.. _churchyard: https://fedoraproject.org/wiki/User:Churchyard
.. _releng: https://pagure.io/releng
.. _Fedora: https://getfedora.org
.. _Open Science: https://en.wikipedia.org/wiki/Open_science
