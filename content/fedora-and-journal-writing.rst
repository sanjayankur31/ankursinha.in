Fedora and journal writing
##########################
:date: 2013-06-23 22:53
:author: ankur
:category: Tech
:tags: Fedora
:slug: fedora-and-journal-writing

I've kept a journal for a long time. Initially, I used to write in a
diary. Since I started grad school and got my laptop though, I've been
writing it in text files. It works for me in general, with a
YYYYMMDD.txt file name. I've since started by masters by research course
and I need to keep another journal, this time a research journal. While
I could use another folder and follow the same method, I'd like my
research journal to be a lot more easily referable than my personal
journal in the future. I've been looking for sometime for a journal
software. Here I'll share my findings. If you too want to keep a
journal, you have a few choices:

#. The first is the **`RedNoteBook`_**. It's a pretty good personal
   journal. A clean, simple interface, good for daily writing. It works
   well. The one thing it missed was encryption. You can add tags to
   your diary entries too.
#. Another is **`Almanah`_**. While it does support encryption, it's too
   simple for my taste. It lacks tags and other features, which is what
   I was looking for, moving away from text files in the first place. It
   does have quite a few features lined up, but at the current time, I
   cannot use it.
#. The last one, and the one I finally decided to use is
   **`lifeograph`_**. Lifeograph let's you organize your posts. It keeps
   your writing encrypted. Best of all, it lets you maintain multiple
   profiles, therefore multiple independent journals. This means, I can
   use lifeograph to maintain both my personal and research journals.
   The other two applications did not do this, and while I could use
   tags to differentiate my two diaries, nothing's better than having
   two completely separate journals!

I've tried all of these because they're available in the Fedora
repositories. You can simply run:

``sudo yum install rednotebook almanah lifeograph``

to install them and pick one that suits you. A few others that aren't in
the Fedora repositories but seem to be good are `journaler`_\ (which is
open source now, but appears to be for Mac only) and `robojournal`_.
Robojournal looks impressive, uses MYSQL as a back end. I haven't given
it a shot though, since lifeograph fits my needs. Using MYSQL might be
slight overkill for a novice user? Upstream says support for sqlite etc.
will be added in the future, which would certainly make it more
useful.(\ `It's up for review`_)

I haven't run into any others yet. I'm going to stick to lifeograph for
the foreseeable future. Happy writing!

.. _RedNoteBook: http://rednotebook.sourceforge.net
.. _Almanah: https://live.gnome.org/Almanah_Diary
.. _lifeograph: http://lifeograph.wikidot.com/start
.. _journaler: https://github.com/phildow/Journler
.. _robojournal: http://sourceforge.net/projects/robojournal/
.. _It's up for review: https://bugzilla.redhat.com/show_bug.cgi?id=967659
