If the recent upgrade "wiped" your accounts from Empathy
########################################################
:date: 2010-07-21 19:48
:author: ankur
:category: Tech
:tags: Fedora
:slug: if-the-recent-upgrade-wiped-your-accounts-from-empathy

The recent upgrade caused my Empathy client to somehow forget the
accounts that I had configured. (The
~/.mission-control/accounts/accounts.cfg file is intact). A quick post
to the devel list, here is what you need to do to get it working again:

::

    chcon -t bin_t /usr/libexec/mission-control*  /usr/libexec/telepathy*

That's a workaround for the time being. The `bug`_ should be fixed
quickly.

.. _bug: https://bugzilla.redhat.com/show_bug.cgi?id=616506
