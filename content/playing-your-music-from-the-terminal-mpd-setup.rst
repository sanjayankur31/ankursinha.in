Playing your music from the terminal : mpd setup
################################################
:date: 2011-02-26 15:06
:author: ankur
:category: Tech
:tags: Linux
:slug: playing-your-music-from-the-terminal-mpd-setup

I love using the terminal. In my `last post`_, I detailed using rtorrent
+ RSS feeds + queue management. I've already posted a `how-to for
irssi`_ sometime back. Today I'm going to blog on setting up mpd and
ncmpc, a mpd client.

First, install the packages:

``$ su -c 'yum -y install mpd ncmpc'``

Alright, let's set up mpd now.

Create a ~/.mpd directory and copy the /etc/mpd.conf to your ~/.mpd
directory. We'll customize this sample file to our needs.

``$ mkdir ~/.mpd && cp /etc/mpd.conf ~/.mpd/mpd.conf``

The file is very well commented. Read the comments and edit the values
to suit your set up. You need to uncomment the "pulse" section to make
mpd use pulseaudio. This is a must.

That's pretty much it for mpd. Save the file, and start mpd.

``$ mpd &``

Now that you have mpd running, you need to install a client. A quick yum
search will tell you that there are quite a few. I'm going to use ncmpc.

Create a ~/.ncmpc directory and copy the /etc/ncmpc/config to it.

``$ mkdir ~/.ncmpc && cp /etc/ncmpc/config ~/.ncmpc/config ;``

Again, the file is very well commented. Customize if to your needs. I,
personally, just enable colours and a few other options.

That's it! Run ncmpc in a terminal, press "1" to see the controls, and
play away!

I've found an audio scrobbler for mpd too, but it isn't quite working
with last.fm yet. An update would fix that from what I gathered off
google. Once it begins to work, I'll post on how to set it up. I'm going
looking for a plugin that sends the "now playing info" to messengers
such as Pidgin and Empathy.

Added reading : http://mpd.wikia.com/wiki/Clients

.. _last post: http://dodoincfedora.wordpress.com/2011/02/23/a-complete-rtorrent-setup/
.. _how-to for irssi: http://dodoincfedora.wordpress.com/2010/12/05/setting-up-irssi-on-fedora/
