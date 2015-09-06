Copr repository for neuroscience related packages
#################################################
:date: 2015-09-06 19:50:46
:author: ankur
:category: Research
:tags: Computational neuroscience, Fedora
:slug: copr-repository-for-neuroscience-related-packages
:summary: I now maintain a COPR repository where I host neuroscience related packages that Fedora users can use. These packages will be submitted for review to Fedora when I have time in the future.

Just a quick quick post to announce that I've set up `a COPR repository where I host software used in neuroscience research`_. At the moment, the repository contains just a few packages:

#. Neuron_
#. Brian_

I'm working on XPPAUT_ now and should have that up soon and then I plan to work on NEST_ and PyNN_. If there are other applications you'd like packaged for Fedora, please `drop me an e-mail`_ and I'll put them up.

Of course, to install the packages, all you need to do is:

.. code:: bash

    $ sudo dnf copr enable ankursinha/neuroscience-research
    $ sudo dnf install nrn # to install NEURON


In the long term, the idea is to have all these packages in the Fedora repositories and then have a new shiny neuroscience spin! Of course, if you'd like to help, please drop me a mail too!

.. _a COPR repository where I host software used in neuroscience research: https://copr.fedoraproject.org/coprs/ankursinha/neuroscience-research/
.. _Neuron: https://www.neuron.yale.edu/neuron/
.. _Brian: https://pypi.python.org/pypi/Brian2
.. _XPPAUT: http://www.math.pitt.edu/~bard/xpp/xpp.html
.. _NEST: http://www.nest-simulator.org/
.. _PyNN: http://neuralensemble.org/PyNN/
.. _drop me an e-mail: mailto:ankursinha@fedoraproject.org


