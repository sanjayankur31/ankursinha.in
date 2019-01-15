NeuroFedora update: week 44
###########################
:date: 2018-11-03 10:02:24
:author: ankur
:slug: neurofedora-update-week-44
:category: Research
:tags: Community, Computational neuroscience, Free software, NEST, Fedora, NeuroFedora, Planet
:summary: A quick update on NeuroFedora_ at the end of week 44. More software,
          some housekeeping, and a few upstream tickets.

.. figure:: {static}/images/20181005-NeuroFedoraLogo01.png
    :alt: NeuroFedora logo!
    :target: {static}/images/20181005-NeuroFedoraLogo01.png
    :width: 30%
    :class: text-center img-responsive pagination-centered

    `NeuroFedora logo by Terezahl from the Fedora Design Team <https://pagure.io/design/issue/602>`__


In week 44:

- PyLEMS_ was imported into Fedora and is now in `testing
  <https://bodhi.fedoraproject.org/updates/?packages=python-PyLEMS>`__.
- We received a suggestion to include fsleyes_, so we've begun working on that.
  Two of its dependencies are in review now: `fslpy
  <https://bugzilla.redhat.com/show_bug.cgi?id=1645329>`__ and `fsleyes-widgets
  <https://bugzilla.redhat.com/show_bug.cgi?id=1645661>`__.

Keeping in line with the spirit of FOSS development, we try to `stay close to
upstream <https://fedoraproject.org/wiki/Staying_close_to_upstream_projects>`__, so:

- PyLEMS_: issues were filed to request that `examples
  <https://github.com/LEMS/pylems/issues/42>`__ and the `license
  text <https://github.com/LEMS/pylems/issues/39>`__ be included in the PyPi
  tarball.
- NeuroMLlite_: I opened a `PR adding the license file to the sources
  <https://github.com/NeuroML/NeuroMLlite/pull/2>`__.
- MUSIC_: Unfortunately MUSIC_ uses a private copy of rudeconfig_ that contains
  changes that have not yet been sent upstream. Bundling is `to be avoided
  <https://fedoraproject.org/wiki/Packaging:Guidelines#Bundling_and_Duplication_of_system_libraries>`__
  in Fedora for good reason, so I've filed a ticket `asking if the local
  changes to rudeconfig could be sent upstream
  <https://github.com/INCF/MUSIC/issues/56>`__. Until this is solved,
  MUSIC_ cannot be included in Fedora, unless a bundling exception is made.

The task list was moved to the `Pagure issue tracker
<https://pagure.io/neuro-sig/NeuroFedora/issues>`__.
I've done a bit of housekeeping so that we now use labels like the NEST_
initiative does, inspired by `this post
<https://medium.com/@dave_lunny/sane-github-labels-c5d2e6004b63#.ve6i7zcou>`__.
It really does make handling issues much easier.

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


.. _PyLEMS: https://src.fedoraproject.org/rpms/python-PyLEMS
.. _NeuroFedora: https://neuro.fedoraproject.org
.. _fsleyes: https://git.fmrib.ox.ac.uk/fsl/fsleyes
.. _NEST: https://github.com/nest/nest-simulator/wiki/issue-labeling-scheme
.. _MUSIC: https://github.com/INCF/MUSIC
.. _rudeconfig: https://github.com/mflood/rudeconfig
.. _NeuroMLlite: https://github.com/NeuroML/NeuroMLlite
