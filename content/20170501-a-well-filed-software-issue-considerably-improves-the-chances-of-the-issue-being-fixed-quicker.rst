A well filed software issue considerably improves the chances of the issue being fixed quicker
##############################################################################################
:date: 2017-05-17 00:22:32
:author: ankur
:category: Tech
:tags: Bugzilla, Community, Free software, Fedora
:slug: a-well-filed-software-issue-considerably-improves-the-chances-of-the-issue-being-fixed-quicker
:summary: People find issues with software everyday. Some of these people will take the time to inform the developers of these issues. Some of these issues that have been reported will be looked at by developers. Some of the issues that the developers look at will contain enough information to encourage the developers to work on a fix. Ultimately, only a handful of issues will be fixed. In this post, I encourage users to report issues to developers the right way - increasing the chances of the bug being corrected. In the process, not only does one improve one's personal experience, one can help improve the experience of other users, while helping developers make their software better. The intended target here is not the developer community - they already know most all of this.

.. raw:: html

    <center>

.. image:: {static}/images/20170501-keep-calm.png
    :alt: Keep calm and file a bug report
    :target: {static}/images/20170501-keep-calm.png
    :width: 40%
    :class: text-center img-responsive pagination-centered

.. raw:: html

    </center>

Prologue
--------

Nowadays, software is ubiquitous - banking, healthcare, driving, communicating, mobile apps that do the most random (often unnecessary) tasks. One often runs into software issues (bugs). It could be a niggle where say, a button in the app doesn't react instantaneously, or it could be a much more critical scenario where a laptop frequently crashes.

Over the years, I've heard quite a few users complain about software that isn't working "as it should", but I've also noticed that very few of them tend to take the extra step of reporting the issue so that it may be fixed. Instead, they either continue using the application hoping that it'll be fixed in the future sometime or simply switch from alternative to alternative. Of course, bugs that affect large numbers of users are often well known and are fixed in a timely manner. On the other hand, the odd bug that affects a select set of users often remains untouched, for various reasons - usually either because it hasn't been reported, or because it isn't important enough to prioritise.

Now, before I go any further, I want to note that proprietary software is more often than not developed behind closed doors. So, I do not actively encourage users to submit bugs for proprietary software simply because if they hit a wall, I do not know where to even begin assisting them. I try to stick to free and open source software (FOSS) myself, and when I do run into an issue with proprietary applications that I use out of necessity, I drop the support folks an e-mail if contact information is readily available. However, with FOSS, the software life cycle is quite transparent. Issue trackers are accessible, so is the source-code, and so are various documents regarding planning, usage, and development. In most cases, the developers are easily accessible too. So for FOSS, I encourage people to file tickets when they run into genuine issues because it does make a difference.


Software is complex - accept that it can have bugs
===================================================

Software issues result in exasperation. "Why can't the damn thing just work?" "How hard is it to write software that just works?" Turns, out, it is actually quite hard. Apps nowadays are rarely isolated programs. They rely on various frameworks, APIs, libraries, even hardware, to provide a service. In order for a program to "work correctly", the entire stack must function correctly, whereas a failure anywhere in the stack can result in unexpected behaviour.

As a simplified example, take a web browser. One types in the address of one's favourite social media website, and boom - all eight hundred "friends" are right there. Under the hood, though, there's a lot happening. Your web browser must use the right parts of the operating system to access the Internet, for example. Only then can it contact servers all over the world to get the right information. Nowadays, with the increased stress on privacy, the browser must use cryptography to ensure that one's personal data cannot be read by others while in transit. After it has gathered the data it needs, it must again use the right bits of the operating system via various interfaces to display this information on the output device - usually the screen. There are multiple layers that are piled up one on top of the other to make the application. Most software is also developed by teams of developers, so while a single developer usually does not need to know the entire stack, but a general idea is a must. Collaborative software development also implies that different chunks of the source are written and handled by different people, and all of it plugs together to form the finished application that an end user interacts with.

Now, if writing software is hard, turns out, making software "bug-free" is even harder. In spite of all the testing (QA) that software may go through, it is extremely rare for it to be declared "bug free". Bugs and bug-fixing is part of the software development lifecycle.

Note that I do not say that software must have issues. I'm just saying that given how complex contemporary software is, it's likely that it will have some issues. This does not make it acceptable for developers to release below par software, of course!

Be nice - rage is never the answer
==================================

I understand that if one pays for software, one should get the best possible user experience out of it. True. All I'm saying is that even commercial software can have bugs in it, hurling expletives towards the developers (individuals, corporations, whatever!) is unwarranted. Even if it is a fundamental issue that makes the software unusable, such an overreaction will do little to improve one's experience - all it'll do is spoil one's day. Rage is never the answer.

Now, in the case of FOSS, which users get free of all cost, I personally feel that an aggressive reaction is quite unacceptable. This is not to say that FOSS is below par just because it is free of cost. I say this because FOSS is based on communities, where a lot of people contribute because they enjoy extending the freedom they have to others. A lot of people I know contribute to FOSS in the time they save from both professional and personal life. So, if contributors can be nice enough to work in their free time to develop such great software, the least users can do is be respectful in their communications. It doesn't feel like much of an ask.

What interests and often confuses me here is that it isn't only end users with a lack of software development knowledge that engage in rage. It is often people that are developers themselves, often free software enthusiasts, that also partake in it.

In summary, it's software, it can have issues, there's no need to kick up a storm about it.

Filing bugs
-----------

On to the main bit now. Filing a bug is quite simple, but there are a few things to keep in mind that improve the chances of a bug being fixed sooner. The goal when filing a bug, of course, is to provide the right person with the right information that will help isolate the issue. For example, informing the wrong person will not help, and neither will providing the right person the wrong information. In fact, badly filed bugs make it harder for developers to fix issues, because they contribute noise that developers must then spend extra time sifting through to find the relevant information.

So, in steps, with a Fedora centric context (similar steps should be followed for all other operating systems in general):

1. Check that the latest stable version of the software is in use
==================================================================

New versions of software bring improvements and bug fixes. If one is using an old, out of date version of software, one must first update to the latest supported version. Using Windows XP, for example, which isn't supported any more is a very bad idea. So is using a version of Fedora that isn't supported anymore. So is using an older version of any application - because the newer release would contain various bugfixes and enhancements that could quite possibly have fixed the issue one is experiencing already. 

Using up to date software is extremely important - various security vulnerabilities in applications can provide a malicious user access to a lot of one's data among other things. Such bugs are often known beforehand and updated versions of software fixes these bugs. An example is the recent spyware attack that has been in the news all week, and has cost a lot of money - `WannaCry <https://en.wikipedia.org/wiki/WannaCry_ransomware_attack>`__ (Google will provide enough information to read).

If a bug that's already been fixed in the latest version is filed, developers will simply request the user to update to the latest version. So, before one files an issue, one should check if one is using the latest version. The simplest approach is to run a full system update and then re-check if the bug still persists. 

2. Provide the right information in the bug report
===================================================

For Fedora users, bugs should be reported to the `RedHat Bugzilla instance <https://redhat.bugzilla.com>`__. One is required to register, but only once, and it's very simple - only an -mail address is required so that notifications regarding updates on various bugs can be sent.

Bugzilla itself contains quite a lot of information, and may not be the most usable interface for users that are not also developers. Luckily, the Fedora infrastructure team has set up other web applications that make it very easy to get to the required Bugzilla form. I usually follow the following process:

1. First, I find the right package using the `Fedora packages application <https://apps.fedoraproject.org/packages/>`__. For example, in the screenshot below, I'm looking for the package that my web browser belongs to. It could either be Firefox, or if not, Epiphany maybe?

.. raw:: html

    <center>

.. image:: {static}/images/20170516-packages-app.png
    :alt: The Fedora packages web application
    :target: {static}/images/20170516-packages-app.png
    :width: 80%
    :class: text-center img-responsive pagination-centered

.. raw:: html

    </center>

2. From there, I go to the page for that particular package. For example, here's the `page for the Firefox browser <https://apps.fedoraproject.org/packages/firefox>`__. As the screenshot shows, this page shows various information about the package, including what bugs are currently filed against it. It also provides links to other Fedora web applications that provide other information, but I won't discuss them all here now.

.. raw:: html

    <center>

.. image:: {static}/images/20170516-packages-firefox.png
    :alt: Firefox on the Fedora packages web application
    :target: {static}/images/20170516-packages-firefox.png
    :width: 80%
    :class: text-center img-responsive pagination-centered

.. raw:: html

    </center>

Here, one can go through the list of bugs to see if something similar has already been reported. One can also use the search box to search through Bugzilla. One doesn't have to search for existing bugs, of course, one can simply file a new bug using the links at the top.

Note: commenting on an existing bug is a better way to inform the developers of an issue, since it lets them know that multiple users are experiencing it. If a duplicate bug is filed, a maintainer will close it as exactly that: a DUPLICATE. More information on Bugzilla bug statuses can be found `here <https://bugzilla.redhat.com/page.cgi?id=fields.html#bug_status>`__.

3. Clicking on "File a Fedora bug" here will take us to an empty bug report form on Bugzilla ready to be filled in! The Bugzilla maintainers already provide a template, as the screenshot shows:

.. raw:: html

    <center>

.. image:: {static}/images/20170516-bugzilla-form.png
    :alt: An empty bug report form on Bugzilla
    :target: {static}/images/20170516-bugzilla-form.png
    :width: 80%
    :class: text-center img-responsive pagination-centered

.. raw:: html

    </center>

The Bugzilla form explained
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The different fields that can be selected:

- Product: Fedora for all Fedora bugs - already set if the Fedora packages web app was used to get here.
- Component: The package name - already set if the Fedora packages web app was used to get here.
- Version: The Fedora version in use - only the current releases and rawhide (Fedora's developer preview) can be selected here.
- Severity, Hardware, and OS: can be filled or ignored. The developers usually use these if required.

- Summary: A short summary of the issue, for example "Firefox crashes on start"?

The template in the description requires a little more explanation:

.. raw:: html

    <center>

.. image:: {static}/images/20170516-bugzilla-description.png
    :alt: The description of a bug.
    :target: {static}/images/20170516-bugzilla-description.png
    :width: 80%
    :class: text-center img-responsive pagination-centered

.. raw:: html

    </center>


- Description of the problem: A clear description of the problem
- Version-Release number of selected component: once the package name is known using the Fedora packages web application, the current version that is in use can be found using the rpm command in a terminal/console:

.. code:: bash

    $ rpm -q <packagename>
    # for example
    $ rpm -q firefox
    firefox-53.0-2.fc26.x86_64

This is important information, so that the developers know exactly what version of the source code this bug is present in.

- How reproducible: This is usually one of ALWAYS/SOMETIMES.
- Steps to reproduce: What actions does the user have to do to see the issue? In as much detail as possible.
- Actual results: A description of exactly what happens - what is the issue - again, in as much detail as possible.
- Expected result: What does the user expect should happen?

The idea here is to inform the developers if the issue happens all the time, or only sometimes erratically. When developers ask if a bug can be "reproduced", what they're asking is if the issue can be ALWAYS seen when the user does certain actions. For example, if Firefox ALWAYS crashes, one would simply say:

- How reproducible: ALWAYS
- Steps to reproduce:
  - Start Firefox from applications menu
- Actual results: Firefox does not start, it crashes immediately
- Expected results: Firefox should start normally.

The more detailed the "steps to reproduce" and "actual results" are, the easier it is for developers to "debug" the issue. This is because, once they can pin point the exact problem, they can start using various tools to pin point where in the source code the problem arises from. Only then can developers think about fixing the issue.

That's quite it. If required, files can also be attached to the bug report. For example, screenshots, or screen casts, or error messages, and so on. After filling in the form, clicking the "Submit" button submits the report, and a developer will be informed.

3. Ask when unsure
====================

I often run into issues where I do not know what the right information to provide is. In such cases, I try to mention whatever I have and then request the maintainer to give me instructions on how I can provide more information to help. As an example, I recently hit a bug in the `open source nouveau Nvidia driver <https://nouveau.freedesktop.org/wiki/>`__ and `asked the developer how I could collect more information <https://bugzilla.redhat.com/show_bug.cgi?id=1439890#c12>`__. Sure enough, the `developer was kind enough to give me some hints <https://bugzilla.redhat.com/show_bug.cgi?id=1439890#c13>`__, and I managed to collect more information to help out. (I even learned a new kernel debugging tool in the process - `netconsole <https://www.kernel.org/doc/Documentation/networking/netconsole.txt>`__. Do you know what it is?)

There is absolutely nothing wrong with asking for help - anywhere in the community. When in doubt, ask!

4. Follow up
=============

After the bug has been filed, the developer will look at the information that has been provided and begin to diagnose the issue. This is an iterative process. The developer may ask for more information, or may provide new versions of the application to test. In all of these cases, the developer will comment on the Bugzilla ticket, and everyone concerned with the bug will receive an e-mail notification. Following up on a bug report is important. It helps developers identify issues quickly, and of course, it helps them confirm fixes too. 


Conclusion: take away from it all
----------------------------------

In short:

- it's software and it can have issues.
- cribbing, whining, blowing one's top off doesn't achieve much - not helping anyone.
- update your system regularly - it's important.
- file a bug - you're helping!
- file a bug the right way - you're helping even more!
- follow up after you file the bug to aid the developer fix the issue.
- rejoice with better, safer software!


Added reading
-------------

Some resources related to bug reporting in Fedora:

- `How to file a bug report <https://fedoraproject.org/wiki/How_to_file_a_bug_report>`__
- `Bug and feature requests <https://fedoraproject.org/wiki/Bugs_and_feature_requests>`__
- `ABRT: automatic bug reporting tool <https://fedoraproject.org/wiki/Automatic_Bug_Reporting_Tool>`__
- `StackTraces <https://fedoraproject.org/wiki/StackTraces>`__
- `QA:Updates Testing <https://fedoraproject.org/wiki/QA:Updates_Testing>`__


Feedback is always welcome. Please comment below, or contact me via e-mail.
