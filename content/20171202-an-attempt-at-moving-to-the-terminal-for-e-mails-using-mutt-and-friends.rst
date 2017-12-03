An attempt at moving to the terminal for e-mails using Mutt and friends
#######################################################################
:date: 2017-12-02 21:46:07
:author: ankur
:category: Tech
:tags: Fedora, Linux
:slug: an-attempt-at-moving-to-the-terminal-for-e-mails-using-mutt-and-friends
:status: draft
:summary: I've long wanted to switch to the terminal for managing my e-mail. I
          do everything else in a byobu instance anyway. Today, I finally took
          the plunge to set it up. I've only moved one account, and one that I
          rarely use, as a test here. Instructions within.


I use the terminal wherever possible. It isn't because I don't like GUI
applications. I just like to do as much as possible using the keyboard, and not
having to move to use the mouse. So, I use VIM, and any applications that let
me use VIM keybindings in a byobu instance. I'm so used to using hjkl for
navigation now, that having to move to the arrow keys to scroll feels like
overkill. Some applications that provide VIM bindings are:

- ncmpcpp (for music)
- vifm (terminal, dual pane file manager)
- vimiv (image viewer)
- qutebrowser (a full browser!)
- zathura (pdf viewer)

This is all on a Fedora 27 system, but most of the steps should be general
enough to work on other distributions. One will have to go find the right
packages, though. I followed `this guide
<https://hobo.house/2015/09/09/take-control-of-your-email-with-mutt-offlineimap-notmuch/>`__
as the main source of information, and the looked around when I needed some
more info.

Offlineimap
-----------




List of references
------------------

Here are all the links I looked at, in no particular order:

- https://hobo.house/2015/09/09/take-control-of-your-email-with-mutt-offlineimap-notmuch/
- https://github.com/sadsfae/misc-dotfiles/blob/master/muttrc-gpg.txt
- http://upsilon.cc/~zack/blog/posts/2011/01/how_to_use_Notmuch_with_Mutt/
- https://notmuchmail.org/
- https://git.notmuchmail.org/git/notmuch/blob/HEAD:/vim/README
- https://www.neomutt.org/guide/optionalfeatures
- https://wiki.archlinux.org/index.php/OfflineIMAP#Using_pass
- http://www.df7cb.de/blog/2010/Using_multiple_IMAP_accounts_with_Mutt.html
- https://github.com/OfflineIMAP/offlineimap/blob/master/offlineimap.conf
- https://wiki.archlinux.org/index.php/OfflineIMAP
- http://www.offlineimap.org/doc/use_cases.html
- https://sparkslinux.wordpress.com/2014/01/30/configuring-offlineimap-to-validate-ssltls-certificates/
- http://stevelosh.com/blog/2012/10/the-homely-mutt/#why-local-email
