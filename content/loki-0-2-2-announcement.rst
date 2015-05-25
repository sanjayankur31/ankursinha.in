loki-0.2.2 announcement
#######################
:date: 2010-06-29 23:57
:author: ankur
:category: Tech
:tags: Fedora
:slug: loki-0-2-2-announcement

`I recently announced the availability of loki-0.1.1`_, the first
release. I've added the notification bubble to it, and made the
Autotools etc adhere more to the conventions/standards. I've also set up
a temporary yum repo for F13 so you folks can try it out! The repo file
is `here`_ (That's legal and allowed , right??) . I would still call it
a BETA release since there is a lot on the TODO list. I hope to see the
TODO list expand as more people try it out and provide me with
suggestions, feedback. The sources are also present at
http://ankursinha.fedorapeople.org/loki_f13/loki_sources/ . I've tried
to keep the source as well documented as possible (it's FULL of
comments, probably enough to irritate a fellow developer who glances
through it :P ) , so folks that want a quick reference to libcurl,
libnotify, libconfig can use the source as a quick tutorial too.

Once you've yum installed loki, you need to run it as "loki &". Creating
a launcher on the "Application Menu" is on the TODO list, so is devising
an exit mechanism and an icon for the app and ..... As of now, it checks
once every 24hours. Making that user configurable is ALSO on the TODO
list. (The TODO list is getting kinda lengthy already!!)

Here's a screenshot. (please click to view)

|image0|

I'm not submitting it for a review yet. There are a couple of reasons to
that:

#. There will probably be a **name change**, which will require a source
   revamp, since all my variables and functions have a "loki" prefix.
#. It still lacks an **exit mechanism**, so once it starts, you gotta
   kill it to stop it.
#. I intend to add a small util to make it easier for users to configure
   their comics and the rest.

In short, I don't think it's reached the standard of an app that I would
expect fedora to feature. I will get down to these points, and the rest
of my TODO list whenever I can find the time. In the mean while, Have
fun!

***Bugs if any,RFEs, feedback, anything else you'd want to say, should
be directed to ankursinha AT fp.o (I can't afford a bugzilla yet ;) )***

.. _I recently announced the availability of loki-0.1.1: http://dodoincfedora.wordpress.com/2010/06/20/loki-0-1-1-release-announcement/
.. _here: http://ankursinha.fedorapeople.org/loki_f13/loki.repo

.. |image0| image:: http://dodoincfedora.files.wordpress.com/2010/06/screenshot.png?w=150
   :target: http://dodoincfedora.files.wordpress.com/2010/06/screenshot.png
