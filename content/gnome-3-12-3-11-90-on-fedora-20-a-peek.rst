Gnome 3.12 (3.11.90) on Fedora 20: A peek!
##########################################
:date: 2014-02-21 05:31
:author: ankur
:category: Tech
:tags: Fedora
:slug: gnome-3-12-3-11-90-on-fedora-20-a-peek

Updating and testing
--------------------

So, the Fedora Desktop SIG have been `discussing how Gnome 3.12 should
be made available to Fedora users`_. Generally, `Fedora discourages
major updates to packages`_. The ideal scenario would be if Fedora 21
and Gnome 3.12 released close to each other, but it isn't going to
happen this time. As a result, there's talk of provide Gnome 3.12 as an
update in Fedora 20. `The initial builds have been put on COPR for
volunteers to test`_. I took the leap today, with two of my machines.
The upgrade was quite easy, and didn't require a lot of manual
intervention. The one issue you may run into would be multilib errors
since the COPR repositories do not provide multilib packages (an x86\_64
COPR repo will not contain any i686 packages at all.). So, if you're on
an x86\_64 system and have some i686 packages that also need to be
updated as part of Gnome 3.12, you'll run into errors with both dnf and
yum.

For example, this is what I ran into with yum:

``> Error: Protected multilib versions: libwayland-server-1.4.0-1.fc20.x86_64 != libwayland-server-1.2.0-3.fc20.i686 > Error: Protected multilib versions: libwayland-client-1.4.0-1.fc20.x86_64 != libwayland-client-1.2.0-3.fc20.i686 > Error: Protected multilib versions: vala-0.23.3-1.fc20.x86_64 != vala-0.22.1-1.fc20.i686 > Error: Protected multilib versions: glib2-2.39.90-1.fc20.x86_64 != glib2-2.38.2-2.fc20.i686 > Error: Protected multilib versions: gdk-pixbuf2-2.30.5-1.fc20.x86_64 != gdk-pixbuf2-2.30.3-1.fc20.i686 > Error: Protected multilib versions: pango-1.36.2-1.fc20.x86_64 != pango-1.36.1-2.fc20.i686``

DNF doesn't provide proper error reports at the moment. I got this
unhelpful message when using the ``--best`` flag:

`` > Error: cannot install both gdk-pixbuf2-2.30.5-1.fc20.x86_64 and > gdk-pixbuf2-2.30.3-1.fc20.x86_64. cannot install both > glib2-2.39.90-1.fc20.x86_64 and glib2-2.38.2-2.fc20.x86_64. cannot > install both libwayland-client-1.4.0-1.fc20.x86_64 and > libwayland-client-1.2.0-3.fc20.x86_64. cannot install both > libwayland-server-1.4.0-1.fc20.x86_64 and > libwayland-server-1.2.0-3.fc20.x86_64. cannot install both > pango-1.36.2-1.fc20.x86_64 and pango-1.36.1-2.fc20.x86_64. cannot > install both vala-0.23.3-1.fc20.x86_64 and vala-0.22.1-1.fc20.x86_64``

The solution is quite simply to manually grab these i686 packages from
the COPR repo and update them before running the complete Gnome 3.12
update.

Once the update is done, you log out and back in, and you have a new
Gnome version to play with. First things you notice: **broken
extensions**.

|Installed extensions|

Upstreams will slowly begin to update their extensions as 3.12 gets
closer to release, but it's always good to test extensions and let
upstreams know if they're working or not. In a vanilla install, no
extensions will work, since the version string in their sources only
specifies that they work with Gnome 3.10. Gnome devs, quite
intelligently, provide a hidden option that gets the system to skip this
version check:

`` # gsettings set org.gnome.shell disable-extension-version-validation true ``

**Please only use this if you're testing extensions. It isn't meant to
be enabled for daily use. It's for debugging purposes only.**

Some of my extensions work just fine, others don't. I've filed issues
upstream for `caffeine`_, `hamster-time-tracker-extension`_ and the
`MPRIS2 extension`_. If you're using extensions, please let the
upstreams know if they don't work with 3.11.90. That way, they'll have
time to update their extensions before 3.12 is formally released.

So, what's new?
---------------

Quite a few things, really. The complete release notes are `here`_. I
noticed the gnome-software update. It now lets you rate your
applications. There's even a shell search provider for software (Please
excuse the large image, I was on my dual monitor set up at the time)

|Gnome-software 3.12|

|Gnome-software search provider|

Another update is gedit. It's been ported over to GTK3 received major UI
update and fits in better with the environment now (I was already using
GTK3 as pointed out in the comments):

|Gedit new|

There are quite a few other changes too, like the Wayland support. I
haven't checked them all out yet.

You can help!
-------------

Well, of course you can! I'll advise setting up a test vm and not using
your work machine for this, just in case. Update, test, file bugs at
relevant places and help make Gnome 3.12 a better experience for Fedora
users, and all users in general! Cheers!

.. _discussing how Gnome 3.12 should be made available to Fedora users: https://lists.fedoraproject.org/pipermail/desktop/2014-January/
.. _Fedora discourages major updates to packages: http://fedoraproject.org/wiki/Updates_Policy
.. _The initial builds have been put on COPR for volunteers to test: http://copr.fedoraproject.org/coprs/rhughes/f20-gnome-3-12/
.. _caffeine: https://github.com/eonpatapon/gnome-shell-extension-caffeine/issues/24
.. _hamster-time-tracker-extension: https://github.com/projecthamster/shell-extension/issues/65
.. _MPRIS2 extension: https://github.com/eonpatapon/gnome-shell-extensions-mediaplayer/issues/153
.. _here: https://wiki.gnome.org/ThreePointEleven/Features/

.. |Installed extensions| image:: http://ankursinha.in/wp/wp-content/uploads/2014/02/extensions-3.12-1024x546.png
   :target: http://ankursinha.in/wp/wp-content/uploads/2014/02/extensions-3.12.png
.. |Gnome-software 3.12| image:: http://ankursinha.in/wp/wp-content/uploads/2014/02/gnome-software-updated-3.12-1024x575.png
   :target: http://ankursinha.in/wp/wp-content/uploads/2014/02/gnome-software-updated-3.12.png
.. |Gnome-software search provider| image:: http://ankursinha.in/wp/wp-content/uploads/2014/02/gnome-software-search-provider-857x1024.png
   :target: http://ankursinha.in/wp/wp-content/uploads/2014/02/gnome-software-search-provider.png
.. |Gedit new| image:: http://ankursinha.in/wp/wp-content/uploads/2014/02/gedit-new-1024x744.png
   :target: http://ankursinha.in/wp/wp-content/uploads/2014/02/gedit-new.png
