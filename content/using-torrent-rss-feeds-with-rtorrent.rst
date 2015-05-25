Using torrent RSS feeds with rtorrent
#####################################
:date: 2011-02-21 02:20
:author: ankur
:category: Tech
:tags: Linux
:slug: using-torrent-rss-feeds-with-rtorrent

I was going through the `rtorrent wiki`_ looking for what else I could
do with rtorrent. I love the client, and I really hate it when someone
says "$MyClient can do this, haven't seen rtorrent do it." One such
feature was using rtorrent with `RSS feeds`_ that you get from torrent
websites. There's this `ticket`_ which discusses this issue. As the
ticket mentions, `rssdler`_ is an amazing utility which helps accomplish
this. It took me a day to set it up to work with rtorrent, so I thought
I'd share it with you folks and save you some time. rtorrent now watches
a directory, which is also the destination folder that rssdler downloads
torrent files to.

I'm going to submit the rssdler package for review soon. For the time
being, you can install it locally in ~/bin and use it. I've placed the
.rtorrent.rc and ./rssdler/config.txt files to my `fedorapeople space`_
that you can download and easily customize.

Here are some additional docs that you can read up:

http://libtorrent.rakshasa.no/wiki

http://www.torrent-invites.com/seedboxes/25858-tutorial-rssdler-setup-config-rtorrent-user.html

http://code.google.com/p/rssdler/w/list

.. _rtorrent wiki: http://libtorrent.rakshasa.no/wiki
.. _RSS feeds: http://en.wikipedia.org/wiki/RSS
.. _ticket: http://libtorrent.rakshasa.no/ticket/987
.. _rssdler: http://code.google.com/p/rssdler/
.. _fedorapeople space: http://ankursinha.fedorapeople.org/rssdler/
