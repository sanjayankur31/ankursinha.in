Fedora Classroom: Command Line 101: report
##########################################
:date: 2017-08-10 23:03:24
:author: ankur
:category: Tech
:tags: Bash, Blog, Community, Linux, Planet, Fedora
:slug: fedora-classroom-command-line-101-report
:summary: I taught a `Fedora classroom`_ session today - "Command Line 101" - where I introduced the command line and demonstrated how useful the command line is. This is a quick summary of the session.

We've gotten the `Fedora classroom`_ sessions going again. After two really good ones, I taught the `third one <https://fedoramagazine.org/fedora-classroom-session-3/>`__ today - a beginners session to the command line. Unlike the previous ones that used video platforms, I decided that the IRC_ was best suited to this session, even more so because I wanted it to be a hands-on session. It went off pretty well. Here are a few notes. Links to the logs are at the bottom of this post.

Some metrics
-------------

- Length: 2 hours (was planned to be an hour, but we quickly realised that it wouldn't be enough!)
- Attendees: 29 - a few of us had FAS usernames too (so we shared cookies!)
- About 800 sentences were spoken (I spoke about half of these, of course)


Summary
-------

I quite enjoyed it, but then I enjoy tinkering with the command line anyway. A few folks stuck around for the full two hours, so that does indicate that they found the session somewhat useful. I'd put up a `gist here with a tentative agenda <https://gist.github.com/sanjayankur31/f40070c6925e8885394d2dd750ae4cb8>`__. We didn't manage to go more than half way through it, though. We:

- did a quick introduction to what a shell is
- learned how to get help using local information - using the man pages
- quickly saw the difference between absolute and relative paths, and also learned about :code:`..` and :code:`.`
- went on to look at some more basic commands/built-ins and their switches/flags/options: :code:`ls, apropos, clear, cd, pwd, which, alias, rm, tree, mkdir, wget, rmdir, rm, fpaste, wc, head, tail, more, less, cat, tac, grep, sort, uniq`
- used these commands to download a copy of `"The tragedy of Julius Caesar" from Project Gutenberg <http://www.gutenberg.org/cache/epub/1120/pg1120.txt>`__, and then extracted some information from it. For example, we obtained how many times Caesar was mentioned in the text. For a more advanced task we also obtained how many times Caesar, Brutus, Cassius, and Casca were each mentioned using a single set of commands. This required the use of :code:`grep, sort, uniq, wc` in different combinations using input-output redirection (pipes in this case). At no point did we use a text editor, and we stuck to using local man pages.

Takeaways
---------

I hope that this rather quick session gave the participants some idea of how the shell can be used for lots of tasks. I also hoped to show them that there's a lot of information available on the system itself that a user can refer to.

I learned a few things myself. I learned that an hour is too short for a proper online session, for example. My supposition that demonstrating commands using tasks would make the session more appealing seems to have been correct too. Only, maybe next time I'll pick a more contemporary text?

For the next session, I'll try and cover slightly more advanced topics, such as tests, loops, maybe even a bit of awk. We shall see.

Feedback is always welcome
--------------------------

If you had attended the session, or have gone through the logs and have some feedback, please get in touch. You can use the Fedora classroom channels:

- `mailing list <mailto:classroom@lists.fedoraproject.org>`__
- #fedora-classroom on Freenode `IRC channel <http://webchat.freenode.net/?channels=%23fedora-classroom>`__

You can even comment on this blog post, and of course, you can give me feedback privately. I'm also looking to make a list of tasks that I can use in future sessions - tasks that would be useful, fun, and that would also require some command line tricks - such that they would demonstrate the power of the command line. So, if you have your pet command line tricks/aliases, please do get in touch.

I'm FranciscoD on quite a few Fedora IRC channels, and I can be reached via e-mail on my Fedora address at ankursinha AT fedoraproject DOT org. All suggestions, comments, criticism is most welcome.

More instructors needed!
-------------------------

The classroom sessions are going rather well, but `we still need more help <https://fedoraproject.org/wiki/Classroom#Help_wanted>`__. We need more people helping with logistics, and of course, if we are to continue these sessions every week, we need more instructors! If there's anything at all you think is worth a classroom session, please get in touch with the team on the `Fedora classroom mailing list <mailto:classroom@lists.fedoraproject.org>`__. A log of all past sessions - whether on IRC_ or on a video platform are maintained on the wiki page `here <https://fedoraproject.org/wiki/Classroom#Previous_Sessions>`__ for everyone to peruse at their convenience.

Logs
----

* `HTML logs <https://meetbot.fedoraproject.org/fedora-classroom/2017-08-10/%22fedora_classroom_-_command_line_101%22.2017-08-10-13.00.log.html>`__
* `Text minutes <https://meetbot.fedoraproject.org/fedora-classroom/2017-08-10/%22fedora_classroom_-_command_line_101%22.2017-08-10-13.00.txt>`__
* `HTML minutes <https://meetbot.fedoraproject.org/fedora-classroom/2017-08-10/%22fedora_classroom_-_command_line_101%22.2017-08-10-13.00.html>`__


.. _Fedora classroom: https://fedoraproject.org/wiki/Classroom
.. _IRC: https://en.wikipedia.org/wiki/Internet_Relay_Chat
