vim : copying to the system clipboard
#####################################
:date: 2010-11-28 11:32
:author: ankur
:category: Tech
:tags: Fedora
:slug: vim-copying-to-the-system-clipboard

Copying a file off vim to paste some place is sometimes a problem. If
you have line numbers enabled, you must disable them before selecting
the text, plus you manually need to re-compose your lines that broke
during the paste etc. I was pretty sure that there would be an easier
way of doing this. Google helped, as always. Here's the solution:

VIM has the clipboard facility. To see if it's enabled or not, run :

::

     vim --version grep -i clipboard

This is what I get:

::

    [ankurGuest@070905042 ~]$ rpm -qa grep vim
    vim-latex-1.8.23-1.20101027.r1112.fc13.noarch
    vim-X11-7.3.055-1.fc13.i686
    vim-common-7.3.055-1.fc13.i686
    vim-vimoutliner-0.3.4-12.fc12.noarch
    vim-minimal-7.3.055-1.fc13.i686
    vim-enhanced-7.3.055-1.fc13.i686
    vim-filesystem-7.3.055-1.fc13.i686
    [ankurGuest@070905042 ~]$ vim --version grep -i clipboard
    -clientserver -clipboard +cmdline_compl +cmdline_hist +cmdline_info +comments
     -xterm_clipboard -xterm_save
    [ankurGuest@070905042 ~]$

As you see, it's disabled. How then does one enable it? Well, **gvim**
in the **vim-X11** is what you need to use. If you like to stick to the
cli version, use **gvim -v**.

::

    [ankurGuest@070905042 ~]$ rpm -ql vim-X11 grep gvim
    /usr/bin/gvim
    /usr/bin/gvimdiff
    /usr/bin/gvimtutor
    /usr/share/applications/fedora-gvim.desktop
    /usr/share/icons/hicolor/16x16/apps/gvim.png
    /usr/share/icons/hicolor/32x32/apps/gvim.png
    /usr/share/icons/hicolor/48x48/apps/gvim.png
    /usr/share/icons/hicolor/64x64/apps/gvim.png
    /usr/share/man/man1/gvim.1.gz
    /usr/share/man/man1/gvimdiff.1.gz
    [ankurGuest@070905042 ~]$ gvim --version grep clipboard
    +clientserver +clipboard +cmdline_compl +cmdline_hist +cmdline_info +comments
    +xsmp_interact +xterm_clipboard -xterm_save

Once done, it's pretty simple to use the functionality. The **"+**
register holds the contents of the system clipboard, and the **"\***
register holds the contents of the X clipboard. So, if you want to copy
the entire file to the clipboard, you go **gg"+yG** or **gg"\*yG**.
Beware, the latter works only when you're using **xterm**. The former
works for gnome-terminal (what I use).
Added reading :
http://vim.wikia.com/wiki/Copy_an_Entire_Buffer_to_the_Clipboard

or in vim, go

::

     :h "+
    I thank the folks on the -devel list and #vim on Freenode who helped me get to this. (and google) Cheers!

