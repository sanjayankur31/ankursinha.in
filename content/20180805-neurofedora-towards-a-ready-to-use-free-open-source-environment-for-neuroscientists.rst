NeuroFedora: towards a ready to use Free/Open source environment for neuroscientists
####################################################################################
:date: 2018-10-06 00:19:32
:author: ankur
:category: Research
:tags: Community, Computational neuroscience, Fedora, Free software, Linux, NEST, Neuron, Numpy, Pandas, Planet, Python, Reproducible research, Sumatra, TeX, NeuroFedora
:slug: neurofedora-towards-a-ready-to-use-free-open-source-environment-for-neuroscientists
:summary: I have recently resurrected the `NeuroFedora SIG`_. We aim to make
          Fedora_ a ready to use platform for neuroscientists, so that they can
          focus on the science. Read on to learn more!


.. figure:: {static}/images/20181005-NeuroFedoraLogo01.png
    :alt: NeuroFedora logo!
    :target: {static}/images/20181005-NeuroFedoraLogo01.png
    :width: 30%
    :class: text-center img-responsive pagination-centered

    `NeuroFedora logo by Terezahl from the Fedora Design Team <https://pagure.io/design/issue/602>`__


I've recently resurrected the `NeuroFedora SIG`_. Many thanks to `Igor
<https://fedoraproject.org/wiki/User:Ignatenkobrain>`__ and the others who had
worked on it in the past and have given us a firm base to build on.

The goal
---------

The (current) goal of the `NeuroFedora SIG`_ is to make Fedora an easy to use
platform for neuroscientists. We aim to do this by making commonly used
Neuroscience software easily installable on a Fedora_ system.

Neuroscience is an extremely multidisciplinary field. It brings together
mathematicians, chemists, biologists, physicists, psychologists, engineers
(electrical and others), computer scientists and more. A lot of software is used
nowadays in Neuroscience for:

- data collection, analysis, and sharing
- lots of image processing (a lot of ML is used here, think Data Science)
- simulation of brain networks (NEURON_, Nest_, Moose_, PyNN_, Brian_)
- dissemination of scientific results (peer reviewed and otherwise, think
  LaTeX_)

Given that a large proportion of neuroscientists are not trained in
computer science, a lot of time and effort is spent setting up systems,
installing software (often building whole `dependency chains
<https://en.wikipedia.org/wiki/Dependency_hell>`__ from source). This can be
hard for people not well-versed in build systems and so on.

So, at NeuroFedora_, we will provide a ready to use Fedora_ based system for
neuroscientists to work with, so they can quickly get their environment set up
and work on the science.

Why Fedora?
-----------

For one, I have been a `contributor
<https://fedoraproject.org/wiki/User:Ankursinha>`__ for a while and know the
`community and the infrastructure <https://apps.fedoraproject.org/>`__ quite
well. That applies to me and others from the Fedora_ community that may work on
this and not the research community in general.

Technically, there are many advantages of using Fedora_ as a base.
Fedora is closely linked to the `Red Hat Enterprise Linux
<https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux>`__
eco system---which `Cent OS <https://www.centos.org/>`__ is a part of and
`Scientific Linux is <https://www.scientificlinux.org/about/>`__ is based on
too (Recently, `CoreOS also joined the Red Hat family
<https://coreos.com/>`__). RPM based systems are commonly deployed in
supercomputers and clusters. So, making this software available on Fedora_ also
makes it simpler to make it available on these systems.  Additionally, the
Fedora_ community is promoting Flatpaks_, and working to permit multiple
versions of software via the modularity_ system. Fedora_ also supports Docker_
very `well <https://fedoraproject.org/wiki/Docker>`__.


Join us!
--------

Packaging software is only *one* way in which one can contribute.  Writing docs
and answering questions about the software in NeuroFedora_ are other ways too,
for example.  If you are interested in neuroscience and in promoting `Open
Science <https://en.wikipedia.org/wiki/Open_science>`__, please consider
joining the SIG. You can get in touch with us via one of our many
`communication channels
<https://fedoraproject.org/wiki/SIGs/NeuroFedora#Communication_and_getting_help>`__.

This invitation extends to all--undergraduates, post-graduates, trainee
researchers (PhD candidates like me), professional researchers, hobbyists, and
everyone else.  If you work in the field already, it is a great way of
supporting the research community. For others, it is a great place to
learn about neuroscience, and  `Free Software
<https://www.fsf.org/blogs/community/user-liberation-watch-and-share-our-new-video>`__
and the various technical skills that go into developing software.

Current status
--------------

We track the software we are working on `here
<https://fedoraproject.org/wiki/SIGs/NeuroFedora/PackageSet>`__. A lot of
software is now ready to use in Fedora. This includes various Python libraries
and simulators such as Nest_ and Moose_. Neuron_, Brian_, and PyNN_ are all in
the pipeline. All of `TeX Live <http://tug.org/texlive/>`__ is also available in
Fedora_. If there is other Free/Open source software that you use which isn't
on our list, please let us know.  If you can help maintain it with us, that'll
be even better.

Fedora/Free software and Science
--------------------------------

Open science shares the `philosophy of FOSS
<https://www.gnu.org/philosophy/>`__. The data, the tools, the results, should
be accessible to all to understand, use, learn from, and develop. More and more
researchers are making it a point to keep Science as open as possible whether
it is to do with the `tools  <http://opensourceforneuroscience.org/>`__ or
`dissemination <https://en.wikipedia.org/wiki/Open_access>`__ of their
findings. NeuroFedora_ hopes to aid this movement. Come, join us!


.. _Fedora: https://getfedora.org
.. _NeuroFedora SIG: https://fedoraproject.org/wiki/SIGs/NeuroFedora
.. _NeuroFedora: https://neuro.fedoraproject.org
.. _Neuron: https://neuron.yale.edu/neuron/
.. _Nest: https://nest-simulator.org
.. _LaTeX: http://tug.org/
.. _PyNN: https://github.com/NeuralEnsemble/PyNN
.. _Moose: https://github.com/BhallaLab/moose
.. _Brian: http://briansimulator.org/
.. _Flatpaks: https://flatpak.org/
.. _modularity: https://docs.fedoraproject.org/en-US/modularity/
.. _Docker: https://www.docker.com/
