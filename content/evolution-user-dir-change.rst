Evolution user dir change
#########################
:date: 2011-01-07 09:38
:author: ankur
:category: FOSS
:tags: Evolution, Fedora
:tags: Evolution, Fedora
:tags: Evolution, Fedora
:tags: Evolution, Fedora
:slug: evolution-user-dir-change

Evolution has moved to using the `XDG standard`_ for user directories.
Your evolution data is now stored in **~/.local/share/evolution**
instead of **~/.evolution**. If you weren't already aware, it's time to
update your backup confs. The change happened in 2.32 iirc.

.. _XDG standard: http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html
