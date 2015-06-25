A small parcellite tip
######################
:date: 2012-03-21 01:52
:author: ankur
:category: Tech
:tags: Fedora
:slug: a-small-parcellite-tip

`Parcellite`_ is a stripped down, basic-features-only clipboard manager
with a small memory footprint for those who like simplicity.

Of late it's been annoying me: It would copy any text that I selected to
the clipboard! I'll explain: Let us assume that I have a url on the
clipboard to be inserted into my blog post on wordpress. Now, when I
highlight the term I want to hyperlink, the clipboard gets overwritten!
So, I have *<a href="hahaha">hahaha</a>* instead of a *proper link*.
It's downright inefficient to have to select my previously copied item
from the parcellite notification (I don't like to move my hands to use
the mouse; I'm a keyboard person.). 

I had thought this to be a *bug*. Instead, this turned out to be a
*feature*. Apparently, this is how the X server manages the clipboard:
by dumping everything you highlight on to it. The rationale behind this
escapes me completely. 

To get rid of this behaviour, all you need to do is stick to the GDK
clipboard. Unselect "Use primary (Selection)" in the parcellite
preferences. Instead of **xsel -i**, use **echo "hahhaa" \|
parcellite**. 

.. _Parcellite: https://bugz.fedoraproject.org/parcellite
