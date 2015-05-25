Trashing from the terminal : non destructively!
###############################################
:date: 2010-11-03 18:00
:author: ankur
:category: Tech
:tags: Fedora
:slug: trashing-from-the-terminal-non-destructively

I've got this habit of using rm and Shift + delete when I come across a
file that I'm not using. It's been costly at times when I've removed
files that I would later need. Now, since I've paid dearly a few times,
I've decided that the following are a must:

#. alias rm='rm -i' in ~/.bashrc
#. **NEVER USE SHIFT** while deleting
#. Since I spend most of my time on the console, install `ptrash`_ or
   `trash-cli`_ and make use of these when you have the urge to delete a
   file. (trash-cli seems better at a glance here)
#. Take time out in a fortnight and empty your waste basket.

.. _ptrash: https://admin.fedoraproject.org/pkgdb/acls/bugs/ptrash
.. _trash-cli: https://admin.fedoraproject.org/pkgdb/acls/bugs/trash-cli
