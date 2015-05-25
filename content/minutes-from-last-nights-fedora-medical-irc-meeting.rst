Minutes from last night's Fedora Medical IRC meeting
####################################################
:date: 2013-09-04 09:23
:author: ankur
:category: Tech
:tags: Fedora
:slug: minutes-from-last-nights-fedora-medical-irc-meeting

Summary
-------

The meeting last night was a really good one. We got quite a few details
sorted. We're finally moving towards creating a live image that we can
give out to folks to try and give us feedback on.

The links that zodbot generated for us are:

`HTML Logs`_

`HTML minutes`_

`Text log`_

`Text minutes`_

I stupidly used #task instead of #action, and therefore the minutes have
no action items at all. I'll put the action items below:

Action items: work to be done
-----------------------------

#. **FranciscoD** update fedora medical trac tickets to reflect current
   state of packages
#. **sjodogne** open ticket for 3D slicer
#. **FranciscoD** open a trac ticket also, so that folks who didn't make
   it to the meeting can comment and make suggestions
#. **mrceresa** package and start review of seg3d2
#. **mrceresa** file new trac ticket for seg3d2
#. **FranciscoD** get in touch with design team spin wrangler and
   request a post on how the spin is made
#. **sebp SSlater sjodogne FranciscoD** : catch hold of any new
   volunteers who'd like to help and get them started

Plans in a nutshell
-------------------

We've already packaged up most of the software that is required for the
creation of a spin. The one issue is that we have multiple use cases. At
the meeting, we identified two:

#. Medical practitioners
#. Researchers

Please read the logs for complete details on this classification.

The idea currently is to package up the higher priority packages and
make two unofficial spins. We'll then use these unofficial spins to
collect feedback and further improve our package set. The improved
package set will then be proposed as an official Fedora Medical spin.
It's still a far way off, but it's good to at least get started on it.

We need more help!
------------------

Here are areas that you can help us out in:

#. **Package maintainers**: we need quite a few more package maintainers
   who can help us maintain all this software in Fedora. If you're not
   yet a package maintainer, `you can start by co-maintaining a
   package`_. Just `drop us an email`_ and we'll help you get started.
#. **Spin wrangler**: sebp and sslater are already looking into this,
   but we can always use a few more hands here. This entails creating a
   fedora spin and testing that it boots etc. just fine. I'm going to
   get in touch with the Spins SIG and see if we can just use the fedora
   system to generate these for us too, so the work here would probably
   not be very complex. I just don't want to start it myself since I
   might not have cycles to keep up with it
#. **Testers**: Folks that just download and see if the software on
   these spins actually work and give us valuable feedback
#. **Trac wrangler**: Just someone who'll keep an eye on the trac,
   update milestones etc. and keep everyone on their toes about tickets!

We'll try and keep working on the spins now. Join us if you have the
cycles! Cheers!

**EDIT: I hang around in #fedora-medical on Freenode. Ping me if you
have something to talk about!**

.. _HTML Logs: http://meetbot.fedoraproject.org/fedora-meeting/2013-09-03/fedora_medical_2013-09-03.2013-09-03-12.03.log.html
.. _HTML minutes: http://meetbot.fedoraproject.org/fedora-meeting/2013-09-03/fedora_medical_2013-09-03.2013-09-03-12.03.html
.. _Text log: http://meetbot.fedoraproject.org/fedora-meeting/2013-09-03/fedora_medical_2013-09-03.2013-09-03-12.03.log.txt
.. _Text minutes: http://meetbot.fedoraproject.org/fedora-meeting/2013-09-03/fedora_medical_2013-09-03.2013-09-03-12.03.txt
.. _you can start by co-maintaining a package: https://fedoraproject.org/wiki/How_to_get_sponsored_into_the_packager_group#Become_a_co-maintainer
.. _drop us an email: https://lists.fedorahosted.org/mailman/listinfo/medical-sig
