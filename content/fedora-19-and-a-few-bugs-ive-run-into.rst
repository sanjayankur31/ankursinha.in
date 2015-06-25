Fedora 19 and a few bugs I've run into
######################################
:date: 2013-05-02 19:27
:author: ankur
:category: Tech
:tags: Fedora
:slug: fedora-19-and-a-few-bugs-ive-run-into

|Fedora 19 alpha banner|

I generally only update once beta is released. This time however, I
really wanted to play with `GNOME3.8`_ and well, "accepted my fate" as
anaconda puts it. Fedora 19 is pretty stable for me already. I did a
fresh install. Anaconda worked well. The first glitch was both anaconda
and `gnome-initial-setup`_\ wanting to set up users. `A bug and its fix
are already on the way`_. Gnome3's new "welcome to gnome" application is
also pretty good. It ensures that new users know what they can do with
the desktop. It also tries to shift people to the new way the desktop is
to be used, since people trying to use it as GNOME2.X really have a very
difficult time with it.

The first major bug I ran into came with an X update. `1.14.0-6 broke X
for me completely`_.. It got pushed to stable in spite of my negative
karma since it appears to work OK for others.

The next bug I thought I had hit was suspend/hibernate not working. The
system would hibernate/suspend just right, but wouldn't resume from the
state. It would start as if it had been powered off. I found `this wiki
page`_ and adding the "resume=/dev/where/swap/is" does seem to fix it
for me. I'm not certain if this is required, but no harm having it in
the grub command line. So far so good. When it did finally resume, X
started failing again. X doesn't resume with the system. A new X starts,
killing whatever apps were running, bringing up GDM, as if I were never
logged in. My screen instance is the only application that survives,
since it only gets detached when it's terminal is killed. It's how I
figured out what was happening. `I filed a bug for this already too`_.
There's a patch upstream already which seems to fix it, so it's only a
matter of time.

A bug that really kills my usability is to do with gnome-online-accounts
and evolution. I use gmail with goa for my mail, along with Microsoft
Exchange for university mail. GOA doesn't seem to like exchange. It
crashes repeatedly. `Abrt filed a bug for me here`_. I shifted to using
IMAP instead of exchange and it works well now. However, I couldn't set
up this IMAP using GOA since GOA only seems to support the "PLAIN"
authentication method for SMTP servers. The university's system requires
a "LOGIN" authentication method. `A bug for this is also filed here`_.
While this is easy to work around, a really annoying bug is that
evolution forgets all it's settings every time GOA crashes. So, all the
settings I make to my accounts, such as security, signatures for
accounts, reply to, subscription settings are lost each time GOA
crashes. With exchange it was crashing frequently and made me set up
evolution again and again. It seems to be an issue with signals that GOA
uses and how clients use these signals. `The bug is here`_, it's already
filed upstream and a fix is pushed to evolution 3.8.2 which we'll see in
a week or two.

I can't remember any other big bugs that need squashing. `Bijiben is up
for review`_. I made an rpm and am using it now, instead of Gnotes. I do
like the simple layout that Bijiben has. I used to manually spread out
my Gnotes on a work space, and I don't have to do it with Bijiben
anymore. It's still an application in its infancy and a lot of features
are still in queue.

If you have the time, switch to F19 now and help test it out. The more
testing it gets, the better it will be at release!

.. _GNOME3.8: http://fedoraproject.org/wiki/Features/Gnome3.8
.. _gnome-initial-setup: https://live.gnome.org/ThreePointFive/Features/InitialSetup
.. _A bug and its fix are already on the way: https://bugzilla.redhat.com/show_bug.cgi?id=929289
.. _1.14.0-6 broke X for me completely: https://bugzilla.redhat.com/show_bug.cgi?id=955400
.. _this wiki page: https://wiki.archlinux.org/index.php/Pm-utils#Editing_GRUB2.27s_defaults
.. _I filed a bug for this already too: https://bugzilla.redhat.com/show_bug.cgi?id=958611
.. _Abrt filed a bug for me here: https://bugzilla.redhat.com/show_bug.cgi?id=958336
.. _A bug for this is also filed here: https://bugzilla.redhat.com/show_bug.cgi?id=958338
.. _The bug is here: https://bugzilla.redhat.com/show_bug.cgi?id=956908
.. _Bijiben is up for review: https://bugzilla.redhat.com/show_bug.cgi?id=919265

.. |Fedora 19 alpha banner| image:: https://fedoraproject.org/w/uploads/5/55/Banners_cat_alpha.png
   :target: http://fedoraproject.org/get-prerelease
