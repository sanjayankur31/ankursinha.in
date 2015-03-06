A complete rtorrent setup
#########################
:date: 2011-02-23 14:31
:author: ankur
:category: Tech
:tags: Fedora
:slug: a-complete-rtorrent-setup

I wrote a  `blog post`_ recently which gave an overview of how you can
use **RSS feeds** with **rtorrent**. Since I was working on this, I
decided to look up **queue management** in rtorrent too. rtorrent does
not provide queue management iby itself at the moment. I found an `RFE`_
which has been open for quite a while.

Google is your friend, and yet again, it gave me the answers. In this
post, I'm going to detail a **complete** rtorrent setup.

Install rtorrent
----------------

``$ yum install rtorrent -y``

Make a ~/bin/ directory
-----------------------

$ mkdir ~/bin

This is needed to keep a user copy of the torrent queue script and
rssdler for the time being (which I hope to hack and submit for review
soon). Please check if ~/bin is in your path or not. It should be there
by default.

Make required directories
-------------------------

This is based on my setup, but you can edit it as you want once you get
a hang of things.

``$ mkdir -p ~/Downloads/torrents/rtorrent_watch ~/Downloads/torrents/rtorrent_completed ~/Downloads/torrents/rtorrent_loading ~/Downloads/torrents/rtorrent_sessions ~/Downloads/torrents/rtorrent_temp/``

There are 5 directories above:

#. completed : directory that completed torrent files will be moved to
#. temp : currently downloading torrent files are stored here
#. watch : a watch directory. You place a .torrent in here, and rtorrent
   automagically loads it (moves it to watchdir after checking queue
   status)
#. loading : the queue manager uses this directory to keep torrent
   files. This is also the directory we'll get rssdler to download our
   torrent files to.
#. sessions : rtorrent session files will be stored here. You can now
   close rtorrent and resume it later without losing any data.

The rtorrent.rc file

Download my `rtorrent.rc`_ file. Place it as ".rtorrent.rc" in ~
(~/.rtorrent.rc). Don't miss the prefix DOT.

I've commented the file, so you can edit it as you like. For more info
look up the rtorrent wiki. Make sure the directories match the ones you
created above!

The rssdler setup
-----------------

`Download rssdler`_, copy the rssdler.py file to ~/bin/

``$ cp /path/to/rssdler.py ~/bin/rssdler && chmod a+x ~/bin/rssdler``

Download my rssdler `config`_ file. It needs to be placed as
~/.rssdler/config.txt The file is also commented since it's just an
edited version of the sample one. Edit it as you like.

The rtorrentqueuemanager.py setup
---------------------------------

Download the `source`_. Open the rtorrentqueuemanager.py file in your
favourite text editor and make necessary changes to the directories at
the beginning of the file. You will notice it needs a
"max\_downloads\_file". You can place this anywhere you want, I've
placed it in my Downloads/torrent/ directory.

``echo "2" > ~/Downloads/torrents/max_downloads.txt``

Again, make sure that the value you give in the file is what you name
the file as etc. If you aren't careful about this, the setup won't work.
Place the python script in ~/bin/ and make it executable

``cp rtorrentqueuemanager.py ~/bin/ && chmod a+x ~/bin/rtorrentqueuemanager.py``

Alright, we're mostly set.
If you want the two scripts to run at login, under GNOME head to
System>prefs>startup applications and add them there. Add rssdler as
"rssdler -d" (daemon mode) and rtorrentqueuemanager.py as "python
rtorrentqueuemanager.py &"

Log out, log back in. Check if rssdler is running : "rssdler -s". You
can list the downloaded files with "rssdler --list-saved".
These files will be downloaded into the loading\_dir. When the
queuemanager sees less that max\_download files in the watch dir, it
moves a new one to it, thus implementing queue management. Cool ha!?

I think I've included most of what needs to be done. If you have
queries/run into trouble, please ask.

.. _blog post: http://ankursinha.in/2011/02/21/using-torrent-rss-feeds-with-rtorrent/
.. _RFE: http://libtorrent.rakshasa.no/ticket/13
.. _rtorrent.rc: http://ankursinha.fedorapeople.org/misc/rtorrentconf/rtorrent.rc
.. _Download rssdler: http://code.google.com/p/rssdler/
.. _config: http://ankursinha.fedorapeople.org/misc/rtorrentconf/config.txt
.. _source: http://www.stabellini.net/rtorrent-howto.txt
