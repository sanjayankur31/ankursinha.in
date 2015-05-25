Counterstrike : Condition Zero on Fedora !
##########################################
:date: 2011-05-21 21:10
:author: ankur
:category: Tech
:tags: Fedora
:slug: counterstrike-condition-zero-on-fedora

It's been a really really long time since I played on my system last.
Actually, it's been a very long time since I played a PC game at all. I
used to be an avid gamer a few years back, and Counterstrike and Age of
Empires were my favourites.

I found my old CS:CZ disk two or three days back, and I couldn't help
wanting to play again :D

It took me a while to google up and get it all working and I'm going to
spew it out here for everyone else.

-  Go find your counterstrike CD!
-  Install wine (refer:
   http://forums.fedoraforum.org/showthread.php?t=263150):

   ::

        su -c ' yum install wine.i686 --enablerepo=u*g'

-  Install the gecko engine thing it asks you to. (I don't know if it's
   needed, but no harm installing it eh?)
-  Install counterstrike from the CD (run the setup.exe using wine)
-  Once finished, you might not view some text in the game. This is
   because of missing mscore fonts. Get the setup files from the
   Internet. There are a lot of sites, `such as this`_, which still have
   these fonts. Install them by running the exe files with wine.
-  Once done, run the game. It \*should\* run.
-  If you choose to play a custom game, it might get stuck. This would
   be because it wants to load some HTML docs or something. A work
   around is to get rid of the "**motd\_temp.html**\ " and
   "**motd.txt**\ "files. You'll find these files in the
   "**/home/user/.wine/drive\_c/Valve/Condition Zero/**\ " directory.
   (Refer: http://appdb.winehq.org/objectManager.php?sClass=version&iId=8032&iTestingId=12149 )
-  Run the game using wine and get them bombs!!!

Happy gaming! "Fire in the hole!" :D

.. _such as this: http://web.nickshanks.com/fonts/microsoft-core-web-fonts
