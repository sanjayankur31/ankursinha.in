Transitioning to Neomutt and friends for e-mail
###############################################
:date: 2017-12-10 15:47:30
:author: ankur
:category: Tech
:tags: Fedora
:slug: transitioning-to-neomutt-and-friends-for-e-mail
:status: draft
:summary: I finally took some time out to set up neomutt_ and related tools
          that let me access my e-mail in a terminal. This post documents why,
          and how I went about it.


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
use :code:`hjkl` to move around, and as far as possible, my fingers do not leave the
`home row <https://en.wikipedia.org/wiki/Touch_typing>`__ on the keyboard. In
Gnome Shell, for example, I switch between applications using the Alt+Tab
combination.


I'm constantly seeking out applications that provide Vim_ like keyboard
bindings---it ensures that I have one set of keys that does the same thing
everywhere, and so, it saves me from having to:

- remember different hot keys for different applications
- leave the home row to use the mouse/touchpad.

So, I now use the excellent byobu_ where I run:

- ncmpcpp_ for music: it provides Vim_ like key bindings.
- Vifm_ for file management, although, a command line is usually sufficient.
- Vit_ as a Taskwarrior_ terminal based front-end, which, yep, provides Vim_
  like key-bindings.
- Weechat_ for IRC which also has `Vim bindings <https://github.com/GermainZ/weechat-vimode>`__.

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

Please note that everything that is documented here is for an up to date
Fedora_ 27 system. Most steps should be general enough to work on other
distributions. One will have to go find the right packages, though. I followed
`this guide
<https://hobo.house/2015/09/09/take-control-of-your-email-with-mutt-offlineimap-notmuch/>`__
as the main source of information, and the looked around when I needed some
more info.

E-mail: the details
--------------------

When a majority of us use e-mail, we simply interact with a client. These
clients: Evolution_/Thunderbird/Outlook or the web applications that we access,
keep the nitty-gritty details away from end users. The `wikipedia article
<https://en.wikipedia.org/wiki/Email#Operation_overview>`__ on e-mail explains
the process quite well:

- An MUA (mail user agent) is the client that we use to read/write email.
- The MUA interacts with an MSA (mail submission agent) to send e-mail, or an
  MDA (mail delivery agent) to receive e-mail to and fro a mailbox.


mutt_ is an MUA, so we need to set up the other bits for it to be able to
interact with an MSA and an MDA, and that's why it is a little more work than
setting up Evolution_ and so on where the tool takes care of setting up the
whole chain.

Fetch e-mail with Offlineimap
-----------------------------

There are a few tools that fetch e-mail. Offlineimap_ seemed to be widely used,
so I settled for it as well. On Fedora_, one can use DNF:

.. code:: bash

    sudo dnf install offlineimap

One must then set up their accounts with credentials and the sort. An example
config file is provided with the package at
:code:`/usr/share/doc/offlineimap/offlineimap.conf`

The config format is quite self explanatory. Here's an example:

.. code:: ini

    [general]
    accounts = account1

    [Account account1]
    localrepository = account1-local
    remoterepository = account1-remote
    status_backend = sqlite
    postsynchook = notmuch new

    [Repository account1-remote]
    type = IMAP
    remotehost = mailhost.com
    remoteport = 587
    remoteuser = username@mailhost.com
    remotepass = password
    ssl = no
    folderfilter = lambda foldername: foldername in ['INBOX', 'Sent', 'Spam', 'Trash', 'Drafts']
    createfolders = False
    maxconnections = 2

    [Repository account1-local]
    type = Maildir
    localfolders = ~/Mail
    restoreatime = no


There's a "general" section where one defines what accounts are to be used. One
can also define global options that will apply to all accounts here.

For each account, one then sets up the main configurations, and then set up the
remote and local repositories. There are other advanced options that one can
use too. The :code:`folderfilter`, for example, is a python statement that lets
one select what folders on the remote should by synced. More in the offlineimap
documentation.

The :code:`postsynhook` bit lets one run a command after offlineimap has
finished syncing. Here, it calls code:`notmuch` to update its database. More on
notmuch_ later.

Once configured, one can run offlineimap to fetch one's mail. The first sync
will take quite a while, but subsequent syncs will be much quicker.

.. code:: bash

    offlineimap

I set up a cronjob_ to sync my e-mail regularly. Most users also use a script
that kills previously running offlineimap instances that may have hung, so a
script like this may be more useful:

.. code:: bash

    check ()
    {
        while pkill offlineimap
        do
            sleep 2
        done
    }

    quick ()
    {
        offlineimap -u quiet -q -s
    }

    full ()
    {
        offlineimap -u quiet -s
    }

    # parse options
    while getopts "qf" OPTION
    do
        case $OPTION in
            q)
                check
                quick
                exit 0
                ;;
            f)
                check
                full
                exit 0
                ;;
            ?)
                echo "Nothing to do."
                exit 1
                ;;
        esac
    done


My crontab then looks like this:

.. code:: bash

    */20 * * * * /home/asinha/bin/fetch-mail.sh -q
    10 */8 * * * /home/asinha/bin/fetch-mail.sh -f

So, every 20 minutes, I do a quick sync, and once every 8 hours, I do a full
sync.


Sending e-mail with msmtp
-------------------------

Now that we can fetch our e-mail, we look at sending e-mail. sendmail_ is quite
a well known client, but the setup is a bit cludgy for me. msmtp_ was
recommended by quite a few users. On Fedora_, one can install it using DNF:

.. code:: bash

    sudo dnf install msmtp

The configuration for msmtp_ is quite simple too. The package provides two
example configuration files:

.. code:: bash

    /usr/share/doc/msmtp/msmtprc-system.example
    /usr/share/doc/msmtp/msmtprc-user.example


Here's an example:

.. code:: ini

    defaults
    protocol smtp
    auth on
    tls on
    tls_trust_file /etc/ssl/certs/ca-bundle.crt
    syslog LOG_USER
    logfile ~/.msmtp.log
    timeout 60

    account account1
    host smtp.hostname.com
    port 587
    domain hostname.com
    from something@hostname.com
    user username@hostname.com
    password password


It has a default section where options common to all accounts can be set up.
here it does to usual setup regarding TLS, and so on.

A separate section for each account then holds the credentials. One can thenn
send e-mail from the command line:

.. code:: bash

    echo "Subject: Test" | msmtp -a account1 someone@anotherhost.com


Setting up the MUA: (neo)mutt
-----------------------------

The two MTAs are not set up, and we can fetch and send mail. We can now link
thse up to our MUA, mutt_. Instead of mutt_, I use neomutt_ which is mutt_ with
additional patches and features. It isn't in the Fedora repos yet, but thre's a
copr repository set up for users:

.. code:: bash

    sudo dnf enable copr flatcap/neomutt
    sudo dnf install neomutt


The neomutt_ configuration is based on the mutt_ bits, and it's rather
extensive. The package provides an example that I use as a starting point:

.. code:: bash

    /usr/share/doc/offlineimap/offlineimap.conf

The important bits are here:

.. code:: ini

    mailboxes ="account1"
    mailboxes `find ~/Mail/account1/* -maxdepth 0 -type d | grep -v "tmp\|new\|cur" | sed 's|/home/asinha/Mail/|=\"|g' | sed 's|$|\"|g' | tr '\n' ' '`
    set from = "user@hostname.com"
    set use_from = "yes"
    set reply_to = "yes"
    set sendmail = "msmtp -a account1"
    set sendmail_wait = 0
    set mbox = "+account1/INBOX"
    set postponed = "+account1/Drafts"
    set record = "+account1/Sent"


The :code:`mailboxes` list what folders the sidebar in neomutt_. These are what
we've set up offlineimap to fetch for us. Similarly, the :code:`sendmail`
setting tells neomutt to use :code:`msmtp` to send e-mail.

Searching e-mail with notmuch
-----------------------------


Other tweaks
-------------

Storing passwords using pass
============================

Multiple accounts
==================

GPG signing
===========

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
- https://github.com/neomutt/neomutt/issues/629 - address completion using
  notmuch

.. _neomutt: https://www.neomutt.org
.. _Vim: https://vim.org
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
.. _Fedora: http://getfedora.org
.. _Offlineimap: http://www.offlineimap.org/
.. _notmuch: https://notmuchmail.org/
.. _cronjob: https://en.wikipedia.org/wiki/Cron
.. _sendmail: https://en.wikipedia.org/wiki/Sendmail
.. _msmtp: http://msmtp.sourceforge.net/
