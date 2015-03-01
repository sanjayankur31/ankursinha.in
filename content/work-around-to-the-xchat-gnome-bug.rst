Work Around to the xchat-gnome bug
##################################
:date: 2009-02-11 18:02
:author: ankur
:category: FOSS
:tags: bugzilla, Fedora, transparency, workaround, X server, xchat-gnome
:tags: bugzilla, Fedora, transparency, workaround, X server, xchat-gnome
:tags: bugzilla, Fedora, transparency, workaround, X server, xchat-gnome
:tags: bugzilla, Fedora, transparency, workaround, X server, xchat-gnome
:slug: work-around-to-the-xchat-gnome-bug

I posted on fedoraforum.org and got a workaround for the xchat-gnome
bug.

    | 1. run gconf-editor (yum install gconf-editor)
    |  2. go to apps->xchat->main\_window
    |  3. set "background\_transparency" to 0
    |  4. You should be able to use xchat-gnome as you did before

Its a reported bug : https://bugzilla.redhat.com/show_bug.cgi?id=478649

I used the workaround to reporoduce it.. :)
