Setting up rygel on your Fedora system
######################################
:date: 2013-05-12 15:51
:author: ankur
:category: Tech
:tags: Fedora
:slug: setting-up-rygel-on-your-fedora-system

|rygel|

I've been trying to get **rygel** to work on my system. It's been
slightly difficult since it uses a dynamic port by default and you need
to open these ports each time you want to use a client over the network.
At the moment, the firewall-config GUI doesn't mention rygel in the
list, and the rygel docs don't tell you what ports you need to open.
There's a `bug with a patch filed`_, but I'm not really sure what's
going on with it. I got it to work today and here's how:

Install the required packages:

``[ankur@ankur-pc ~]$ sudo yum install rygel tumbler gupnp-av``

**Tumbler** is a dbus thumbnailer. If you don't install it, rygel gives
an error saying a dbus thumbnailer isn't available. It also gives an
error saying it couldn't find
**"/usr/share/gupnp-av/didl-lite-v2.xsd"**, and the
gupnp-av\ [STRIKEOUT:-devel] package provides this. I've got to look
into both these and see if they should be required by rygel by default.
Any way, moving on:

Copy the configuration file:

``[ankur@ankur-pc ~]$ cp /etc/rygel.conf ~/.config/rygel.conf``

Modify the config file. For example, I enabled the tracker plugin since
I'm on gnome3. An important change is to use a fixed port, so you always
know which one needs to be opened in your firewall. I randomly picked
65530. You can pick any that isn't already reserved.

| `` [ankur@ankur-pc ~]$ vim ~/.config/rygel.conf # Make modifications # The port to run HTTP server on. 0 means dynamic. port=65530 # Other modifications``
|  Open your firewall ports:

You need to open the UDP 1900 and the 65530 TCP port:

| ``[ankur@ankur-pc ~]$ sudo firewall-cmd --add-port=1900/udp sudo firewall-cmd --add-port=65530/tcp [ankur@ankur-pc ~]$ sudo firewall-cmd --list-ports 1900/udp 65530/tcp``
|  (or use the **firewall-config** GUI)

That should be enough. **Totem** will show it up in the sidebar. I
tested it with a wdtv box and my android phone too (There are many dlna
clients available in the play store).

|totem-rygel|

|Screenshot_2013-05-12-15-45-09|

I haven't been able to get VLC to use it though. I'll look into it
sometime later and see if I can diagnose it. Hope this helps!

EDIT: Packaging bug in gupnp-av fixed F19 onwards. -devel package no
longer required.

.. _bug with a patch filed: https://bugzilla.redhat.com/show_bug.cgi?id=626188

.. |rygel| image:: http://ankursinha.in/wp/wp-content/uploads/2013/05/rygel.png
   :target: http://ankursinha.in/wp/wp-content/uploads/2013/05/rygel.png
.. |totem-rygel| image:: http://ankursinha.in/wp/wp-content/uploads/2013/05/totem-rygel-300x298.png
   :target: http://ankursinha.in/wp/wp-content/uploads/2013/05/totem-rygel.png
.. |Screenshot_2013-05-12-15-45-09| image:: http://ankursinha.in/wp/wp-content/uploads/2013/05/Screenshot_2013-05-12-15-45-09-168x300.png
   :target: http://ankursinha.in/wp/wp-content/uploads/2013/05/Screenshot_2013-05-12-15-45-09.png
