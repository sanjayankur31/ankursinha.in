Adding version control to nautilus
##################################
:date: 2013-03-14 04:37
:author: ankur
:category: Tech
:tags: Fedora
:slug: adding-version-control-to-nautilus

On my `previous blog post`_, a comment pointed out that nautilus has
limitations for developers since it doesn't have version control
support. I found `rabbitvcs`_ on digging up, and it works really well.
This post is intended to just get it a little more visibility. Here's
how to set it up on Fedora:

``sudo yum install rabbitvcs-nautilus # Yep. That's it.``

Fire up nautilus after this, and navigate to a git repository. You'll
see a different icon set, showing what status your files in the
repository are in. Right click and use the rabbitvcs context menu. The
screen-shot below shows me using it to see the git history of the
`aeskulap package in fedora git`_.

 
I still use the terminal for my git purposes, but quite a few folks do
prefer the GUIs. Rabbitvcs should work well for them. It also has
support for other version control systems, svn etc., but I don't really
use anything other than git and haven't had a chance to check them out.

EDIT:
rabbit vcs doesn't work with nautilus in gnome3.8. There's a bug, and
a patch filed `here`_

.. _previous blog post: http://ankursinha.in/2013/03/07/i-really-like-gnome3/
.. _rabbitvcs: http://rabbitvcs.org/
.. _aeskulap package in fedora git: http://bugz.fedoraproject.org/aeskulap
.. _here: http://code.google.com/p/rabbitvcs/issues/detail?id=798
