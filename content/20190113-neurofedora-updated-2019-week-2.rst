NeuroFedora updated: 2019 week 2
################################
:date: 2019-01-13 20:55:44
:author: ankur
:slug: neurofedora-update-2019-week-2
:category: Research
:tags: Community, Matlab, Computational neuroscience, Free software, Fedora, NeuroFedora, Planet
:summary: An update on NeuroFedora_ at the end of week 2 in 2019.


.. figure:: {static}/images/20181005-NeuroFedoraLogo01.png
    :alt: NeuroFedora logo
    :target: https://docs.fedoraproject.org/en-US/neurofedora/overview/
    :width: 30%
    :class: img-responsive

    `NeuroFedora logo by Terezahl from the Fedora Design Team <https://pagure.io/design/issue/602>`__


We had our first meeting of the year. The `full logs
<https://meetbot.fedoraproject.org/teams/neurofedora/neurofedora.2019-01-11-14.00.log.html>`__
from our meeting are available here on the `Fedora mote application
<https://meetbot.fedoraproject.org/>`__. I have pasted the minutes of the
meeting at the end for your convenience.

The meeting was broadly for the team to come together and discuss a few things.
We checked on the status of current tasks, and discussed our future steps.
We've got to work on our documentation, for example.  There's a lot to do, and
a lot of cool new things to learn---in science, computing, and community
development. If you'd like to get involved, please get in touch.

We're continuing our work on including software in NeuroFedora, since that's
the major chunk of our work load.

----

Meeting summary
---------------
Meeting started by FranciscoD at 14:00:15 UTC.

* Roll call  (FranciscoD, 14:00:43)
   * IRC meeting commands: https://fedoraproject.org/wiki/Meeting:Guide (FranciscoD, 14:01:56)

* Joining the team  (FranciscoD, 14:04:37)
   * We need package maintainers, testers, doc writers, users---> there are so
     many ways of getting involved  (FranciscoD, 14:05:30)
   * To help with packaging, please join the neuro-sig FAS group, and then log
     out and back in to src.fp.o once your membership is approved  (FranciscoD,
     14:05:49)
   * To join the group on pagure (where we maintain issues), please drop any of
     us a ping and we'll add you  (FranciscoD, 14:06:10)
   * Our channels: #fedora-neuro on IRC, https://t.me/NeuroFedora on Telegram,
     neuro-sig@lists.fp.o is our ML  (FranciscoD, 14:07:07)
   * https://pagure.io/neuro-sig/NeuroFedora -> housekeeping repo (FranciscoD, 14:07:57)
   * https://pagure.io/neuro-sig/documentation -> documentation repo (FranciscoD, 14:08:05)
   * Tickets:
     https://pagure.io/neuro-sig/NeuroFedora/issues?tags=S%3A+Next+meeting
     (FranciscoD, 14:11:56)
   * Additional agenda item: prioritise packages so we have some order in which
     to go about them  (FranciscoD, 14:12:36)
   * Poster at CNS: https://pagure.io/neuro-sig/NeuroFedora/issue/189
     (FranciscoD, 14:13:49)
   * Annual organisation for computational neuroscience conference is at
     Barcelona in July this year: https://www.cnsorg.org/cns-2019 (FranciscoD,
     14:14:18)
   * Everyone that contributes in any way will be a mentioned in the author
     list  (FranciscoD, 14:14:53)
   * https://pagure.io/neuro-sig/NeuroFedora/issue/188 -> Own neurofedora.org?
     (FranciscoD, 14:16:20)
   * AGREED: Use neuro.fp.o (+5, -0)  (FranciscoD, 14:18:28)
   * https://pagure.io/neuro-sig/NeuroFedora/issue/152 -> Organisational blog
     on neurofedora.github.io?  (FranciscoD, 14:19:08)
   * We do have a github organisation: https://github.com/neurofedora
     (FranciscoD, 14:19:26)
   * AGREED: FranciscoD publish updates on his blog for the time being.
     Organisational blog to be revisited in the future (+6, -0) (FranciscoD,
     14:26:45)
   * https://pagure.io/neuro-sig/NeuroFedora/issue/8 -> A web location for
     user-end troubleshooting?  (FranciscoD, 14:27:01)
   * https://neurostars.org/ -> NeuroStars generic troubleshooting form
     (FranciscoD, 14:29:51)
   * A list of neuroscience resources is here:
     https://docs.fedoraproject.org/en-US/neurofedora/related-links/
     (FranciscoD, 14:30:14)
   * A new FAS (better interface etc) is being planned, but there's no ETA of
     when it'll be ready for deployment  (FranciscoD, 14:33:55)
   * ACTION: FranciscoD update docs to request users to file bugs on pagure
     (FranciscoD, 14:35:34)
   * https://pagure.io/neuro-sig/NeuroFedora/issue/121 -> Add comps groups
     (FranciscoD, 14:35:46)
   * Neuron (without MPI/Python) is currently in review:
     https://bugzilla.redhat.com/show_bug.cgi?id=1662526  (FranciscoD,
     14:37:30)
   * Link to our suggestion form is here:
     https://docs.fedoraproject.org/en-US/neurofedora/overview/#_suggest_software_for_inclusion
     (FranciscoD, 14:39:06)
   * https://pagure.io/neuro-sig/NeuroFedora/issue/180 -> Docker images for
     NEST  (FranciscoD, 14:41:26)
   * ACTION: FranciscoD create new page for third party software resources in
     docs  (FranciscoD, 14:49:18)
   * ACTION: FranciscoD add https://flathub.org/apps/details/org.gnode.NixView
     to "third party sources list" on docs  (FranciscoD, 14:50:38)
   * LINK: https://github.com/G-Node/nix/   (gicmo, 14:53:20)
   * https://pagure.io/neuro-sig/NeuroFedora/issue/155 -> Including packages
     that need Matlab at runtime  (FranciscoD, 14:55:27)
   * Prioritise python over Matlab/Octave  (FranciscoD, 14:57:56)

* Open floor  (FranciscoD, 14:58:50)
   * ACTION: FranciscoD add a page "neuroscience resources for beginners"
     (FranciscoD, 15:03:56)
   * LINK: https://labs.fedoraproject.org/ -> I mean these  (FranciscoD,
     15:05:12)
   * ACTION: FranciscoD send out logs  (FranciscoD, 15:06:28)
   * ACTION: FranciscoD summarise meeting discussion in next blog post
     (FranciscoD, 15:06:38)
   * LoKoMurdoK and zbyszek are package maintainer sponsors  (FranciscoD,
     15:08:33)
   * Thanks gicmo pac23 zbyszek LoKoMurdoK blackfile mhough for coming, and
     helping out  (FranciscoD, 15:09:35)

Meeting ended at 15:10:43 UTC.

----

`NeuroFedora documentation
<https://docs.fedoraproject.org/en-US/neurofedora/overview/>`__ is available on
`the Fedora documentation website
<https://docs.fedoraproject.org/en-US/docs/>`__.  Feedback is always welcome.
You can get in touch with us `here
<https://docs.fedoraproject.org/en-US/neurofedora/overview/#_communicating_and_getting_help>`__.

.. _NeuroFedora: https://neuro.fedoraproject.org
