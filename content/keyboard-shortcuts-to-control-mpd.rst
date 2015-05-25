Keyboard shortcuts to control mpd
#################################
:date: 2011-06-20 12:45
:author: ankur
:category: Tech
:tags: Fedora
:slug: keyboard-shortcuts-to-control-mpd

I `use`_ ncmpc, which is a great great curses based client for mpd.
However, my multimedia keys won't work with ncmpc. I've been looking
around for a while, trying to make them work so I don't have to keep
switching to ncmpc when I want to move to the next song etc. I finally
found something today. It works!

This is for **gnome-shell** on a fedora 15 system.

Hit the "hot corner", in the search box write "keyboard" (The search box
is really convenient)

Once you're there, create a custom short cut (look at the bottom of the
keyboard settings dialog).

Create a new one. Name it "MPC play", and in the command, write "mpc
toggle". It will be disabled, click on disabled and press "ctrl + shift
+ alt +p". Of course, you can put whatever key bindings you
like.Similarly, add another for stop, prev, next. Look up "man mpc" for
the commands.

Simple, effective, awesome! Cheers!

Edited: mpc toggle added.

Edited: Notifications from mpc

If you want to see what song's playing, you can use a simple script such
as this one:

::

    if [ -x /usr/bin/notify-send ]
    then
        status=`mpc status | egrep playing`

        # check if playing
        if [ -n "$status" ]
        then
            notify-send -t 5 -i /usr/share/icons/gnome/scalable/actions/media-playback-start-symbolic.svg "MPD: Now Playing -> " "`mpc status | head -1`"
        else
            # is it paused
            if [ -n "`mpc status | egrep paused`" ]
            then
                notify-send -t 5 -i /usr/share/icons/gnome/scalable/actions/media-playback-pause-symbolic.svg "MPD: Paused -> " "`mpc status | head -1`"
            else
                notify-send -t 5 -i /usr/share/icons/gnome/scalable/actions/media-playback-stop-symbolic.svg "MPD: Stopped!"
            fi
        fi
    else
        echo "notify-send not installed"
        exit -1
    fi

    exit 0

Now make a mapping for it, I've used ctrl + shift + alt + w (what's
playing now).

.. _use: http://dodoincfedora.wordpress.com/2011/02/26/playing-your-music-from-the-terminal-mpd-setup/
