yumdownloader: downloading x86_64 packages on i686 systems
##########################################################
:date: 2012-04-04 14:48
:author: ankur
:category: Tech
:tags: Fedora
:slug: yumdownloader-downloading-x86_32-packages-on-i686-systems

Note: This is at best, a hack.

Currently yumdownloader does not download x86\_64 packages on an i686
host. The --archlist argument is not sufficient, and ``setarch x86_64``
does not work. The --archlist argument doesn't work because yum picks up
repository information from the configuration files where $basearch is
expanded to i686 on the hosts. setarch is supposed to remedy this, but
it sadly doesn't. There's a `WONTFIX bug`_ on the matter.

I really needed to download some x86\_64 rpms to make an up to date
`Fedora Electronics Lab`_ spin to give out to a requester. This is what
I came up with:

In **/etc/yum.repos.d**/ , make copies of the **fedora.repo** and
**fedora-updates.repo**. Call them **fedora64.repo**,
**fedora-updates64.repo**. Then, modify the files to change the
repository names to **fedora64** and **fedora-updates64** respectively.
Then, use a search and replace, to change "**$basearch**\ " to
"**x86\_64**\ ".

Now,
``yumdownloader --disablerepo=* --enablerepo=*64* @electronic-lab --resolve``
will download your x86\_64 packages.

Do remember to remove the new repo files you've made, or at least
disable them. **Keeping them around for regular yum transactions may
break your system!**

.. _WONTFIX bug: https://bugzilla.redhat.com/show_bug.cgi?id=470938
.. _Fedora Electronics Lab: http://spins.fedoraproject.org/fel/
