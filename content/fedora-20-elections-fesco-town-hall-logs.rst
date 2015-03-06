Fedora 20 elections: FESCo town hall logs
#########################################
:date: 2013-06-11 04:21
:author: ankur
:category: Tech
:tags: Fedora
:slug: fedora-20-elections-fesco-town-hall-logs

** The meetbot logs are archived at: http://meetbot.fedoraproject.org/fedora-townhall/2013-06-10/.** Just
pasting them here to save you that one click :)

I'm most grateful to everyone who made it, the candidates, and the
community members who asked them questions. Have a good read:

.. code-block:: irc

    17:06:17 <FranciscoD> #startmeeting Fedora 20: FESCo townhall
    17:06:17 <zodbot> Meeting started Mon Jun 10 17:06:17 2013 UTC.  The chair is FranciscoD. Information about MeetBot at http://wiki.debian.org/MeetBot.
    17:06:17 <zodbot> Useful Commands: #action #agreed #halp #info #idea #link #topic.
    17:06:41 <FranciscoD> #meetingname FESCo townhall
    17:06:41 <zodbot> The meeting name has been set to 'fesco_townhall'
    17:06:50 * FranciscoD pokes zodbot
    17:07:11 <nirik> it's rejoining the 120+ channels it's on, so it will be slow to respond for a bit.
    17:07:23 <FranciscoD> As long as it gets logs.
    17:07:42 <FranciscoD> #topic Reminders and introductions.
    17:08:03 <FranciscoD> Hello everyone. Thank you for joining us at the FESCo townhall tonight.
    17:08:20 <nirik> it needs ops to change the topic. ;)
    17:08:28 <FranciscoD> nirik: restart?
    17:08:43 <nirik> no, it's on track now.
    17:08:49 <nirik> it just didn't change the topic.
    17:08:51 <nirik> yet
    17:09:00 <FranciscoD> Proceeding then.
    17:09:25 <FranciscoD> All questions go to #fedora-townhall-public. I'll pass them on to the candidates who will answer them in here.
    17:09:36 <FranciscoD> We'll start with introductions.
    17:09:50 <FranciscoD> Candidates, whenever you're ready, please tell us a little about yourself :)
    17:10:27 <mattdm> Hi all. I'm Matthew Miller; I've been involved in Fedora for a long time, most recently working on cloud images and related things.
    17:10:28 <kalev> Hi, I am Kalev Lember. Fedora contributor for over 4 years, package maintainer / provenpackager / packager sponsor.
    17:10:31 <kalev> I'm involved with GNOME and have been doing a lot of GNOME package updates in Fedora recently.
    17:10:38 <jwb> Josh Boyer.  Current FESCo member and one of the Fedora kernel maintainers.
    17:10:54 <pjones> Hi!  As you no doubt know from the past, and from the brief blurb that's on the website, I'm Peter Jones, and I've been working on Fedora since its inception (and RHL before that).
    17:11:08 <pjones> I'm also a current FESCo member, and I help maintain various things in our software stack.
    17:11:10 <nirik> Hi. I'm Kevin Fenzi, For the last two years I've been employed by Red Hat to lead the Fedora Infrastructure team. I've been involved in Fedora since 2005 (the Fedora Extras days) and on FESCo since it's been around. I see Fedora continuing to grow into new and exciting spaces (Cloud, ARM) and wish to help the community to sustainably spread Fedora's values and foundations to new areas while improv
    17:11:10 <nirik> ing things in areas we already are.
    17:11:52 <t8m> I am Tomáš Mráz. I've been FESCo member for two years and I work in the Red Hat as engineer - developer and maintainer primarily focused on security related packages - crypto, PAM, etc.
    17:12:44 <notting> Hi. I'm Bill Nottingham. As an amorphous alien once said, "I have always been here". Current FESCo member, does random vaguely-leadership-y things for Fedora (and with my Red Hat hat on, RHEL).
    17:13:05 * FranciscoD counts 7 introductions :)
    17:13:12 <FranciscoD> #topic questions and answers
    17:13:24 <FranciscoD> (Please note that candidates can ask questions too)
    17:14:11 <FranciscoD> First question comes from josef: i feel like fedora is starting to get relatively stable, it seems to me like theres very little for Fesco to do on a regular basis, what do you guys see as our challenges moving forward and Fescos responsiblity in helping address those challenges?
    17:14:59 <FranciscoD> Please answer whenever you're ready. No specific order need be followed.
    17:15:05 <jwb> stable how?
    17:15:24 <jwb> stable from a release perspective, or stable from a "not much changing" perspective, or?
    17:15:33 <pjones> josef: I think there's still a lot of progress to be made to improve Fedora, such as the replacement of the (much loathed by all) Feature process, which is going to be a key issue in this coming term.
    17:16:10 <nirik> 1. I think there is still things to do, but I also appreciate that Fedora is getting more stable. I think our challenges are to grow new areas and be relevent in them (arm, cloud, new languages/rapid devel), while keeping our core values. I think we can continue to make it easier to contribute, I think we can work on fixing more process.
    17:16:11 <FranciscoD> joseph clarifies: "not much changing, its been rather boring on the list recently, not may flame wars related to big changes"
    17:16:21 <pjones> josef: likewise, broadening our support for new platforms, such as the oh-so-nebulous "cloud" and ARM, are going to be things that will need FESCo's help to ensure they work well for our users.
    17:16:39 <t8m> I don't really think that Fedora is getting to be relatively stable in the near future. I think there will be really disrupting changes ahead and also the implementation of the new processes (new changes process and the proposed Fedora revamp) will probably require pretty serious involvement of FESCo
    17:16:49 <jwb> frankly, i think we need a break from the big changes.  i'm happy f19 has been comparatively quiet
    17:16:54 <mattdm> Yeah. Although there are obviously still improvements in each area and there's always room for surprising innovation, the basic issues of a Linux-based OS distribution are largely solved. This is becoming a boring area -- not necessarily in a bad way, but the excitement is "moving up the stack". If we want to remain relevant as a project, we need to address those areas of excitement.
    17:17:22 <jwb> however, going forward i don't expect that to last.  i think FESCo's role there is to facilitate making those big changes in the distro more feasible.  better communication, better planning, etc
    17:17:26 <pjones> josef: I think the reason the discussions are about process is that we need those processes to work better, in order to ensure that discussions about the content can truly be fruitful.
    17:18:12 <nirik> I think we have had improved stability in the last few years... I think it's at least somewhat related to the updates policy changes and I think it's a good thing.
    17:18:27 <kalev> One big change that is coming up is the ARM addition as the primary architecture, and FESCo would have a rather large role to ensure it goes smoothly.
    17:18:31 <notting> josef: I think the biggest challenge to Fedora remains growing our community into new areas, and finding our niche there, whether that be as a cloud platform, the various different (and even contradictory) things people try to do on ARM, and so on. Part of FESCo's role is to allow and foster that growth. But at some point Fedora as a whole likely needs to decide what it's trying to do... "everything and nothing" has its downsides as well.
    17:18:38 <FranciscoD> Could I request you folks to just EOF when you're done, so I know when to ask the next question? Thanks.
    17:18:55 <pjones> EOF
    17:19:01 <mattdm> EOF
    17:19:02 <kalev> EOF
    17:19:02 <jwb> EOF
    17:19:03 <nirik> EOF
    17:19:20 <t8m> EOF
    17:20:18 * FranciscoD waits for notting to finish
    17:20:26 <notting> EOF
    17:20:34 <FranciscoD> Thanks.
    17:20:50 <FranciscoD> nirik asks: what do candidates think of arm in general or as it pertains to Fedora. Is it ready to be a primary arch? What areas of it should we focus on?
    17:21:42 <notting> nirik: you're asking yourself questions?
    17:21:44 <notting> anyway
    17:21:49 <jwb> i think the ARM team has done a lot of work over the f19 release to get ready for primary arch.  from everything i've seen, it's getting very close to an experience like primary
    17:22:28 <jwb> i'm curious to see if that holds out and they have an installable via anaconda release, and then how their build infrastructure compares
    17:22:32 <nirik> 2. (disclaimer: I asked this) I think arm will/should be a primary arch soon. I think focus will of course be up to those that do the work on it, but I think it's going to be a lot more common in the datacenter, and we should make sure there's a good server story there. Also, misc developer devices so we get more interest/contibutors are good. Phones and tables are the least interesting area IMHO.
    17:22:43 <nirik> notting: Was worried we didn't have enough. ;)
    17:22:44 <pjones> Well nirik, I don't think it's ready yet, for a couple of reasons.  Right now one of the restrictions that FESCo has placed on that is that we've effectively got to raise the bar for arm to that of a primary arch - in terms of bug response, security response, and infrastructure, for at least one fedora release before we officially promote them.  As it stands, we're getting close to that, but we're not near it yet.
    17:22:46 <t8m> ARM is not my area of expertise but I'd say if some new hardware improves the build times we could/should try to make it primary arch. It would be nice to see some non-x86 architecture as a primary arch after some time.
    17:22:50 <jwb> if those match up, i think they stand a chance of becoming primary.
    17:23:26 <nirik> pjones: they released beta the same day as primary. ;) but sure, there are still things to discuss/look at.
    17:23:42 <pjones> At the same time, there are still some big changes coming for ARM that aren't there yet - the move to "Aarch64" (64-bit armv8 with a terrible name.), for example, will require changes that aren't all in place yet.
    17:23:59 <pjones> so I think we're still a ways off, but the arm team is making good progress.
    17:24:18 <pjones> nirik: yeah, they've also reasonably gotten a new kernel maintainer as well, or so I hear.
    17:24:18 <jwb> pjones, i view AArch64 as another arch
    17:24:32 <jwb> the work done thus far is clearly for ARMv7
    17:24:35 <nirik> it is another arch
    17:24:41 <nirik> and doesn't really exist yet. ;)
    17:24:42 <mattdm> As I understand it, it's very close to being ready to be a primary arch. I think we may need some redefinition of the release criteria and what it means to be a primary arch. While ARM-on-notebooks is an interesting case, it's not necessarily the most interesting area for ARM. (Instead: hyperscale servers). We may need to look at changing what we require in order to be primary in order to accommodate
    17:24:44 <mattdm> ARM -- and we *should* do that.
    17:24:45 <pjones> jwb: well, the arm team hasn't brought that up with fesco yet, so it's probably too soon to hell how we'll interpret that, but sure, that's a strong possibility.
    17:25:05 <jwb> nirik, i meant "it won't automatically be primary, even if 32-bit ARM is"
    17:25:12 <notting> nirik: ARM is interesting in that it's the first new processor since x86_64 to be really heavily gaining in marketshare, so it opens up new markets and areas to Fedora. It seems like it's getting close to primary, although it also seems to be suffering from a crisis of identity in terms of markets. there are both many people espousing its wonders as a server platform, and many desktop spins being created. (saw gnome-shell on a N4 last week...)
    17:25:13 <nirik> jwb: right.
    17:25:46 * FranciscoD will wait for EOFs before moving to the next question
    17:25:51 <t8m> EOF
    17:25:59 <kalev> EOF
    17:26:00 <jwb> EOF
    17:26:01 <pjones> EOF
    17:26:10 <mattdm> EOF
    17:26:15 <notting> nirik: much like Fedora as a whole, it's likely about finding a good way to allow the community to take that in the directions they want. but it's certainly far closer to primary in terms of having a signifiant userbase than any other secondary so far.
    17:26:16 <notting> EOF
    17:26:29 <nirik> EOF
    17:26:46 <FranciscoD> number80 asks: What do they think we should to do improve our reviewing process ? (tickets piling up, inactive sponsors, etc.)
    17:27:42 <jwb> i have no good suggestions for this.  the current thinking is probably tied in with Fedora Badges or other forms of recognition for a job well done
    17:27:52 <nirik> This has always been a difficult issue. I'm not sure there's too much we can do unless we go to the point of asking for someone to do a review to get a approval, and I don't think thats a really good step.
    17:28:31 <nirik> Badges could help I guess... at least recognize those people who are doing good in reviews/sponsoring.
    17:28:46 <jwb> the few consistent reviewers we have seem to be internally motivated here, but finding others like that is hard.  coming up with some kind of reward might entice some
    17:28:49 <jwb> EFO
    17:28:50 <jwb> er, EOF
    17:28:50 <mattdm> I would like to see us reduce the amount of Fedora which needs extra-strict review.
    17:28:56 <kalev> jwb's idea to go with Fedora Badges could make a lot of sense, yeah. Having some recognition for reviews done could help a lot.
    17:29:01 <pjones> I think this is actually a really difficult question, especially because as you become more involved with Fedora, you have less and less time to review packages.  That said, reviewing seems to go best when reviewers and packagers are discussing things directly on e.g. irc, in real time, rather than just on the bz; this is also true of finding reviewers.  Swaps and "hey, who can help with this" in real time really help.
    17:29:06 <notting> number80: not to throw technology at the problem, but... automate! find ways to streamline and automate the process & procedures. (attempting to) throw people at the backlog hasn't really worked.  But also, it may be worth in the future thinking of a world where strict review criteria is applied to packages that are critical/important (via their placement in the software stacks we ship), and places on the edges that may not have the same full req
    17:29:06 <notting> uirements.
    17:29:06 <notting> EOF
    17:29:14 <pjones> So there are probably things we can do, which we haven't done, to facilitate that sort of interaction.
    17:29:15 <nirik> I think our quality is one of our best advantages, I don't think we should slack requirements.
    17:29:17 <nirik> EOF
    17:29:33 <t8m> That's a tough question. I think that the review process thanks to the fedora-review package is automate enough now. Perhaps there could be some way of "marketplace" for advertising interesting packages that weren't reviewed yet.
    17:29:37 <mattdm> I would like to see reviewers get more reward. The trade-for-review process can be a big barrier to contributors.
    17:29:37 <t8m> EOF
    17:30:32 <kalev> I am actually a bit concerned about the automated fedora-review process -- many packagers just run this and don't look at the package in question at all, missing important issues.
    17:30:36 <kalev> EOF
    17:30:38 <pjones> mattdm: that's not a bad idea; we've traditionally had the issue that we don't really have any way to *provide* such a reward to people.  But things like GNOME Bounties have been somewhat successful (or so I hear?) so that sort of model could help here as well.
    17:30:51 <pjones> EOF
    17:31:08 <mattdm> If we determine that the review process is a really big bottleneck, that it needs to stay, and we've automated what we can, we may need to make that argument to, um, $sponsoringcompany that we actually need people paid specifically to do this.
    17:31:26 <mattdm> (And if we can't make that argument effectively, we need to do some more reflection.)
    17:31:45 <mattdm> EOF
    17:31:48 <pjones> yep.
    17:32:07 <kalev> We might want to take a look at how other projects do reviews. In the WebKit project, for instance, reviews are rarely a bottleneck.
    17:32:17 <kalev> EOF
    17:32:30 <FranciscoD> number80 asks: what do candidate think about which technical road Fedora should take: Fedora as a Platform or Fedora as a Product ? Fedora as a Product == Fedora as an end user distro/ Fedora as a Platform == Fedora geared to be a based for potentially multiple use/distro
    17:32:51 <jwb> i've always viewed Fedora as a platform
    17:33:12 <jwb> we just happen to have one spin that gets more attention than the rest as a way to promote that platform
    17:33:22 <mattdm> I am very firmly in the Fedora as a Platform camp. I'd like us to _enable_ Fedora as a Product but it shouldn't be the center.
    17:33:25 <nirik> I think it is a platform and parts of fedora happen to make products out of parts of it.
    17:33:30 <t8m> I'm definitely for the Fedora as a Platform - and I think we are currently much more near this than Fedora as a Product.
    17:33:31 <pjones> I've always viewed it as a platform, using that criteria, though there's no reason the "product" version can't be an output of that.  But in a very real way, that depends entirely on what the most people put in to it, and right now most people put in things for very specific spins.
    17:33:37 <jwb> if that needs to change to something people are using more of instead of a desktop, i'm ok with that.  but i don't believe they are mutually exclusive
    17:33:49 <jwb> EOF
    17:33:50 <mattdm> violent agreement all around!
    17:33:52 <mattdm> EOF
    17:33:58 <t8m> EOF
    17:34:07 <notting> number80: i believe that Fedora needs to be a platform. However, for it to be successful as a platform, people need to use it, which requires Products of some sort around that.
    17:34:08 <notting> EOF
    17:34:14 <nirik> I think things like the cloud images are a great new product based on the platform. ;)
    17:34:16 <nirik> EOF
    17:34:30 <pjones> So, you know, if you'd prefer for something other than desktop to be the primary output of our platform, you need to work on other outputs, and convince others to do so or to put resources behind them.
    17:34:32 <pjones> EOF
    17:35:17 <kalev> I believe both are important. We should have a strong primary product, but also make sure other areas get attention.
    17:36:04 * FranciscoD will wait for kalev to EOF
    17:36:12 <kalev> Having focus is important, otherwise we'll get pulled in too many directions. But that doesn't mean Fedora should be _one product only_, no.
    17:36:15 <kalev> EOF
    17:36:25 <FranciscoD> josef asks: we've had a few discussions about overriding what developers are doing in certain cases (usually anaconda) when it goes against what seems like is good for the community, what is your stance on making that sort of decision, should fesco ever override developers work?  should it never?  is there a balance to be struck and if so how?
    17:37:10 <nirik> I think we can and have done so in the past, but I think we should try very very hard to avoid doing so.
    17:37:25 <pjones> josef: there's certainly a balance to be struck, and it's very dependent on the specifics of the situation.
    17:37:28 <kalev> Technical issues almost always have a (good) technical solution. I see FESCo as a body that makes sure the relevant people talk to each other, and help guide them in the right direction.
    17:37:40 <pjones> but nirik is right - it is a last resort, and not a tool to be used lightly.
    17:37:42 <nirik> Such overrides should be only in very rare cases where we cannot convince developers that the change is needed for the distro as a whole.
    17:37:50 <t8m> I don't know whether the current situation is ideal but I think it is fairly near it - that means we will definitely need to sometimes override developers decisions but it should be very very uncommon case.
    17:37:51 <nirik> EOF
    17:37:53 <jwb> the only way to do that is either to convince upstream to change, or to fork (micro-fork, whatever you want to call it).  sometimes a fork is ok, like with grub1.  most of the time it isn't, so i think FESCo should focus on communication, planning, and conflict resolution of technical issues
    17:37:58 <jwb> EOF
    17:38:06 <kalev> EOF
    17:38:07 <t8m> EOF
    17:38:48 <pjones> in the case of Anaconda, the issue, and one of the reasons we didn't do much real overriding, was that it was largely FESCo's problem, not anaconda's - the schedule (which FESCo approved) for F18 simply could not work with what FESCo agreed would go in the distro.
    17:38:49 <notting> josef: I don't rule out that FESCo may do that, but I really really really would prefer to avoid doing so. If we can't come to consensus, there are problems.
    17:38:50 <notting> EOF
    17:39:10 <pjones> EOF
    17:39:10 <mattdm> In order to be either a strong product or a strong platform, as opposed to a collection of random packages lumped together, we need to have an overall goal. If an indivdual package's own goals don't align, and we need functionality that package provides, we need to find a solution that works for the whole.
    17:39:52 <mattdm> That may in involve asking the packagers or developers to consider our needs in a way that's different from that project's own goals.
    17:40:19 <mattdm> We can't (usually) _force_ anyone to do anything, but hopefully we can come to the right understanding.
    17:40:43 <mattdm> EOF
    17:40:48 <FranciscoD> gholms asks Remixes like the raspberry pi's can sometimes have platform-specifix enhancements that, for instance, configure hardware right in anaconda.  Is there a place for thwse on a primary arch in Fedora proper?  Can/should we make one? He further clarifies: "I'm wondering about how identical people feel different platforms should be."
    17:41:44 <mattdm> I'm pretty sure we should get the hardware specifics right. (Anaconda pulls in packages needed for specific storage support based on the hardware, for example.)
    17:42:14 <pjones> I think in a lot of cases that's something that should be determined by developers - not just the developers of the platform, but them *in coordination* with the developers of the other parts of fedora.  So in your example, FESCo should be doing something pretty hands off - mostly ensuring that anaconda developers and the people who see a need for that sort of platform change are talking, and share a common plan.
    17:42:29 <nirik> well, the pi is a weird case. ;) It's never likely to be primary in fedora. I'd say submit patches to anaconda and if they are willing to carry them great, but if not, I guess they would need to carry their own fork. I don't see FESCo forcing anaconda to maintain something thats not a fully suported platform.
    17:42:40 <kalev> If the downstreams like the Raspberry Pi remix want to upstream their platform-specific Anaconda improvements, I believe they should have the chance. As long as they follow the Anaconda code standards and other requirements the developers set.
    17:42:46 <mattdm> I think the different primary platforms should be as similar as possible, but we certainly don't need all _spins_ to be identical, and there may be a spin dedicated to a specific platform.
    17:43:03 <mattdm> The cloud image is another example of a spin with a specific focus like that.
    17:43:08 <pjones> mattdm: I think his question may reflect on, for example, hyperscale really needing whole-image installs, and anaconda not doing that.  That said, right now anaconda can install to images, so you'd really want a separate /deployment/ mechanism /after/ anaconda.
    17:43:12 <jwb> i don't think the pi is a great example here, but i think spins and/or remixes should be free to tune their images as they see fit for their device or audience.
    17:43:29 <t8m> In my opinion the different platforms do not have to be completely identical, although the more they are identical the more the non-primary arch maintainers have less work on the maintenance so it is in their interest to make it so they are identical as much as possible.
    17:43:49 <kalev> That's the whole point of remixes -- to offer something that differs from the primary offerings.
    17:44:37 <t8m> EOF
    17:44:38 <mattdm> pjones: yeah. And I think using anaconda to generate those images (rather than somewhat-kludgy chroot-based non-anaconda tools) is the right way forward. We get the right kind of convergence there.
    17:44:39 <kalev> EOF
    17:44:40 <nirik> EOF
    17:44:41 <mattdm> EOF
    17:45:28 <notting> Anaconda does have new addon functionality - I could see spins using that functionality somewhere. But that would be a bit unusual.
    17:45:51 <pjones> But if we're really talking about raspi - no, I don't necessarily think that hardware specific things on some remixes is a terrible thing, but they still need to be done in coordination with the anaconda developers.  We are trying to make a coherent experience, so it should differ only where it's necessary to get the user a working system.
    17:46:05 <pjones> EOF
    17:46:06 <mattdm> +1 pjones
    17:46:17 <notting> I would agree that they shouldn't be done in a vacuum though, so at least people are aware of what is going on in these spaces.
    17:46:17 <notting> EOF
    17:47:13 <jwb> oh, EOF
    17:47:16 <kalev> I agree with notting. Remix developers should be in contact with upstream (Fedora) and try to ensure that fixes also go to upstream.
    17:47:21 <FranciscoD> :)
    17:47:22 <kalev> EOF
    17:47:29 <FranciscoD> mitr asks: any thoughts moving away from primary focus on packaging (as demonstrated by the packaging policy and review guidelines being the largest document) and looking every at every package individually to component integration and looking at quality of the resulting distribution?
    17:47:58 <jwb> that seems largely up to QA
    17:48:10 <mattdm> I think that's an excellent approach.
    17:48:32 <jwb> i also don't think "length of document" denotes a primary focus
    17:48:39 <jwb> it just means someone actually wrote stuff down
    17:48:40 * nirik isn't sure he understands the question
    17:48:54 <mattdm> We do need individual component testing, but integration testing is important too.
    17:49:13 <pjones> I think we've been trying to make a whole, coherent distribution for a long, long time now.  It's harder than it sounds, especially since Fedora has a very "all things to all people" approach.
    17:49:14 <mattdm> it's my understanding that this is something the QA team is working on
    17:49:26 <t8m> I think this could make sense to make Fedora more of an integrated OS than a "Linux distribution" however I'd see problems largely on the available resources and especially available developers and QA for that.
    17:49:28 <pjones> but jwb's point is also very true.
    17:49:44 <jwb> the QA team needs more people.  at the moment, they aren't scaling past installation testing
    17:49:51 <jwb> so... consider this a plug for them
    17:49:57 <nirik> I think we definitely could use better testing plans and such, but we should keep packaging guidelines as I think they ensure we don't make silly mistakes from initial import
    17:50:14 <mattdm> yeah. this is an area where we need an investment of resources.
    17:50:28 <notting> I can see a tighter integration that could come by defining what the integrated core *is* and working off of that. But we've had a definite philosophy in Fedora of allowing people to scratch their itches, which does lead to prioritizing packaging-the-world (or at least a large subset of it).
    17:50:35 <pjones> mattdm: It's hard to think of any area that doesn't need more resources, but that means you're right about that ;)
    17:50:44 <mattdm> lol
    17:50:53 <kalev> Fedora has a very large number of packages and I believe it is important to have guidelines that demonstrate best practices for packaging. Having clear guidelines also makes it easier for new people to get involved.
    17:51:00 <notting> If we do want to prioritize Fedora-as-a-Platform (FaaP? that sounds bad.), that would imply more concentration on integration rather than package additions.
    17:51:00 <notting> EOF
    17:51:07 <jwb> EOF
    17:51:14 <pjones> EOF
    17:51:18 <mattdm> EOF
    17:51:24 <t8m> EOF
    17:51:30 <nirik> I agree we could look at trying to integrate more from the packager/developer side, instead of having a fence...
    17:51:44 <nirik> I'd look forward to reading such plans. ;)
    17:51:47 <nirik> EOF
    17:52:16 <kalev> I would also like to encourage more developer to run rawhide to make sure people run the code they are working on.
    17:52:19 <kalev> EOF
    17:52:38 <FranciscoD> josef asks: some features require work from lots of different groups, such as btrfs as the default fs.  for these big distro changing features should fesco be taking a more proactive and hands on approach to making sure all of the various teams are playing together nicely so one group doesn't get blocked waiting on another one, or should they just all fight it out and when its ready its ready?
    17:52:44 <mattdm> (Part of the integration testing plan involves aways-functional-rawhide, so this is all good together.)
    17:53:16 <jwb> i think the new Change process was implemented for exactly this reason
    17:53:32 <jwb> however, it doesn't currently address changes that require multiple releases to land
    17:53:34 <nirik> I don't think there should be any "fight". ;) They should talk to all involved teams and if they feel there's a blockage or issue, please do bring that to fesco to try and help with. Otherwise I'd much rather see a "here, we are ready, and all the other teams say so too" approach.
    17:53:41 <pjones> josef: well, fundamentally, fesco is almost always a reactionary body.  it's hard to break that mold, though some members have been doing a great job with the Changes process.
    17:54:06 <jwb> so i think the developers need to be upfront about realistic expectations for a Change, and then FESCo can proactively test and communicate with all parties across the required timeframe
    17:54:18 <nirik> EOF
    17:54:20 <jwb> i don't think there should be a fight.  just better communication
    17:54:21 <jwb> EOF
    17:54:23 <mattdm> FESCO can help facilitate conversation when there are blockers. I think the development of the change process has been great and is obviously helpful.
    17:54:35 <kalev> Big features like brtfs is exactly where FESCo's technical leadership is needed. FESCo should be the body that asks other groups to work on supporting new features, e.g. brtfs.
    17:54:43 <pjones> That said, there's no reason the "just in time" approach has to be /fighting/.  In principle, with a change like btrfs-as-default, the best thing is for somebody involved to be in charge of the change, and for that person to come to fesco if there's another group with whom communicate is difficult.
    17:54:54 <kalev> FESCo doesn't really have a lot of resources to direct, but it can direct other people's attention, guide them.
    17:55:07 <mattdm> Yeah. All that. :)
    17:55:09 <mattdm> EOF
    17:55:11 <kalev> EOF
    17:55:20 <pjones> that person doesn't need to be on fesco, and in the past often hasn't been (but not always) - and I think that model has worked pretty well for us.
    17:55:27 <t8m> FESCo can help teams to communicate better - and the Changes process should help with that but anyway it will still be the developers duty to talk with each other on the changes needed.
    17:55:28 <notting> FESCo should certainly be helping to ensure that Changes are well publicized, and that the proper teams are informed and communicating so that they can work together, and help to pull the people involved together. There are limits to what FESCo can do in terms of remediation, or facilitating the *work* on the change itself, though.
    17:55:30 <t8m> EOF
    17:55:33 <notting> EOF
    17:55:43 <pjones> EOF
    17:56:13 <FranciscoD> gholms asks: What do you believe that you bring to the table to help make F20 the best it can be?
    17:56:33 * FranciscoD notes that this will probably be our last question before he requests candidates to make their concluding remarks.
    17:57:29 <jwb> experience and continuity.  as hard as we try to make things clear and well documented, there is some inherent tribal knowledge to everything and i've been doing this a while
    17:57:48 <pjones> Well, this pretty much the intro paragraph from the nominations and introductions from earlier - more than a decade of experience putting together various linux distros, doing engineering work across the whole stack, as well as several years on FESCo helping Fedora be the best that it can.
    17:58:05 <nirik> A desire to help parts of fedora get things done as well as knowledge to help make sure we do that in a sustainable way.
    17:58:06 <jwb> beyond that, just technical awareness of multiple areas helps.
    17:58:07 <jwb> EOF
    17:58:10 <nirik> EOF
    17:58:18 <pjones> EOF
    17:58:22 <notting> gholms: I would have to say my experience doing this for a while, and breadth of knowledge across the platform.
    17:58:22 <notting> EOF
    17:58:56 <t8m> I'd say that working on my area of expertise and helping with reasonable decisions in FESCo if I am elected.
    17:58:57 <t8m> EOF
    17:59:55 <mattdm> I haven't been in the fedora leadership before, but I have been involved for a long time and have kept an eye on things across the entire distribution. I'm very interested in seeing Fedora succeed in new areas like cloud and ARM, and want to look at how we can adapt while remaining true to our values.
    18:00:18 <kalev> I believe FESCo should be diverse to ensure technical expertise in various different areas
    18:00:28 <mattdm> (that sounds kind of politiciany. but I mean it.)
    18:01:04 <pjones> mattdm: the "fesco outsider" tack, eh?
    18:01:24 <jwb> i'm good with that too.  new blood is important
    18:01:58 * FranciscoD waits for 2 more EOFs before requesting concluding remarks
    18:02:02 <mattdm> heh. something like that.
    18:02:08 <mattdm> EOF
    18:02:17 <kalev> EOF
    18:02:31 <FranciscoD> #topic Concluding remarks
    18:02:42 <FranciscoD> I'm glad all the candidates could make it here.
    18:02:55 <pjones> Vote for me!
    18:03:07 <pjones> (I'm actually leaving for another meeting right now...)
    18:03:11 <FranciscoD> Could you all please make some concluding remarks (like that one ;)) and we'll call it a successful townhall :)
    18:03:45 <notting> Vote for me! Or don't! But vote.
    18:03:48 <jwb> i think all the candidates here are solid.  if you want to vote for me, great.  but most importantly, VOTE
    18:03:48 <nirik> Thanks for the questions. If anyone has any further, feel free to drop me an email or catch me in #fedora-devel. Please do vote. :)
    18:03:48 <t8m> Please vote and if you vote for me - even better. :)
    18:04:06 <kalev> A lot of different people here representing different areas -- I am happy to see this and I hope if I get elected, I will be able diversify the group with my own technical insight.
    18:04:08 <mattdm> I *do* thing Fedora will need to make some big changes to remain relevant over the next decade. I don't have all the answers for what those changes look like, but I'm very interested in listening to everyone's ideas and working with the whole community to build the future Fedora.
    18:05:34 * FranciscoD waits for final EOFs
    18:05:46 <notting> (eof)
    18:05:49 <nirik> EOF
    18:05:56 <mattdm> And now I need to go pick up my children from school. (Waves the flag, patriotic music plays.)
    18:05:58 <mattdm> EOF
    18:06:00 <jwb> EOF
    18:06:01 <t8m> EOF
    18:06:16 <kalev> EOF
    18:07:21 <FranciscoD> notting pjones kalev mattdm jwb nirik t8m Thank you so much for making it to the town hall. I wish you all the best for the final voting phase :)
    18:07:26 <jwb> thanks
    18:07:32 <FranciscoD> #endmeeting

