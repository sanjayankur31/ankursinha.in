Installing skype: big trouble!!
###############################
:date: 2009-11-18 17:24
:author: ankur
:category: FOSS
:tags: Fedora 12, Skype
:tags: Fedora 12, Skype
:tags: Fedora 12, Skype
:tags: Fedora 12, Skype
:slug: installing-skype-big-trouble

ah, simple, yum install skype-2.1.0.47-fc10.i586.rpm should do it for
me.. But wait!! What do we have here?? It installed without pulling in
ANY deps, and obviously skype din't work. Errors: "missing this missing
that!!"

Now I'm sitting here running alternating "yum installs" and "yum
whatprovides" to try and manually install the deps.  And, yeah, since
it's an i586 package, I'm installing i686 packages to support it on my
x86\_64 system. Talk about trouble!

Already, my webcam module wont build. Dunno how they manage to build it
here http://forums.fedoraforum.org/showthread.php?t=160117&page=3

It doensn't build ( as you can see from my repeated cries on the thread
)

Guess it's a bad day to install stuff :\|

 

EDIT

Steps (from my comment below):

yum install qt-x11-4.5.3-9.fc12.i686

yum install qt-4.5.3-9.fc12.i686

yum install libXScrnSaver-1.2.0-1.fc12.i686

yum install libXv-1.0.5-1.fc12.i686

yum install alsa-lib-1.0.21-3.fc12.i686

and after all this, it functions with an error (doesnt cause any harm
though) which requires

yum install alsa-plugins-pulseaudio-1.0.21-2.fc12.i686

 
