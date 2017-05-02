A well filed software issue considerably improves the chances of the issue being fixed quicker
##############################################################################################
:date: 2017-05-01 15:22:32
:author: ankur
:category: Tech
:tags: Bugzilla, Community, Free software
:slug: a-well-filed-software-issue-considerably-improves-the-chances-of-the-issue-being-fixed-quicker
:summary: People find issues with software everyday. Some of these people will take the time to inform the developers of these issues. Some of these issues that have been reported will be looked at by developers. Some of the issues that the developers look at will contain enough information to encourage the developers to work on a fix. Ultimately, only a handful of issues will be fixed. In this post, I encourage users to report issues to developers the right way - increasing the chances of the bug being corrected. In the process, not only does one improve ones personal experience, one can help improve the experience of other users, while helping developers make their software better. The intended target here is not the developer community - they already know most all of this.

.. raw:: html

    <center>

.. image:: {filename}/images/20170501-keep-calm.png
    :alt: Keep calm and file a bug report
    :target: {filename}/images/20170501-keep-calm.png
    :width: 40%
    :class: text-center img-responsive pagination-centered

.. raw:: html

    </center>


Nowadays, software is ubiquitous - banking, healthcare, driving, communicating, mobile apps that do the most random (often unnecessary) tasks. One often runs into software issues (bugs). It could be a niggle where say, a button in the app doesn't react instantaneously, or it could be a much more critical scenario where a laptop frequently crashes.

Over the years, I've heard quite a few users complain about software that isn't working "as it should", but I've also noticed that very few of them tend to take the extra step of reporting the issue so that it may be fixed. Instead, they either continue using the application hoping that it'll be fixed in the future sometime or simply switch from alternative to alternative. Of course, bugs that affect large numbers of users are often well known and are fixed in a timely manner. On the other hand, the odd bug that affects a select set of users often remains untouched, for various reasons - usually either because it hasn't been reported, or because it isn't important enough to prioritise.

Now, before I go any further, I want to note that proprietary software is more often than not developed behind closed doors. So, I do not actively encourage users to submit bugs for proprietary software simply because if they hit a wall, I do not know where to even begin assisting them. I try to stick to free and open source software (FOSS) myself, and when I do run into an issue with proprietary applications that I use out of necessity, I drop the support folks an e-mail if contact information is readily available. However, with FOSS, the software life cycle is quite transparent. Issue trackers are accessible, so is the source-code, and so are various documents regarding planning, usage, and development. In most cases, the developers are easily accessible too. So for FOSS, I encourage people to file tickets when they run into genuine issues because it does make a difference.


Software is complex - accept that it can have bugs
---------------------------------------------------

Software issues result in exasperation. "Why can't the damn thing just work?" "How hard is it to write software that just works?" Turns, out, it is actually quite hard. Apps nowadays are rarely isolated programs. They rely on various frameworks, APIs, libraries, even hardware, to provide a service. In order for a program to "work correctly", the entire stack must function correctly, whereas a failure anywhere in the stack can result in unexpected behaviour.

As a simplified example, take a web browser. One types in the address of ones favourite social media website, and boom - all eight hundred "friends" are right there. Under the hood, though, there's a lot happening. Your web browser must use the right parts of the operating system to access the Internet, for example. Only then can it contact servers all over the world to get the right information. Nowadays, with the increased stress on privacy, the browser must use cryptography to ensure that your personal data cannot be read by others while in transit. After it has gathered the data it needs, it must again use the right bits of the operating system via various interfaces to display this information on the output device - usually the screen. There are multiple layers that are piled up one on top of the other to make the application. Most software is also developed by teams of developers, so while a single developer usually does not need to know the entire stack, but a general idea is a must. Collaborative software development also implies that different chunks of the source are written and handled by different people, and all of it plugs together to form the finished application that an end user interacts with.

Now, if writing software is hard, turns out, making software "bug-free" is even harder. In spite of all the testing (QA) that software may go through, it is extremely rare for it to be declared "bug free". Bugs and bug-fixing is part of the software development lifecycle.

Rage is never the answer
------------------------

I understand that if one pays for software, one should get the best possible user experience out of it. True. All I'm saying is that even commercial software can have bugs in it, hurling expletives towards the developers (individuals, corporations, whatever!) is unwarranted. Even if it is a fundamental issue that makes the software unusable, such an overreaction will do little to improve ones experience - all it'll do is spoil ones day. Rage is never the answer.

Now, in the case of FOSS, which users get free of all cost, I personally feel that an aggressive reaction is unnecessary and unacceptable. This is not to say that FOSS is or can be below par just because it is free of cost. I say this because FOSS is based on communities, where a lot of people contribute because they enjoy extending the freedom they have to others. A lot of people I know contribute to FOSS in the time they save from both professional and personal life. 

What interests and often confuses me here is that it isn't only end users with a lack of software development knowledge that engage in rage. It is often people that are developers themselves, often free software enthusiasts, that also partake in it. 

Check that you are using the latest stable version of the software
-------------------------------------------------------------------

Developers cannot fix bugs that they are unaware of
---------------------------------------------------

Most developers, especially developers that charge for their software, rely on good user experience to increase the number of users that buy their software. Users being troubled by bugs, of course, does not help. It stands to reason that developers, therefore, are eager to fix bugs that they are informed of. This brings up the first observation - *developers cannot fix bugs that they are unaware of!*

Check if the issue has been reported already
--------------------------------------------

Provide the right information
-----------------------------

Ask when unsure
---------------

Follow up
---------

Be nice
-------
