Setting up irssi on Fedora.
###########################
:date: 2010-12-05 15:54
:author: ankur
:category: Tech
:tags: Fedora
:slug: setting-up-irssi-on-fedora

There are a lot of IRC clients that one can use. The more frequently
used are `X-Chat`_, `Pidgin`_ and `irssi`_. Since I prefer to stick to
the terminal, I user the GNU Screen + irssi combination. Screen is
configured to automatically run irssi on start up, and irssi is
configured to "autojoin" the respective fedora IRC channels, with
password authentication. I'll spell out the steps.

Install irssi, screen:
----------------------

Fire up a terminal and go:

::

    $ su -c 'yum -y install irssi screen'

Once the install completes, proceed to setting them up for yourself.

Configure screen
----------------

I've put up a sample .screenrc file `here`_. You can use it as a
starting template. Place it as **~/.screenrc.** Documentation on screenrc
file options is
`here <http://www.gnu.org/software/screen/manual/html_node/index.html#Top>`__.
Do replace the names etc. with your own ;)

Configuring irssi
-----------------

I've also put up a sample config file for irssi `here.`_ This one is set
up to auto connect to Freenode, auto join a bunch of Fedora channels,
and also has quite a few aliases. Replace the <nickname> with your nick
etc.before you attempt to run irssi. **Your nick must
be\ `registered`_\ with Freenode**. The file needs to be placed as
**~/.irssi/config**\ **.**

Running irssi
-------------

Fire up a terminal and go:

::

    $ screen

and it should work!

Extra commands
--------------

Some necessities to start you up with:

-  Once in screen, use **Ctrl + a followed by a "?"** to see the
   commands.
-  In irssi, **Meta + <1 to 0>** cycles channels in windows 1 to 10.
   **Meta** is usually the **Alt** key. **Escape followed by a number**
   works as well. For windows **10-20**, use the **qwerty row** on the
   keyboard. Once can also use**/win <window#>** to change windows.

Added reading
-------------

Refer to these pages for detailed info :

-  `GNU Screen docs`_
-  `irssi docs`_
-  Google up, there are many many pages with info on using Screen and
   irssi together.
-  `Fedora project wiki page`_ on using X-chat.
-  `Fedora project wiki page <http://fedoraproject.org/wiki/IRC>`__ on
   how to use the IRC.

.

.. _X-Chat: http://www.xchat.org/
.. _Pidgin: http://www.pidgin.im/
.. _irssi: http://www.irssi.org/
.. _here: http://ankursinha.fedorapeople.org/IRC/screenrc
.. _here.: http://ankursinha.fedorapeople.org/IRC/config
.. _registered: http://freenode.net/faq.shtml#nicksetup
.. _GNU Screen docs: http://www.gnu.org/software/screen/manual/html_node/index.html#Top
.. _irssi docs: http://www.irssi.org/documentation
.. _Fedora project wiki page: http://dodoincfedora.wordpress.com/2010/12/05/setting-up-irssi-on-fedora/
