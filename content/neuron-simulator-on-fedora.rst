NEURON simulator on Fedora
##########################
:date: 2014-02-18 07:58
:author: ankur
:category: Tech
:tags: Fedora
:slug: neuron-simulator-on-fedora

I've been meaning to package up NEURON for Fedora for a while now. From
the `NEURON website`_:

***What is NEURON?***

NEURON

-  is a flexible and powerful simulator of neurons and networks
-  has important advantages over general-purpose simulators
-  helps users focus on important biological issues rather than purely
   computational concerns
-  has a convenient user interface
-  has a user-extendable library of biophysical mechanisms
-  has many enhancements for efficient network modeling
-  offers customizable initialization and simulation flow control
-  is widely used in neuroscience research by experimentalists and
   theoreticians
-  is well-documented and actively supported
-  is free, open source, and runs on (almost) everything

 

It's quite an old piece of software. It took me a while to hack rpms out
of the source code. The rpms probably won't make it through a Fedora
review in their current state, so I've put up a copr repository instead:
http://copr.fedoraproject.org/coprs/ankursinha/NEURON/

The builds work, as the screenshot below will show. I'm still new at
NEURON myself, so it'll be a few weeks before I'll have all the
functionality tested out. There are tutorials strewn over the interwebs,
please just search for them yourselves.

[caption id="attachment\_1532" align="aligncenter" width="625"]\ |NEURON
in action| NEURON in action[/caption]

If you're a computational neuroscientist using Fedora, this is a little
bit of good news for you! Cheers!

.. _NEURON website: http://www.neuron.yale.edu/neuron/what_is_neuron

.. |NEURON in action| image:: http://ankursinha.in/wp/wp-content/uploads/2014/02/NEURON-screenshot-1024x575.png
   :target: http://ankursinha.in/wp/wp-content/uploads/2014/02/NEURON-screenshot.png
