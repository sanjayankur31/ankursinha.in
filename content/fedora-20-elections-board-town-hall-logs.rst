Fedora 20 Elections: Board town hall logs
#########################################
:date: 2013-06-14 17:30
:author: ankur
:category: Tech
:tags: Fedora
:slug: fedora-20-elections-board-town-hall-logs

| /\* For the .log.html \*/
|  pre { /\*line-height: 125%;\*/
|  white-space: pre-wrap; }
|  body { background: #f0f0f0; }

| body .tm { color: #007020 } /\* time \*/
|  body .nk { color: #062873; font-weight: bold } /\* nick, regular \*/
|  body .nka { color: #007020; font-weight: bold } /\* action nick \*/
|  body .ac { color: #00A000 } /\* action line \*/
|  body .hi { color: #4070a0 } /\* hilights \*/
|  /\* Things to make particular MeetBot commands stick out \*/
|  body .topic { color: #007020; font-weight: bold }
|  body .topicline { color: #000080; font-weight: bold }
|  body .cmd { color: #007020; font-weight: bold }
|  body .cmdline { font-weight: bold }

::

    19:00:31 <mdomsch> #startmeeting Fedora Project Board Elections Town Hall
    19:00:31 <zodbot> Meeting started Thu Jun 13 19:00:31 2013 UTC.  The chair is mdomsch. Information about MeetBot at http://wiki.debian.org/MeetBot.
    19:00:31 <zodbot> Useful Commands: #action #agreed #halp #info #idea #link #topic.
    19:00:51 <mdomsch> Welcome to the Fedora Board Town Hall for this election cycle.  I?m your moderator, Matt Domsch, former board member.  Everyone (including candidates) may pose questions in #fedora-townhall-public.  I will take the questions and pose them to the candidates, assigning a number to each question to keep answers collated.  Candidates, please answer in parallel, completing your answer with ?EOF?.
    19:01:13 <mdomsch> We have five candidates for three Board seats, each will serve for one year.  With us are Josh Boyer (jwb), Matthew Garrett (mjg59), Ha?kel Gu?mar (number80), and Dan Mashal (dan408).  Eric Christensen (sparks) sends his regrets as he has another obligation at this hour.  $DAYJOB schedule conflicts are to be expected for all Fedora volunteers, including Board members, please do not hold this against any candidate.
    19:01:44 <mdomsch> While people are getting their questions ready, I will open asking for introductions.
    19:01:52 <mdomsch> Q1.  Please start with a brief introduction of yourself, what your involvement in Fedora has been to date, and what you think makes you an excellent candidate for the Board.
    19:03:32 <mjg59> I'm Matthew Garrett, and I've been working on Fedora for just over 5 years. I've mostly been involved in kernel and hardware support, working on the lower levels of the software stack, but I have some small contributions to desktop code as well.
    19:03:35 <jwb> Josh Boyer, contributor since around FC4, FESCo member for a rather long time, previous Board member.  I come from an engineering background and have served on multiple Fedora committees and teams, so I have a wide array of experience with most things Fedora.  I do, however, suck at art and GUI stuff, so i haven't been on the design team ;)
    19:04:32 <number80> I've been a Fedora packager for 7 years, ambassador for 6 (founding member of the French Team, etc.). I'm a serial patcher on many FOSS projects.
    19:05:26 <mjg59> More recently I've been working on things like UEFI Secure Boot support, which has involved a lot of negotiation, collaboration and political work with lawyers, developers and managers at various companies. Finding a solution that left people as happy as possible was a significant job, and I think that the work involved there maps quite nicely to the skills required to be an effective board member.
    19:05:38 <dan408> My name is Dan Mashal (fas: vicodan) (irc nick: dan408). I have been a system administrator for over 10 years for various companies. I have been Fedora for as long as I remember and love it. I maintain MATE and co-Cinnamon desktops, the new MATE-Compiz spin introduced in Fedora 19, active member of the QA and Ambassador teams, active package reviewer.
    19:06:46 <dan408> I also pick up orphaned packages and am working on Enlightenment (which was completely rewritten) for Fedora 20. I do many package reviews and also end user IRC support in #fedora as well.
    19:06:46 <mdomsch> thank you all
    19:07:04 <mdomsch> #topic Questions and Answers
    19:07:37 <mdomsch> Q2: <mitr> What should the board decide with respect to the user base?  (i.e. both what is the question to be decided, and what is your answer?)
    19:07:48 <mdomsch> Let me elaborate briefly...
    19:08:16 <mdomsch> #link https://lists.fedoraproject.org/pipermail/advisory-board/2013-April/011968.html
    19:08:16 <mdomsch> is Robyn?s outline for a discussion on User Base.
    19:08:40 <jwb> that... isn't quite fair.  if we haven't read that yet, we certainly won't have time now
    19:08:40 <mdomsch> and this question has been ongoing since at least 2007 if not before
    19:09:15 <mdomsch> jwb: just framing the question in terms of history, not really content
    19:09:37 <jwb> ok
    19:09:53 <mjg59> The fundamental question is whether Fedora is intended to produce a product
    19:10:14 <jwb> so.  i think focus on user base is a double edged sword.  if we're trying to make a product, then it's great to know who you're making it for.  if we're trying to make a platform, then it's less relevant
    19:10:14 <number80> or a platform ? :)
    19:10:34 <jwb> i view Fedora more as a platform that other people make products (spins, etc) from
    19:10:40 <mjg59> We can look at various other aspects of it. Should Fedora be a community? Should Fedora be a place where people can engage in worthwhile technical experimentation? Should it be easy to build things on top of Fedora?
    19:11:16 <mjg59> But if we compare Fedora to Ubuntu, we find that Ubuntu has, if anything, managed these things better than we have
    19:11:22 <jwb> i was on the Board when we came up with the current target user.  it was helpful to have a direction and someone to aim marketing at.  i'm not sure it's really done anything for the technical side of the distro
    19:11:23 <number80> My point of view is that the board is mostly here to set common values/shared vision and a guarantee that contributors may do as they please
    19:11:49 <mjg59> Because without a product, we lack the incentive for initial involvement
    19:12:06 <mjg59> People come to the Ubuntu community because they run Ubuntu. They don't run Ubuntu because they want to join the Ubuntu community.
    19:12:56 <mjg59> So I think the questions that are being asked right now are the wrong questions to be asking. A community is worthless without users to serve. We don't gain users unless we concentrate on producing a product.
    19:13:13 <dan408> I'm have read that and just skimmed through it and am just going to offer a completely fresh opinion here. Lots of things have changed since then. For example the feature process has changed. I believe that the board's goal is to make sure end users and contributors are happy from all walks of life. That means the board should over see all aspects of Fedora. That is the definition of
    19:13:13 <dan408> a traditional board. For example, what are the most common questions in #fedora? What are the most common packaging questions for new packagers? How can we make creating your first package and getting reviewed/sponsored easier? The board should look at all SIGs and groups and see if there is any help they can provide to those groups to help them operate better. The board should also
    19:13:13 <dan408> improve communication distro wide between different said groups and SIGs.
    19:13:26 <jwb> mjg59, so... the question becomes is a "desktop distribution" the correct product?
    19:13:33 <jwb> for focus purposes
    19:13:33 <mjg59> jwb: And the answer is clearly yes
    19:14:00 <dan408> jwb mjg59 i disagree.
    19:14:03 <number80> I agree with mjg59 that we need a flagship product in order to promote the platform and our community but i believe that is the role of the contributors (and ultimately the fesco) to decide what shape should take that product
    19:14:18 <jwb> mjg59, i believe we've been doing that for a while now and as you've said, Ubuntu is winning by larger margins there
    19:14:21 <mjg59> We don't have the community we could have, but we *do* have a community. And the majority of those community members use Fedora as a desktop operating system.
    19:14:34 <mjg59> jwb: Yeah, because we've consistently produced a product that works less well.
    19:15:15 <dan408> Fedora is not a "desktop distribution. It is a LINUX distribution. It offers multiple choices of desktops. It gives you the choice of having no desktop at all. You can run Fedora as a server, firewall, router, desktop, build machine, anything. That's the beauty of it.
    19:15:24 <dan408> "
    19:15:30 <jwb> mjg59, so the current community has failed?
    19:15:49 <mjg59> jwb: No, I think the leadership has failed
    19:16:00 <dan408> mjg59: what would change?
    19:16:05 <dan408> what would *you* change?
    19:16:17 <mjg59> jwb: See the board discussion around Secure Boot, for instance. The board was entirely ok with the idea of releasing a distribution that normal people would be unable to install on new computers.
    19:16:48 <dan408> mjg59: And how was that fixed?
    19:17:01 <mjg59> dan408: We did it anyway
    19:17:15 <dan408> mjg59: You shouldn't "do it anyway"
    19:17:20 <mjg59> dan408: What?
    19:17:22 <mjg59> No
    19:17:27 <dan408> I think in that case the board was uninformed
    19:17:34 <mjg59> We informed the board
    19:17:36 <number80> I don't think that technical issues should be decided at the board level, unless it violates Fedora Foundations or technical boards failed to resolve them
    19:17:46 <jwb> "doing it anyway" is essentially the community actually working as it should
    19:17:53 <jwb> so i don't think that specific case was a bad thing
    19:17:59 <mjg59> Yeah. I think the right thing happened. But I think it happened for the wrong reasons.
    19:18:10 <mjg59> There should have been leadership from the board driving us towards a solution
    19:18:13 <mjg59> But there wasn't
    19:18:17 <dan408> number80: I believe that technical issues should be decided in the board if it possible that it could frustrate end users.
    19:18:50 <dan408> For example going to back to mjg59 and secure boot, that affected me negatively. I compiled a kernel manually on a UEFI  / secureboot system and I completely hosed my system.
    19:18:51 <jwb> dan408, the Board is not a technical body.  they rely on the people doing the work to explain the issues
    19:19:03 <number80> dan408: we're a contributors driven distro, the board may represent the users, but decisions should be taken by the contributors
    19:19:32 <mjg59> The board shouldn't make technical decisions, but it should be providing a framework to target those technical decisions
    19:19:41 <number80> dan408 is right that the board may express an opinion if it affects end users
    19:19:42 <dan408> And the kernel maintainers view was "Sorry we're not giving you our key." So the end result was actually a failure on your part. That taught me the lesson of dont install fedora with uefi and secureboot because I wont be able to compile a custom kernel.
    19:20:02 <jwb> dan408, you clearly can.  just create your own key
    19:20:12 <jwb> pretty sure i even wrote a post on how to do it
    19:20:14 <dan408> I'm not going through the extra trouble just for that.
    19:20:31 <jwb> you're already building a kernel.  creating a key takes just a few min more.
    19:20:40 <dan408> jwb: From the pristine linux source code?
    19:20:43 <dan408> not the SRPM?
    19:20:56 <jwb> no
    19:20:59 <dan408> exactly.
    19:21:02 <jwb> but the tools are all in fedora
    19:21:07 <mdomsch> we're getting far afield from the original question - user base, and how would you resolve the outstanding question of "what should our users be"
    19:21:18 <dan408> Our users should be EVERYONE.
    19:21:31 <dan408> that is not even a question.
    19:21:32 <mjg59> No
    19:21:43 <mjg59> Our users should be everyone who would benefit from using Fedora rather than something else
    19:22:01 <dan408> Everyone could benefit from a free operating system.
    19:22:08 <dan408> So I fail to see your logic.
    19:22:28 <mjg59> Debian users have a free operating system
    19:22:39 <mdomsch> moving on...
    19:22:44 <jwb> (and gentoo, and ...)
    19:22:51 * dan408 moves on.
    19:22:51 <jwb> mdomsch, please
    19:22:52 <mdomsch> Q2: <j_dulaney> What do you forsee the Board actually $doing?
    19:22:57 <jwb> ha!
    19:23:05 <jwb> so before i was on the board, i asked that a lot
    19:23:11 <number80> you mean in the future ?
    19:23:56 <jwb> having been on the Board, it can be difficult to summarize exactly what happens in meeting logs and such
    19:24:01 <dan408> Response to Q2: What do I see the board actually doing? More of the same. What has changed since the last election? Not much.
    19:24:22 <mjg59> What do I forsee the board actually doing, or what would I like to see the board actually doing?
    19:24:23 <number80> Redefine shared goals, and make it easier to contribute to Fedora (and with much less flame)
    19:24:33 <dan408> mjg59: actually doing
    19:25:00 <mjg59> What I forsee is a bunch of meetings with results that depend on what the board numbers are motivated by
    19:25:10 <mjg59> I don't think it's a terribly meaningful question
    19:25:28 * dan408 reminds everyone of http://fedoraproject.org/wiki/Board
    19:25:33 <number80> I think of the board as a servant leadership, we have to remove impediments that bother our contributors and help to make it rocks
    19:25:34 <mdomsch> (for the record, that was Q3)
    19:25:38 <mjg59> What I would *like* to see the board do is make decisions that it knows may alienate some people
    19:25:39 <jwb> the job of the Board is to ensure the fedora distro is guided by the 4 foundations.  since we don't really deviate from that, it's hard to show where they've had to step in
    19:25:57 <jwb> plus they deal with trademark issues, and a few other things that aren't discussed in public
    19:26:07 <jwb> to be honest, must of it is tedious work
    19:26:10 <jwb> er, much
    19:26:15 <mdomsch> Q4: <jsmith> Much of the Board's work involves balancing the wants of a few people against the goals and aspirations of the larger project. What is your view with regards to this balance, and how to find that balance when conflicts arise?
    19:26:17 <number80> jwb: that's an impediment
    19:26:25 <jwb> number80, which?
    19:26:28 <dan408> mjg59: I'm sorry again I misunderstand? You want the board to make decisions that alienate people?
    19:26:43 <number80> jwb: dealing with trademark and patents issues
    19:26:56 <dan408> mdomsch: what happened to Q3?
    19:27:02 <mjg59> dan408: I want the board to be willing to make decisions that alienate people if the alternative is not to make decisions at all
    19:27:07 <jwb> number80, sure?  but it's the reality we live in
    19:27:40 <dan408> mjg59: Okay I can agree with that but I believe that the board should try to not alienate people, yes tough decisions must be made for the greater good. I agree.
    19:27:44 <number80> jwb: yeah, the board may relieve that from our contributor, ungrateful job but very appreciated
    19:28:09 <mdomsch> dan408 I misnumbered and asked 2 twice
    19:28:13 <mjg59> q4: What goals and aspirations of the larger project?
    19:28:44 <jwb> q4 is throwing me a bit.  is there an example of this kind of situation coming up?
    19:29:09 <number80> about jsmith Q, that requires diplomacy and a lot of listenning, and we need something like a Zen of the Fedora contributor
    19:29:31 <number80> contributors may have been a bit less nicer to each other these last year
    19:30:28 <number80> We want the board to act as an arbiter not as UN-like forces
    19:30:54 <mjg59> mdomsch: ?
    19:31:03 <mjg59> mdomsch: Maybe move on to the next question?
    19:31:04 <mdomsch> I think jsmith is afk for a bit
    19:31:09 <mdomsch> next question coming up
    19:31:12 <dan408> Answer to Q4: This relates to the current discussion. As I said the board's primary goal to keep Fedora moving forward and prevent it from taking any steps back. To clarify, I personally believe the board shouldn't alienate ANYONE. In fact, I as a contributor I have found to be quite welcoming and I enjoy attending the public board meetings. I appreciated their unanimous approval of
    19:31:12 <dan408> my spin it meant a lot that I Didn't have to go through a lot of questioning. It was just approved because all the processes were followed and everyone saw the benefit of having the MATE-Compiz spin included with Fedora.
    19:31:37 <mdomsch> Q5: <misc> Quite recently, a controversy erupted regarding a poster competition linked to Fedora and Mozilla erupted. Provided you know what was this about, how would have you handled the case as part of the board ?
    19:32:06 <dan408> mdomsch: Can you please provide a link to said controversy?
    19:32:12 <number80> +1
    19:32:25 <jwb> i've not seen said eruption
    19:32:58 <dan408> Is this in reference to this? http://www.wfs-india.org/p/poster-competition-womens-and-lgbt-issues
    19:34:09 <number80> probably
    19:34:13 <dan408> number80 jwb according to EvilBob the question was inreference to the above link
    19:35:05 <jwb> so the jist here is someone decided to give away Fedora flash drives as a prize?
    19:35:22 <mjg59> Well as it currently stands, that page seems entirely appropriate
    19:35:26 <mjg59> So is there some further history?
    19:35:38 <number80> I see no conflict with our Foundations
    19:35:41 <dan408> In my opinion, The board hopefully did not approve this. Fedora should not be getting involved in social or politicial issues whatsoever.
    19:35:49 <jwb> what?
    19:36:00 <jwb> how is "Free Software" neither social nor political?
    19:36:02 <mjg59> Free software is inherently social and political
    19:36:14 <mjg59> It's fundamentally about changing power dynamics
    19:36:19 <dan408> Not necessarily.
    19:36:26 <mjg59> It's an effective mechanism for social change
    19:36:38 <number80> I understand that it might not please some of our community but it's about FOSS promotion
    19:36:49 <dan408> I agree with that, but this is in regards to sexual preference and gender issues
    19:37:08 <jwb> at any rate, i don't believe the Board has any recourse here if it is an unmodified Fedora release.
    19:37:21 <number80> And it's not linked to controversial matters like racism, women rights denial
    19:37:35 <mjg59> Oh what
    19:37:37 <dan408> Do not get me wrong, I believe that everyone should have the freedom for sexual preference and equal rights for women
    19:37:55 <mjg59> You can't divorce these things
    19:38:11 <mjg59> Free software is about personal freedom
    19:38:28 <mjg59> It's inherently the same thing as sexual freedom
    19:38:39 <mdomsch> Q6: <notting> Various studies have shown Fedora's active contributor base to be shrinking. Do you feel that this is a problem,, and if so, how would you combat it?
    19:38:40 <mjg59> You can't be in favour of one and against the other
    19:38:43 <dan408> mjg59: That is out of the scope of what Fedora needs to worry about.
    19:38:48 <mjg59> dan408: Oh no, it's really not
    19:39:02 <number80> Q6: yes it is, it's an HUGE one
    19:39:15 <mjg59> q6: Why would anyone contribute to Fedora?
    19:39:17 <jwb> ignoring that, i'm not sure usage of a Fedora prize is implying Fedora sponsorship or promotion of the idea
    19:39:44 <number80> I feel that Fedora community is a lot less friendlier than before, and that we have no more ass-kicking goals
    19:39:45 <jwb> it can be construed that way, but the Board could ask the person to reword it or something along those lines
    19:39:48 <mjg59> Ubuntu was an attractive thing for people to involve themselves with
    19:40:16 <mjg59> Because it meant they were associated with something that got press and which they saw actual real people running
    19:40:21 <number80> We need to work on new contributors mentoring and make them feel welcomed
    19:40:46 <mjg59> And now that's less attractive because it seems like contributing to Ubuntu is just helping Canonical make money
    19:40:46 <dan408> Answer to Q6: It's not just the contributor base that's shrinking. It's the user base too. Do I feel that this is a problem? Yes. It is currently pretty hard to combat. There are decisions that are currently made with out community approval. See Anaconda in Fedora 18. See Gnome 3 in Fedora 15.
    19:40:47 <number80> and help the community to set new ambitious goals
    19:41:11 <mjg59> But it's always seemed that way for Fedora
    19:41:18 <number80> dan408: I disagree about the GNOME3 part
    19:41:29 <dan408> number80: Tell that to every MATE and Cinnamon user.
    19:41:31 <mjg59> The public perception is that Fedora is just a vehicle for getting work done on RHEL
    19:41:42 <mdomsch> I would conjecture that the declining contributor base, and the stagnent to declining user base, are related.  Would you agree or disagree, and why?
    19:41:49 <number80> dan408: there are more users of GNOME3 than both MATE and Cinnamon
    19:41:52 <dan408> mjg59: Currently that's not a perception. It's a fact.
    19:42:05 <mjg59> And by concentrating on the Fedora community, we do nothing to dissuade people from believing that
    19:42:09 <dan408> number80: MATE is brand new, and was forked out of necessity.
    19:42:47 <number80> mjg59: I think that RH CTO has helped to spread that myth, that's why we need a strong board to voice our community about these matters
    19:42:47 <mjg59> "Come work on Fedora! You'll get to hang out with some cool people, but the only people who'll actually run what you produce will be paying Red Hat for it!"
    19:42:50 <dan408> number80: Gnome is how old? MATE 1.6 was just released in April 2013. The entire project is barely over a year old.
    19:43:15 <jwb> mjg59, so you're saying we need to grow a user base before we grow a contributor base
    19:43:18 <mjg59> jwb: Yes
    19:43:23 <jwb> clearly related, sure
    19:43:27 <dan408> jwb: absolutely
    19:43:28 <mjg59> And we don't grow a user base unless we actually concentrate on producing a product
    19:43:35 <number80> dan408: i disagree about that, but it's not the right place to discuss this (i would gladly share a beer with you to discuss about that later :) )
    19:43:36 <dan408> every contributor is a user too.
    19:43:42 <dan408> number80: sure
    19:44:19 <dan408> last point in regards to G3, almost all of #Fedora end user IRC support do not run Gnome 3.
    19:44:55 <number80> I think that the board should also spend more time communicating about the project
    19:45:07 <mjg59> So, what should the board do:
    19:45:14 <mjg59> 1) Define a specific Fedora product
    19:45:19 <mjg59> 2) Market that
    19:45:22 <dan408> in regards to Anaconda. It is currently the buggiest "package" in Fedora, and what caused Fedora 18 to miss its schedule. It is currently what 95% of the F19 final blocker bugs are opened on.
    19:45:24 <mjg59> 3) Profit
    19:45:41 <mjg59> dan408: The Anaconda changes went through the entire community approval process
    19:45:42 <number80> mjg59: s/define/help the community to define/
    19:45:45 <dan408> mjg59: Fedora is not for profit.
    19:45:52 <number80> the board is no dictatorship
    19:46:04 <jwb> Profit in the growth sense, not monetary i would assume
    19:46:07 <mjg59> number80: The community will not be guided to a decision. We've seen that.
    19:46:40 <number80> mjg59: I remember a wonderful FPL (who works at Amazon actually) who reached that ;)
    19:46:45 <mdomsch> Q7 is related: <gholms> Do you have any thoughts on Fedora outreach into new communities of interest?  What communities come to mind?  How can Fedora become involved?
    19:47:11 <jwb> i'm still not sure focusing on a single product is the right solution.  companies diversify for growth reasons
    19:47:32 <mjg59> jwb: Companies don't try to sell fifteen different things into the same market
    19:47:41 <jwb> mjg59, true.  they go after different markets
    19:47:49 <jwb> but they don't do it with a _single_ product
    19:47:51 <number80> Most Fedora contributors favor the platform over the product, so we need to be supportive of the SIG
    19:48:11 <dan408> Answer to Q7: We need to out reach to more universities and expand the Red Hat internship program. If "new blood" is what we're after, then let's get "new blood", literally. At the colleges.
    19:48:26 <mjg59> Hey, I actually agree with dan408 for once
    19:48:32 <number80> +1
    19:48:34 <mjg59> College outreach is important
    19:48:48 <mjg59> But, again, why would people at college contribute to Fedora rather than anything else?
    19:48:49 <dan408> Continued answer to Q7: We need to reach out to Comp Sci departments and ask them why they are not running Fedora.
    19:49:03 <mjg59> And let's not limit ourselves to CS
    19:49:07 <jwb> i actually think college is one level too high
    19:49:08 <dan408> We need to go to college campuses and pass out multi live media
    19:49:17 <number80> we should build training materials and work in hand with ambassadors on that issue
    19:49:27 <jwb> local high schools are a much more impressionable and relevant target
    19:49:30 <dan408> We need to actually get off our computers and talk to people about Fedora!
    19:49:44 <dan408> This is what being an Ambassador is all about!
    19:50:03 <number80> I think that the ARM gang have impressive tools for that goal ;)
    19:50:03 <jwb> they're strapped for cash, students like doing "different" things, and it ties in with all kinds of other out-reach programs
    19:50:04 <dan408> The problem with the Ambassador program is that it is focused on events, not the real life community.
    19:50:14 <mjg59> So going back to Ubuntu again, one of the massively attractive aspects of its early marketing was that it was about humanity. It appealed to people's desires for social change.
    19:50:52 <number80> dan408: right, but as an ambassador, most of my job has been to build my local community (town, region, nation levels)
    19:51:01 <dan408> When I first joined the Ambassador program my first question was WHY are we spending time and effort preaching Fedora at Linux conferences? It's like going to CES and sell your brand of TV
    19:51:06 <mjg59> Talking about Fedora as software doesn't help a great deal there
    19:51:27 <dan408> number80: different regions in the Ambassador program face different isues and different approaches to tackling them.
    19:51:40 <number80> dan408: right
    19:52:05 <mdomsch> Q8: <pjones> How do you see the relationship between the board and FESCo? (and what distinguishes their responsibilities and authority)
    19:52:17 <number80> mjg59: do you suggest that we work with other projects or companies to create new use ? (ie: Fedora Phone ?)
    19:52:39 <mjg59> number80: What would Fedora Phone even be?
    19:52:39 <dan408> mjg59: You don't talk about Fedora as software. You go to a comp sci major and tell him why he should run Fedora (i.e. newest versions of perl, python, knowing Fedora helps them know RHEL which is what is being widely used in the corporate world)
    19:53:20 <mjg59> dan408: And then they tell you that they're doing all their software development on OS X because that's what all their Heroku howtos talk about
    19:53:43 <number80> mjg59: that could be an awesome goal if we find a partner, but that would be the job of the community to decide which road to take
    19:53:59 <jwb> q8: i view the relationship as very weak.  that isn't a bad thing.  FESCo is charged with making sure the distribution is technically viable, stable, and competent.  the Board theoretically provides oversight, but that is rarely needed
    19:54:05 <mjg59> FESCo make technical decisions. The decisions should align with the board's guidance about the goals of the project.
    19:54:08 <number80> Q8: Fesco is the ultimate authority for technical issues, period
    19:54:16 <dan408> Answer to Q8: I see FESCo as one of THE MOST important groups in Fedora and the board and FESCo should be actively involved with each other. People have suggested to me to run for FESCo. I do not feel qualified because I do not feel I am on the same technical level as the current members for FESCo.
    19:55:03 <number80> The board should only intervene for legal/patent/trademark issues or voice the larger community in some topics (but the decision should be taken by the fesco)
    19:55:40 <mdomsch> one last question before we're out of time
    19:55:42 <dan408> FESCo can dissect extremely technical issues and explain them to the board when needed if and when a board decision is needed.
    19:55:52 <mdomsch> Q9: <kalev> The stable Fedora releases are currently receiving a lot of updates; some of them are bug fixes, some are feature updates.  Do you feel the current situation is appropriate?  Should we strive to do more / less feature updates for stable Fedora releases?
    19:56:22 <jwb> this question comes up every election, for every group
    19:56:26 <mjg59> So, for instance, if the board (with whatever project involvement) had decided that the priority for stable Fedora releases should be stability rather than feature updates, and Fesco voted to remove all karma requirements from stable updates, I think that would be a case where the board should discuss Fesco's decisions
    19:56:28 <number80> we have a stable policy and a QA team for that stuff, but our QA team is man-lacking
    19:56:57 <number80> mjg59: discuss but not take the decision
    19:57:07 <jwb> i think we need to look at delivering updates differently.  clearly telling people "less updates" hasn't worked for the past 3 years
    19:57:45 <number80> the board represents the whole community, the fesco the contributors, I believe that "he who does, should decide"
    19:57:48 <mjg59> The argument is that having feature updates in stable releases gives us an advantage over Ubuntu because people can get the latest version of code
    19:57:54 <dan408> Answer to Q9: It depends. For MATE Desktop it was absolutely appropriate. I pushed MATE Desktop 1.6 to Fedora 17/18. I did not notice many bugs being filed in regards to this. Users got an updated MATE Desktop without having to upgrade Fedora. It keeps the branches of the MATE Desktop packages in sync.
    19:58:16 <dan408> For things like the Kernel you quite obviously are on a slippery slope there.
    19:58:16 <mjg59> But what actually happens in Ubuntu is that someone sets up a PPA with newer versions and people get to make that choice themselves
    19:58:42 <number80> mjg59: maybe we should give more attention to copr
    19:58:43 <mjg59> So I don't think feature updates provide a compelling reason for people to run Fedora
    19:59:03 <jwb> fwiw, the kernel team does try and limit update frequency as a release gets older
    19:59:09 <dan408> mjg59: ACtually it does.
    19:59:19 <mjg59> number80: Yup. I actually think that should be a priority. It'd provide a technical mechanism for relieving community tension.
    19:59:26 <dan408> mjg59: MATE Desktop is still not officially included in Ubuntu or Debian.
    19:59:35 <dan408> it is officially included in Fedora
    19:59:49 <dan408> This has brought Gnome 3 abandoners of Fedora back.
    20:00:06 <dan408> believe it or not, it's the truth.
    20:00:17 <mjg59> (citation needed)
    20:00:23 <jwb> great.  that doesn't mean it's because of UPDATES
    20:00:36 <jwb> that's content
    20:00:50 <number80> I think that stability vs features brings (again) another question: platform or product ?
    20:01:12 <mjg59> People are only interested in a building a platform to the extent that it allows them to build their own product
    20:01:15 <number80> if we had a single product, stability would obviously come first
    20:01:21 <mdomsch> number80: we will let the next board decide that question then :-)
    20:01:24 <mdomsch> #topic Wrapup
    20:01:40 <mdomsch> with that, thank you to all our candidates for your time today
    20:01:45 <jwb> lots of overlap in the questions
    20:01:48 <dan408> Thank you mdomsch for hosting.
    20:02:20 <mdomsch> and to the Fedora members who posted great questions and spurred on lively debate.  I hope the answers here will help enlighten your choice for voting.
    20:02:33 <number80> thank mdomsch for hosting, FranciscoD for organizing, my fellow candidates and our awesome community
    20:02:45 <mjg59> Yeah, thanks to everyone who put effort into this
    20:03:03 <mdomsch> #endmeeting

