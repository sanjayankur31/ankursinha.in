Giving Qutebrowser a go - a fantastic keyboard-focused browser
##############################################################
:date: 2017-06-21 00:09:30
:author: ankur
:category: Tech
:tags: Fedora, FlatPak, Free software, Linux, Python, Vim, Qutebrowser
:slug: giving-qutebrowser-a-go-a-fantastic-keyboard-focused-browser
:summary: After years of using the excellent Firefox, I've decided to tweak my workflow a little more by giving Qutebrowser_ a go. Qutebrowser_ is a brilliant keyboard-focused browser. In this post, I document my first day with Qutebrowser_, and I also include some tips and tricks that others may find helpful.


.. raw:: html

    <center>


.. image:: {static}/images/20170621-qutebrowser3.png
    :alt: A screenshot showing hints in Qutebrowser on the Qutebrowser website
    :target: {static}/images/20170621-qutebrowser3.png
    :width: 80%
    :class: text-center img-responsive pagination-centered

.. raw:: html

    </center>


Years ago, I was introduce to `touch typing <https://en.wikipedia.org/wiki/Touch_typing>`__. I knew immediately that it was a skill I must learn. I remember spending hours playing with `gtypist <https://apps.fedoraproject.org/packages/gtypist>`__ trying to improve my typing efficiency. I'm not too bad nowadays. I can mostly type without looking at the keyboard at all, and with few errors. 

I've always loved using the command line. In fact, I maintain that new programmers should start at the command line and only move to IDEs once they've learned exactly what's being done under the hood. I use the terminal as much as conveniently possible - music via `ncmpcpp <https://apps.fedoraproject.org/packages/ncmpcpp>`__, IRC on `irssi <https://apps.fedoraproject.org/packages/irssi>`__ (there are Gitter and Slack gateways to IRC too), `taskwarrior <https://apps.fedoraproject.org/packages/task>`__ to organise my TODOs, all my writing in VIM_ (programming and otherwise), for example. `Byobu <https://apps.fedoraproject.org/packages/byobu>`__ makes it really easy.

The one effect sticking to the command line so much has had on me is that I've developed a slight aversion to the mouse/touchpad. I now feel mildly annoyed if I must move my fingers off the home-row to do something. I must use the touchpad to check my mail/calendar on Evolution, for example, but this doesn't annoy me too much because I usually check these when I've taken a break from programming (or my `code is compiling <https://xkcd.com/303/>`__). It's really on Firefox that the constant switching between keyboard and mouse used to be a real downer.

Being a VIM_ user, I did the expected - went looking to see if there was a way to use VIM_ style key-mappings on Firefox. There are multiple add-ons that permit this with different feature sets - `vimperator <http://vimperator.org/>`__, `pentadactyl <http://5digits.org/pentadactyl/>`__, `vimium <https://vimium.github.io/>`__, `vimFX <https://addons.mozilla.org/en-GB/firefox/addon/vimfx/>`__ are a few examples. Now, the different features these provide cater to different people's requirements. I went for pentadactly. Not only does it permit VIM_ style key mappings and navigation, it also provides a vim style command line that is incredibly handy. I've used it for years now. The issue that has troubled pentadactyl for some time now is constant breakage - it tends to break each time the Firefox addon API is updated. Recently, I `read that some major changes in the API will make pentadactly pretty much unusable in the near future <https://github.com/5digits/dactyl/issues/99>`__. This made me go looking for a more stable alternative. I tried one or two others - vimium for example, but somehow, I find vimium too simple.

So, I `dug further <https://www.reddit.com/r/linux/comments/3aqmhd/why_cant_we_have_a_nice_vimlike_webkit_browser/>`__ and ran into `Vimb <https://fanglingsu.github.io/vimb/>`__ and Qutebrowser_. They're both "vim like browsers" i.e., they're designed for more advanced users and they provide VIM_ like key-mappings and modes. I gave vimb a short try, but Qutebrowser_ really impressed me a lot more.

Qutebrowser
-----------

The best thing about Qutebrowser_ is that it's `actively maintained <https://github.com/qutebrowser/qutebrowser/pulse/monthly>`__. I even hopped on to the `IRC channel <https://webchat.freenode.net/?channels=#qutebrowser>`__ earlier today to get some help. The latest version is in Fedora already, so you can simply go :code:`sudo dnf install qutebrowser` to give it a whirl. I wanted to test out the latest codebase, so I quickly set up a `copr repository <https://copr.fedorainfracloud.org/coprs/ankursinha/qutebrowser/>`__ that you can use too. I'm tinkering with `FlatPak <http://flatpak.org/>`_ to try and build one too, so that it becomes even easier to install, but I'm still figuring out how FlatPaks are built.

.. raw:: html

    <center>

.. image:: {static}/images/20170621-qutebrowser1.png
    :alt: A screenshot showing hints in Qutebrowser
    :target: {static}/images/20170621-qutebrowser1.png
    :width: 80%
    :class: text-center img-responsive pagination-centered


.. raw:: html

    </center>

The screenshot shows "hinting" which is how one opens links. You press "f" and the various links in the page get labelled. Simply type the label of the link you want to visit. There's also "advanced hinting" which lets you do things like open links in a background tab, or in a new tab, or save (`yank <https://unix.stackexchange.com/questions/209660/why-is-the-vi-editors-copy-command-called-yank>`__) a link URL.

.. raw:: html

    <center>

.. image:: {static}/images/20170621-qutebrowser2.png
    :alt: A screenshot showing the command mode in Qutebrowser
    :target: {static}/images/20170621-qutebrowser2.png
    :width: 80%
    :class: text-center img-responsive pagination-centered

.. raw:: html

    </center>

This one shows the command mode - everything can be done here, including configuration of the browser or browsing related tasks.

A few tips
==========

I did a few things to get started. First, I wanted to use the new "webengine" backend. This requires the installation of two packages: :code:`sudo dnf install python3-pyopengl python3-qt5-webengine`, and then creating a new file in :code:`~/.local/share/applications/qutebrowser.desktop` with the following contents:

.. code:: ini

    [Desktop Entry]
    Name=qutebrowser
    GenericName=Web Browser
    Icon=qutebrowser
    Type=Application
    Categories=Network;WebBrowser;
    Exec=qutebrowser --backend webengine %u
    Terminal=false
    StartupNotify=false
    MimeType=text/html;text/xml;application/xhtml+xml;application/xml;application/rdf+xml;image/gif;image/jpeg;image/png;x-scheme-handler/http;x-scheme-handler/https;
    Keywords=Browser
    X-Desktop-File-Install-Version=0.23

This new file simply ensures that picking Qutebrowser_ from the activities menu will run the new backend. Without this, one would have to launch it from the terminal each time.

Next, I configured it a bit to my liking - still very limited, but it's a start. The configuration file for Qutebrowser_ is at :code:`~/.config/qutebrowser/qutebrowser.conf`.  There's so much one can modify here. I've only set up a few search engines and updated the default to Google. To do this, one needs to modify the :code:`[searchengines]` section in the file:

.. code:: ini

    DEFAULT = https://google.com/search?hl=en-GB&q={}
    duckduckgo = https://duckduckgo.com/?q={}
    github = https://github.com/search?q={}
    google-scholar = https://scholar.google.co.uk/scholar?hl=en&q={}


I also enable :code:`save-session` - just set it to :code:`true`. There are a few other tweaks, such as updating the :code:`startpage` to http://start.fedoraproject.org. There's even a built in ad-blocker that one can configure.

To get flash working, one needs to also install the ppapi bits. Assuming one already has the flash plugin repository installed, :code:`sudo dnf install flash-player-ppapi` does this. I haven't gotten Netflix to work yet - it requries some Silverlight thingy. I can always run Chrome or FF for that one rare purpose anyway.

There are, obviously a few limitations in the current Qutebrowser_ version. The most noticeable one is probably the lack of a sync service similar to ones Firefox and Chrome provide. Google does tell me something about using `syncthing <https://syncthing.net/>`__ but I haven't gotten down to this yet. While it would be nice to have, it isn't quite that necessary. There isn't a password manager either. There are `plans to develop a plug-in system <https://github.com/qutebrowser/qutebrowser/issues/30>`__ in the pipeline to implement such features already, though. (`userscripts <https://github.com/qutebrowser/qutebrowser/blob/master/doc/userscripts.asciidoc>`__ seem to provide some additional functionality too.)


Anyway, it's a great, quick, and lean browser if you're a VIM_ addict like me, so give it a go? If you have some cycles and are intersted in some hacking, get in touch with the devs over Github too. If not, please do at least `file bugs <{filename}/20170501-a-well-filed-software-issue-considerably-improves-the-chances-of-the-issue-being-fixed-quicker.rst>`__ if you see them.

Here's a `quickstart <https://www.qutebrowser.org/doc/quickstart.html>`__ to quickly get up and running with. Oh, and yeah, *the mouse/touchpad works in the browser too*!


.. _Qutebrowser: https://www.qutebrowser.org/
.. _VIM: https://vim.sourceforge.io/
