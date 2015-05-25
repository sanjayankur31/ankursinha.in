why fedora-tour won't be a Fedora 14 feature
############################################
:date: 2010-07-08 13:35
:author: ankur
:category: Tech
:tags: Fedora
:slug: why-fedora-tour-wont-be-a-fedora-14-feature

Frankly, we're working pretty slow. That's the reason, we're not going
to deny it at all. But YES, we do have valid reasons (excuses) for this.
I'll try to convince you that it isn't really our fault.

The `fedora-tour`_ project relies heavily on `clutter`_ and the graphics
support from our new free drivers. I run an Nvidia machine which runs
`nouveau`_ (dv6226tx HP Pavilion Laptop). On F-12, my code would run,
and show me the UI that I had created. On F-13, my code segfaults! So,
in short, I can't see what I just coded. Yes, I've filed a `bug`_.
Unfortunately, I'm using a laptop and pulling out the Nvidia graphics
card so it can fall back on its native on-board  graphics controller is
out of the question. At the moment, we are two \*active\* developers on
the fedora-tour team, `subfusc`_, and me (`FranciscoD`_), and somehow,
both of us are stuck with this bug. Sad, isn't it?

What now? Are we going to sit and sip on cold beer while waiting for
upstream to sort it out? Well, yes, in a way. Since the fedora-tour
needs 3D support and the rest (whatever clutter needs), we need to wait
for all the hardware/drivers to work properly. The fedora-tour needs to
work on all hardware, it is meant for \*all\* users. It needs to be
tested on all the hardware we can find so that the maximum possible
people can use it.

In spite of this, we're not happy sitting on our asses waiting. I have
an old run down machine back at home which uses an Nvidia card (crap!).
I intend to pull the card out so the on board Intel graphics (which will
not cause my code to segfault, hopefully) can take over. This machine, I
shall update to a decent working condition and ship to college (this
will need an additional task of cajoling dad for funds) and set up as a
minimal server where the fedora-tour team can set up accounts and test
their code. I'm going to get home on the 20th of this month and will set
up the server ASAP. It's a long shot, and does need quite a bit of luck
(what if pulling out the card doesn't work!!??) but it's almost the only
solution we've got.

.. _fedora-tour: http://fedorahosted.org/fedora-tour
.. _clutter: http://www.clutter-project.org/
.. _nouveau: http://nouveau.freedesktop.org/
.. _bug: https://bugzilla.redhat.com/show_bug.cgi?id=591771
.. _subfusc: https://fedoraproject.org/wiki/User:Subfusc
.. _FranciscoD: http://fedoraproject.org/wiki/AnkurSinha
