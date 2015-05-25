Time and task tracking
######################
:date: 2013-12-16 01:15
:author: ankur
:category: Tech
:tags: Fedora
:slug: time-and-task-tracking

Being a research student is really tough. I mean **tough**. The most
difficult part is keeping up the **self discipline**, day after day,
week after week. As a research student, you make your own schedule, you
even make your own syllabus pretty much. I handle the syllabus part just
fine, but I struggle with maintaining a disciplined schedule. It takes a
while to get into a stable rhythm where you work according to plan and
remain focussed on the task at hand, for however long it takes. On the
other hand, it's really easy to upset said rhythm: a late night coding
spree, a night out with friends, an unexpected task that makes you
diverge from your plan for the day etc. are often sufficient to make me
sleep late and mess up the next day. Self discipline requires
commitment, and a **lot** of hard work. Luckily, I'm not alone in this
struggle. Here's a helpful post on improving self discipline:
http://www.pickthebrain.com/blog/self-discipline/. Since I spend most of
my day at a computer, I went around and looked for tools that would help
me keep focussed on my work; keep me away from distractions (yes,
Facebook is a distraction); and help me work according to the plans I
make.

Tools I use
-----------

Here is my set up. I use the simplest tools, and whatever is available
in the Fedora repositories. Some of you might find them useful.

Leechblock
^^^^^^^^^^

[caption id="attachment\_1498" align="aligncenter"
width="300"]\ |Leechblock| Leechblock[/caption]

A simple `Firefox add-on`_ that serves as negative reinforcement when
you have that urge to check Facebook, or your Gmail. I even put Fedora
sites in the list during the hours I work at my laboratory on my
research. Of course, it can be bypassed, but it reminds you that you
need to focus on your work and that it isn't the time to enter the
internet black hole yet.

Leechblock's really helped me fight what I call "**notification
slavery**\ ", where I check my mail or social networking website every
few minutes for activity.

Getting things GNOME
^^^^^^^^^^^^^^^^^^^^

[caption id="attachment\_1493" align="aligncenter"
width="300"]\ |Getting things GNOME| Getting things GNOME[/caption]

This is an amazing task manager. I used `the Gnote method outlined
here`_ in the past, but I made the move to GTG a while back and haven't
looked back at Gnote since. I've actually switched to Bijiben for note
taking too. I find using GTG to be a much better way of managing my
tasks really. You can add tasks as you plan them out, add start and due
dates, categories and tags. Your tasks are colour coded so you know when
you haven't finished one on time. A bunch of helpful plug-ins extend the
application. For instance, a bugzilla plugin lets you quickly add a bug
you need to look at later. Another plug-in lets you communicate with the
hamster time tracker (next). Of course, it's in the Fedora repositories:

`` sudo dnf install gtg ``

Hamster time tracker
^^^^^^^^^^^^^^^^^^^^

[caption id="attachment\_1506" align="aligncenter"
width="300"]\ |Hamster overview| Hamster overview[/caption]

Hamster provides an easy way of tracking your activities at work for
later introspection. GTG and Hamster work quite well together, so you
can add your tasks to GTG and track them using Hamster with a single
click. There's also a `gnome-shell extension`_ available that makes it
even easier to track your tasks.

[caption id="attachment\_1509" align="aligncenter"
width="300"]\ |Hamster GNOME shell extension| Hamster GNOME shell
extension[/caption]

``sudo dnf install hamster-time-tracker``

Evolution
^^^^^^^^^

[caption id="attachment\_1511" align="aligncenter"
width="300"]\ |Evolution calendar view| Evolution calendar
view[/caption]

I use Google Calendar to plan my day. Gnome online accounts works really
well with Google services. I keep Evolution open almost all day in
calendar mode to see what appointments I have in the day. Gnome shell
has a calendar in the top panel too. GTG is supposed to sync with
Evolution's task list too, but I haven't gotten it to work on Fedora
yet. `Peter said the back end needs to be updated to use the new GTK3
evolution data server bindings`_. I need to talk to upstream about this
(/me adds to GTG task list).

Taskjuggler
^^^^^^^^^^^

[caption id="attachment\_1514" align="aligncenter"
width="300"]\ |Taskjuggler| Taskjuggler[/caption]

All the tools listed above help me in the short term. Taskjuggler is
something I use to make long term plans. For example, I make my masters
research plan using Taskjuggler. I don't use it quite as much as project
managers do, but it does help me decide how I'll go about my work. I
used taskjuggler to plan the Fedora 20 Election cycle too. You can
generate ICS files etc. quite easily. It does have a slight learning
curve, but you can do quite a bit once you learn how to use it. Jaroslav
uses it to plan the `Fedora schedule`_ too.

`` sudo dnf install rubygem-taskjuggler ``

There's **planner** in the repositories too, which is a simpler, GUI
based too. `Here's a tutorial on how to use it.`_

``sudo dnf install planner``

Labyrinth
^^^^^^^^^

A lot of people use tools to make mind maps that help them work. I don't
use them that much, but they do come in handy when you're trying to
visualise a lot of information, like a research paper. I use labyrinth
for my work. It's a rather simple tool. More serious mind mappers might
want to look into vym or freemind.

[caption id="attachment\_1522" align="aligncenter"
width="300"]\ |Labyrinth mind mapping tool.| Labyrinth mind mapping
tool.[/caption]

| ``sudo dnf install labyrinth``
|  ``sudo dnf install freemind``
|  ``sudo dnf install vym``

Lifeograph
^^^^^^^^^^

Introspection is an important part of the self improvement process. I
also need to note down my research thoughts from time to time.
Lifeograph is a great journal application. that I use to maintain both
my research and personal journals. There are a few more journal
applications that I tried out. I've already reported my findings
`here`_.

[caption id="attachment\_1523" align="aligncenter"
width="300"]\ |Lifeograph| Lifeograph[/caption]

``sudo dnf install lifeograph``

Summary
-------

These tools are only supposed to aid one in their work. There isn't any
substitute for hard work itself. Over a period of time, everyone tends
to settle with a system that works for them. Some of these might be
worth adding to your set up. Cheers.

Edit: Added lifeograph and labyrinth.

.. _Firefox add-on: https://addons.mozilla.org/en-US/firefox/addon/leechblock/
.. _the Gnote method outlined here: http://fedoraproject.org/en/using/tutorials/gnote.html
.. _gnome-shell extension: https://extensions.gnome.org/extension/425/project-hamster-extension/
.. _Peter said the back end needs to be updated to use the new GTK3 evolution data server bindings: https://lists.fedoraproject.org/pipermail/desktop/2013-November/008476.html
.. _Fedora schedule: http://fedorapeople.org/groups/schedule/f-20/
.. _Here's a tutorial on how to use it.: http://www.redhat.com/magazine/009jul05/features/planner/
.. _here: http://ankursinha.in/wp/2013/06/23/fedora-and-journal-writing/

.. |Leechblock| image:: http://ankursinha.in/wp/wp-content/uploads/2013/12/leechblock-blog-300x148.png
   :target: http://ankursinha.in/wp/wp-content/uploads/2013/12/leechblock-blog.png
.. |Getting things GNOME| image:: http://ankursinha.in/wp/wp-content/uploads/2013/12/gtg-screenshot-blog-300x154.png
   :target: http://ankursinha.in/wp/wp-content/uploads/2013/12/gtg-screenshot-blog.png
.. |Hamster overview| image:: http://ankursinha.in/wp/wp-content/uploads/2013/12/hamster-screenshot-300x226.png
   :target: http://ankursinha.in/wp/wp-content/uploads/2013/12/hamster-screenshot.png
.. |Hamster GNOME shell extension| image:: http://ankursinha.in/wp/wp-content/uploads/2013/12/hamster-extension-blog-300x168.png
   :target: http://ankursinha.in/wp/wp-content/uploads/2013/12/hamster-extension-blog.png
.. |Evolution calendar view| image:: http://ankursinha.in/wp/wp-content/uploads/2013/12/evolution-calendar-blog-300x154.png
   :target: http://ankursinha.in/wp/wp-content/uploads/2013/12/evolution-calendar-blog.png
.. |Taskjuggler| image:: http://ankursinha.in/wp/wp-content/uploads/2013/12/taskjuggler-blog-300x193.png
   :target: http://ankursinha.in/wp/wp-content/uploads/2013/12/taskjuggler-blog.png
.. |Labyrinth mind mapping tool.| image:: http://ankursinha.in/wp/wp-content/uploads/2013/12/screenshot-labyrinth-blog-300x159.png
   :target: http://ankursinha.in/wp/wp-content/uploads/2013/12/screenshot-labyrinth-blog.png
.. |Lifeograph| image:: http://ankursinha.in/wp/wp-content/uploads/2013/12/lifeograph-blog-screenshot-300x154.png
   :target: http://ankursinha.in/wp/wp-content/uploads/2013/12/lifeograph-blog-screenshot.png
