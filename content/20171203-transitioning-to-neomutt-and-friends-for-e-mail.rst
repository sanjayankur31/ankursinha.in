Transitioning to Neomutt and friends for e-mail
###############################################
:date: 2017-12-16 00:01:53
:author: ankur
:category: Tech
:tags: Fedora
:slug: transitioning-to-neomutt-and-friends-for-e-mail
:summary: I finally took some time out to set up neomutt_ and related tools
          that let me access my e-mail in a terminal. This post documents how I
          went about it.


I'm constantly seeking out applications that provide Vim_ like keyboard
bindings---it ensures that I have one set of keys that does the same thing
everywhere, and so, it saves me from having to:

- remember different hot keys for different applications
- leave the `home row`_ to use the mouse/touchpad (Yeh, the home row is a
  thing!)

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

In all of the above mentioned applications, :code:`hjkl` moves about, other hot
keys such as :code:`G` and :code:`gg`, and so on work too, and they even have a
command mode that can be accessed using :code:`:` as in Vim_. So, I don't have
to think of the shortcuts now---it's all muscle memory!

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
more info. I've collected a list of links at the bottom of this post.

E-mail: the details
--------------------

When a majority of us use e-mail, we simply interact with a client. These
clients: Evolution_/Thunderbird_/Outlook or the web applications that we access,
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

The :code:`postsynchook` bit lets one run a command after Offlineimap_ has
finished syncing. Here, it calls :code:`notmuch` to update its database. More on
notmuch_ later.

Once configured, one can run Offlineimap_ to fetch one's mail. The first sync
will take quite a while, but subsequent syncs will be much quicker.

.. code:: bash

    offlineimap

I set up a cronjob_ to sync my e-mail regularly. Most users also use a script
that kills previously running Offlineimap_ instances that may have hung, so a
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

    account account2
    host smtp.anotherhostname.com
    port 587
    domain anotherhostname.com
    from something@anotherhostname.com
    user username@anotherhostname.com
    password password

It has a default section where options common to all accounts can be set up.
here it does to usual setup regarding TLS, and so on.

A separate section for each account then holds the credentials. One can then
send e-mail from the command line:

.. code:: bash

    echo "Subject: Test" | msmtp -a account1 someone@anotherhost.com


Setting up the MUA: (neo)mutt
-----------------------------

The two MTAs are now set up, and we can fetch and send mail. We can now link
these up to our MUA, mutt_. Instead of mutt_, I use neomutt_ which is mutt_ with
additional patches and features. It isn't in the Fedora repos yet, but there's a
COPR_ repository set up for users:

.. code:: bash

    sudo dnf copr enable flatcap/neomutt
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

If it all went well, running :code:`neomutt` should bring up a window like the
figure below:

.. figure:: {static}/images/20171215-neomutt.png
    :align: center
    :height: 800px
    :scale: 60%
    :target: {static}/images/20171215-neomutt.png
    :alt: A screenshot of Neomutt in action



On the left, there's the sidebar where all folders are listed. These can be
configured using :code:`mailboxes` as `explained in the documentation here
<https://www.neomutt.org/feature/sidebar-intro>`__. On the right hand side, the
various e-mails are listed on top in the :code:`index`, and a particular e-mail
is visible in the :code:`pager` view. As can be seen, the index view also shows
threads! (This is running in :code:`byobu`, by the way, which shows the other
information in the bottom information bar.) More on all of this in the
documentation, of course.


Searching e-mail with notmuch
-----------------------------

We have our e-mail set up, but we at the moment, it has a very basic search
feature that mutt_ provides. notmuch_, which thinks "not much mail" of your
massive e-mail collection helps here. notmuch_ is called after each Offlineimap
sync above, in the :code:`postsynchook`. Then, using simple keyboard shortcuts,
one can use notmuch_ search their whole e-mail database. notmuch_ has quite a
few advanced features, like searching as threads, and searching e-mail
addresses, and the sort. notmuch_ comes with the handy :code:`notmuch-config`
which makes configuration trivial. Here's an example below:

.. code:: bash

    $ notmuch address from:*lists.fedoraproject.org
    classroom-request@lists.fedoraproject.org
    freemedia-owner@lists.fedoraproject.org
    fedora-join-bounces@lists.fedoraproject.org
    fedora-join-owner@lists.fedoraproject.org
    cwg-request@lists.fedoraproject.org
    cwg-private-request@lists.fedoraproject.org


The same can be used within neomutt_ with a few simple hotkeys:

.. code::

    macro index <F8> \
    "<enter-command>set my_old_pipe_decode=\$pipe_decode my_old_wait_key=\$wait_key nopipe_decode nowait_key<enter>\
    <shell-escape>notmuch-mutt -r --prompt search<enter>\
    <change-folder-readonly>`echo ${XDG_CACHE_HOME:-$HOME/.cache}/notmuch/mutt/results`<enter>\
    <enter-command>set pipe_decode=\$my_old_pipe_decode wait_key=\$my_old_wait_key<enter>" \
     "notmuch: search mail"

    macro index <F9> \
    "<enter-command>set my_old_pipe_decode=\$pipe_decode my_old_wait_key=\$wait_key nopipe_decode nowait_key<enter>\
    <pipe-message>notmuch-mutt -r thread<enter>\
    <change-folder-readonly>`echo ${XDG_CACHE_HOME:-$HOME/.cache}/notmuch/mutt/results`<enter>\
    <enter-command>set pipe_decode=\$my_old_pipe_decode wait_key=\$my_old_wait_key<enter>" \
     "notmuch: reconstruct thread"

    macro index <F6> \
    "<enter-command>set my_old_pipe_decode=\$pipe_decode my_old_wait_key=\$wait_key nopipe_decode nowait_key<enter>\
    <pipe-message>notmuch-mutt tag -- -inbox<enter>\
    <enter-command>set pipe_decode=\$my_old_pipe_decode wait_key=\$my_old_wait_key<enter>" \
     "notmuch: remove message from inbox"


The three commands in a :code:`neomuttrc` file will respectively:

- bind F8 to open a neomutt_ search
- bind F9 to find a whole thread based the currently selected e-mail. This
  includes all folders.
- binds F6 to untag an e-mail (more on notmuch_ tagging in the docs)


Other tweaks
-------------

The aforementioned bits cover most of the main functions that one would need
with e-mail. Here are some more tips that I found helpful.

I have not yet set up a command line address book client. There seem to be a
few that sync with Gmail and other providers and can be used with mutt_, but I
don't need them yet.  notmuch_ provides sufficient completion for the time
being, and when I begin to use newer addresses that are not already in my
mailbox, I shall look at address book clients. For those that are interested,
these are what I've found:

- `abook <http://abook.sourceforge.net/>`__
- `gobook <https://gitlab.com/goobook/goobook>`__

Storing passwords using pass
============================

Storing passwords as plain text is a terrible idea. Instead most use password
managers. pass_ is an excellent command line password manager that uses GPG_
to encrypt password files. It even integrates with Git_ so that a central
repository can hold the encrypted files, and can be cloned to various systems.

Both Offlineimap_ and msmtp_ permit a user to store passwords in a tool and then
run a command to extract it. In the :code:`offlineimaprc`, for example, one can
use:

.. code:: ini

    remotepasseval = get_pass("E-mail")

to fetch passwords from pass. Here :code:`get_pass` is a python function that
does the dirty work:

.. code:: python

    def get_pass(account):
            return (check_output("pass " + account, shell=True).splitlines()[0]).decode("utf-8")


Similarly, msmtp_ lets one use a shell command to get a password:

.. code:: ini

    passwordeval pass E-mail

where the :code:`E-mail` file is associated with the password for a certain account using pass.

Multiple accounts
==================

Both Offlineimap_ and msmtp_ can handle multiple accounts. neomutt_ can too,
but to set sane defaults each time one switches mailboxes, a bit of trickery is
required. The `gist here <https://gist.github.com/miguelmota/9456162>`__ shows
what's needed. Essentially, using a :code:`folder-hook`, one updates the
required configurations (signature, from address, sent mail folder, draft
folder) when one switches to a folder associated with a different account. I
use four accounts in neomutt_ currently. It works rather well. The snippet
below is what I have in my neomutt_ configuration file. It sets up host3 as the
default account, and each time I change to a different host folder, the
folder-hook updates some configurations. Here, I have different files for each
host.

.. code:: ini

    # Hooks for multi-setup
    # default
    set folder ="~/Mail"
    set spoolfile = "+host3/INBOX"
    source ~/Documents/100_dotfiles/mail/host1.neomuttrc
    source ~/Documents/100_dotfiles/mail/host4.neomuttrc
    source ~/Documents/100_dotfiles/mail/host2.neomuttrc
    source ~/Documents/100_dotfiles/mail/host3.neomuttrc

    # folder hook
    folder-hook host4/* source ~/Documents/100_dotfiles/mail/host4.neomuttrc
    folder-hook host1/* source ~/Documents/100_dotfiles/mail/host1.neomuttrc
    folder-hook host2/* source ~/Documents/100_dotfiles/mail/host2.neomuttrc
    folder-hook host3/* source ~/Documents/100_dotfiles/mail/host3.neomuttrc



GPG signing
===========

I sign my e-mails with `my GPG key
<https://keys.fedoraproject.org/pks/lookup?search=0xE629112D&op=vindex>`__.
neomutt_ supports this via a few configuration options:

.. code:: ini

    set pgp_sign_as = 0xE629112D
    set crypt_autosign = "yes"
    set crypt_verify_sig = "yes"
    set crypt_replysign = "yes"


E-mails will be signed when they're going out, and when a signed e-mail comes
in, neomutt_ will verify the signature if the key is available and so on. If
you're not using GPG keys, this `guide on the Fedora wiki
<https://fedoraproject.org/wiki/Creating_GPG_Keys>`__ is a great guide for
beginners.

Viewing HTML mail and attachments
==================================

Even though I send all my e-mail as plain text, I do receive lots of HTML mail.
neomutt_ can be set up to automatically view HTML e-mail. It does so by using a
tool such as :code:`w3m` to strip the e-mail of HTML tags and show the text.
The screenshot below shows an example HTML from Quora.


.. figure:: {static}/images/20171215-neomutt-html.png
    :align: center
    :height: 800px
    :scale: 60%
    :target: {static}/images/20171215-neomutt-html.png
    :alt: A screenshot of Neomutt showing HTML e-mail.

A simple configuration line tells neomutt_ what to do:

.. code:: ini

    auto_view text/html

neomutt_ uses information from :code:`mailcap` to do this. For those that are
unaware of what :code:`mailcap` is, like I was, `here's the manual page
<https://linux.die.net/man/4/mailcap>`__.

The configuration file for :code:`mailcap` is :code:`~/.mailcaprc`. Mine looks
like this:

.. code::

    audio/*; /usr/bin/xdg-open %s ; copiousoutput

    image/*; /usr/bin/xdg-open %s ; copiousoutput

    application/msword; /usr/bin/xdg-open %s ; copiousoutput
    application/pdf; /usr/bin/xdg-open %s ; copiousoutput
    application/postscript ; /usr/bin/xdg-open %s ; copiousoutput

    text/html; qutebrowser %s && sleep 5 ; test=test -n "$DISPLAY";
    nametemplate=%s.html; needsterminal
    # text/html; lynx -dump %s ; copiousoutput; nametemplate=%s.html
    text/html; w3m -I %{charset} -T text/html ; copiousoutput; nametemplate=%s.html

One can use either :code:`lynx` or :code:`w3m`. I tried both and settled for
:code:`w3m`. Fedora_ systems have a default :code:`mailcaprc` file at
:code:`/etc/mailcap` which I adapted from. The :code:`copiousoutput` option
tells neomutt_ not to quickly delete the temporary file.

For cases where HTML e-mails also contain images, one can simply open the HTML
e-mail in a browser. The HTML e-mails are present as attachements to the e-mail
message. Pressing :code:`v` on an e-mail message shows the attachement menu.
The screenshot below shows the attachment menu for the same e-mail as above.
Hitting enter opens up the HTML attached version in the browser I've set up in
my :code:`mailcap` above, :code:`qutebrowser`.


.. figure:: {static}/images/20171215-neomutt-attachments.png
    :align: center
    :height: 800px
    :scale: 60%
    :target: {static}/images/20171215-neomutt-attachments.png
    :alt: A screenshot of Neomutt showing e-mail attachments.


Note: all attachments can be viewed like this.

Viewing links with urlview
===========================

Since I use byobu_, which is based on either tmux_ or screen_, I can copy and
paste any text in the terminal using their buffers. neomutt_ provides an easier
way, though, using urlview_. So, binding ctrl-b to urlview_ will put the e-mail
through urlview_ to show a menu of all URLs in it. One can then pick what URL
to open, as the screenshot below shows:

.. code::

    # urlview bits
    macro index \cb | urlview\n
    macro pager \cb | urlview\n


.. figure:: {static}/images/20171215-neomutt-urlview.png
    :align: center
    :height: 800px
    :scale: 60%
    :target: {static}/images/20171215-neomutt-urlview.png
    :alt: A screenshot of Neomutt with urlview.

Right then, let's stick to the home row!
----------------------------------------

This post turned out to be a lot lengthier than I'd expected. There's always so
much tweaking one can do. I hope this helps somewhat. It isn't complete by a
far stretch, but it should include enough hints and links to enable a reader to
Google up and figure things out. Read the docs, read the manuals---it's all in
there.


Happy e-mailing!

Incomplete list of references
-------------------------------

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
- http://jasonwryan.com/blog/2012/05/12/mutt/

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
.. _Thunderbird: https://www.mozilla.org/en-GB/thunderbird/
.. _COPR: https://copr.fedorainfracloud.org/
.. _pass: https://www.passwordstore.org/
.. _GPG: https://www.gnupg.org/
.. _Git: https://git-scm.com/
.. _tmux: https://github.com/tmux/tmux/wiki
.. _screen: https://www.gnu.org/software/screen/
.. _urlview: https://github.com/sigpipe/urlview
.. _home row: https://en.wikipedia.org/wiki/Touch_typing
