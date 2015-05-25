transmission-2.11-2 for Fedora 14
#################################
:date: 2010-11-10 01:31
:author: ankur
:category: Other
:tags: Fedora
:slug: transmission-2-11-2-for-fedora-14

Transmission-2.12 is going to be released in a few days. However, it's
not going to be a general bugfix release. There is going to be removal
of some features in that one. Since we didn't want to push the 2.12
release to F14 users, we went "cherry picking" and patched the 2.11
release with some important bug fixes. It's been pushed to testing and
awaits your feedback.

Fixes:

#. Added patches as per
   https://bugzilla.redhat.com/show_bug.cgi?id=649545#c9
#. https://trac.transmissionbt.com/ticket/3629
#. https://trac.transmissionbt.com/ticket/3639
#. https://trac.transmissionbt.com/ticket/3666
#. https://trac.transmissionbt.com/ticket/3644

Link to bodhi update is :
https://admin.fedoraproject.org/updates/transmission-2.11-2.fc14
