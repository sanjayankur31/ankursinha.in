Byobu and mc
############
:date: 2012-05-24 22:14
:author: ankur
:category: Tech
:tags: Fedora
:slug: byobu-and-mc

|midnight commander on byobu|

 

I'm a big fan of `byobu`_. Even though folks have moved over to using
`tmux`_ as the backend, I still use `gnu screen`_. It works for me. Now,
another tool that I'm a huge fan of is `midnight commander`_, or as it's
referred to "mc". Using the default keybindings that byobu sets up makes
mc a little difficult to use. The
**/usr/share/byobu/keybindings/f-keys.screen** file will tell you why:

::

    bindkey "^[[1;2A" focus up                              # shift-up | focus up
    bindkey "^[[1;2B" focus down                            # shift-up | focus down
    bindkey "^[[1;2D" focus up                              # shift-left | focus up
    bindkey "^[[1;2C" focus down                            # shift-right | focus down

These lines capture the shift + arrow keys. In mc, shift + up/down is
used to select multiple files in the panels. Understandibly, this is an
anoyance. I had a tough time when I wanted to select multiple files to
copy/move in mc. I've been looking for a fix. The fix is to disable the
byobu key bindings. This may be overkill, so you can just unbind the
shift+arrow keys. I've disabled them, to use the default screen
bindings. Now, here's where a bug crept in. "Escape" + ! is supposed to
be the "toggle f-keys" command. However, ctrl + a (escape) + ! for me
only prints out the following on the terminal:

::

    ":source /usr/share/byobu/keybindings/f-keys.screen.disable" (with the starting ":")

I found a `bug already mentioning the issue`_. I've filed a `new one as
requested in the last comment`_. There is a `workaround`_ which works
well! I can now use mc properly with byobu!

.. _byobu: http://launchpad.net/byobu
.. _tmux: https://bugs.launchpad.net/fedora/+source/byobu/+bug/1004031
.. _gnu screen: https://bugs.launchpad.net/fedora/+source/byobu/+bug/1004031
.. _midnight commander: http://en.wikipedia.org/wiki/Midnight_Commander
.. _bug already mentioning the issue: https://bugs.launchpad.net/byobu/+bug/389129/
.. _new one as requested in the last comment: https://bugs.launchpad.net/fedora/+source/byobu/+bug/1004031
.. _workaround: https://bugs.launchpad.net/byobu/+bug/389129/comments/8

.. |midnight commander on byobu| image:: http://ankursinha.in/wp/wp-content/uploads/2012/05/screenshot-from-2012-05-24-221209.png?w=300
   :target: http://ankursinha.in/wp/wp-content/uploads/2012/05/screenshot-from-2012-05-24-221209.png
