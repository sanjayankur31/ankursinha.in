Transitioning to Neomutt and friends for e-mail
###############################################
:date: 2017-12-03 12:04:51
:author: ankur
:category: Tech
:tags: Fedora
:slug: transitioning-to-neomutt-and-friends-for-e-mail
:status: draft
:summary: I finally took some time out to set up neomutt_ and related tools
          that let me access my e-mail in a terminal. This post documents why,
          and how I went about it.


Why?
----

I use Evolution_ on my Gnome workstation. It works rather well. It brings
together my Contacts, Calendar, and my E-mail in one place. The Gnome folks
have done a great job of integrating it with Gnome Online Accounts, and the
Gnome Shell too. It is an important application that I've used on a daily
basis, for a number of years now. As an end user, I have no complains from it
whatsoever.

The other application I use habitually is Vim_. If I can integrate things with
Vim_, I'll do that with the various plug-ins. I have quite a few set up now in
my `vimrc file <https://github.com/sanjayankur31/vimfiles/blob/master/vimrc>`__
and I keep adding to the list as I come across more of them. As a Vim_ user, I
use hjkl to move around, and as far as possible, my fingers do not leave the
`home row <https://en.wikipedia.org/wiki/Touch_typing>`__ on the keyboard. In
Gnome Shell, for example, I switch between applications using the Alt+Tab
combination. I'm constantly seeking out applications that provide Vim_ like
keyboard bindings---it ensures that I have one set of keys that does the same
thing everywhere, and so, it saves me from having to:

- remember different hot keys for different applications
- leave the home row to use the mouse/touchpad.

So, I now use the excellent byobu_ where I run:

- ncmpcpp_ for music: it provides Vim_ like key bindings.
- Vifm_ for file management, although, a command line is usually sufficient.
- Irssi_ for IRC: I haven't found Vim_ bindings for Irssi_ yet, and I'm looking
  to try out WeeChat_ which I read does provide them in the near future.
- Vit_ as a Taskwarrior_ terminal based front-end, which, yep, provides Vim_
  like key-bindings.

Vim_ has an in-built file browser, and one can use other plug-ins such as
NerdTree for more advanced tasks. I even have a Taskwarrior_ plug-in for Vim
that let's me quickly look up my tasks while writing code and the sort.

For other uses where the terminal is insufficient, I've found:

- Vimiv_ for viewing images
- Qutebrowser_ as a full featured browser. One can also use add-ons to
  Firefox/Chrome, but I've quite fallen for Qutebrowser_.
- Zathura_ for viewing various document types.

I rarely use LibreOffice---I mostly stick to LaTeX, and Vim_ deals with it
rather well.

In all of the above mentioned applications, hjkl moves about, other hot keys
such as G and gg, and so on work too, and they even have a command mode that
can be accessed using :code:`:` as in Vim_. So, I don't have to think of the
shortcuts now---it's all muscle memory!

Evolution_, being a modern GUI productivity tool, does not have a method to
navigate around only using a keyboard, and this got me to look for an e-mail
client that provided Vim_ like bindings. The answer I found was the rather well
known mutt_ terminal client. I'd been thinking of giving it a go for a while
now---more than a year. However, as I document later in this post, setting up
mutt_ isn't as trivial as setting up Evolution_ where one simply uses Gnome
Online Accounts and can get up and running in a few minutes.

At no point will I suggest that anyone migrate to such a terminal oriented
setup. This is tailored to my personal, rather Vim-y needs. One should use
whatever tools fit their personal tastes. We needn't spend time on "But, I
prefer this, and it's better!" themed conversations.

Please note that everything that is documented here is for an up to date a
Fedora 27 system. Most steps should be general enough to work on other
distributions. One will have to go find the right packages, though. I followed
`this guide
<https://hobo.house/2015/09/09/take-control-of-your-email-with-mutt-offlineimap-notmuch/>`__
as the main source of information, and the looked around when I needed some
more info.

Background
-----------

MUA, MTA etc etc

Fetching e-mail with Offlineimap
---------------------------------


Reading e-mail with Neomutt
----------------------------


Searching e-mail with notmuch
-----------------------------

Sending e-mail with msmtp
-------------------------


Sending e-mail with Neomutt
---------------------------


Other stuff
-----------

Viewing links with urlview
===========================

Opening attachments
===================


List of references
------------------

Here are most of the links I looked at, in no particular order:

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
- https://raisedfist.net/2017-05-02/muttupdated/
- https://stackoverflow.com/questions/18765928/mutt-send-signature-hook
- https://notmuchmail.org/vimtips/
- https://www.neomutt.org/guide/configuration.html#my-hdr
- https://www.neomutt.org/guide/advancedusage.html

.. _neomutt: https://www.neomutt.org
.. _Vim: https://vim.org
.. _Irssi: https://irssi.org/
.. _Vifm: https://vifm.info
.. _byobu: http://byobu.co/
.. _Vit: https://github.com/scottkosty/vit
.. _Taskwarrior: https://taskwarrior.org
.. _ncmpcpp: https://github.com/arybczak/ncmpcpp
.. _WeeChat: https://weechat.org
.. _Vimiv: http://karlch.github.io/vimiv/
.. _Zathura: https://pwmt.org/projects/zathura/
.. _Qutebrowser: http://www.qutebrowser.org/
.. _Evolution: https://wiki.gnome.org/Apps/Evolution
.. _mutt: http://www.mutt.org/
