An update on the migration of Fedora Free Media to Pagure
#########################################################
:date: 2017-02-08 14:50:50
:author: ankur
:category: Tech
:tags: Fedora, Community
:slug: an-update-on-the-migration-of-fedora-free-media-to-pagure
:summary: The `Fedora Free Media programme`_ is being migrated over to Pagure. Here's a quick update on what's going on and where you can help.

The `Fedora Free Media programme`_ aims to provide Fedora media to users in regions of the world where the internet connectivity is insufficient. The volunteers of this team download, burn, and mail out media from their own money. This is an imperative initiative that helps spread Free software to regions that are yet to catch up when it comes to infrastructure. When I'd checked last, we had about 250 volunteers in total - not all of them are active, of course, but that's the number I've been able to generate from querying FAS and the mailing list for the moment.

The setup
----------

The programme uses a `form <http://fedoraproject.org/freemedia/FreeMedia-form.html>`__ that users fill to request media. This form is a frontend that files a ticket on our `trac instance <https://fedorahosted.org/freemedia/>`__. Volunteers then accept tickets and send out requests, closing the tickets when they do. Tickets that have not been serviced are regularly closed as "WONTFIX". We send out an e-mail to the filer simply saying that since we've received too many requests, we've been unable to service them all.

The migration to Pagure
-----------------------

Since Fedorahosted will soon be shut down, we need to move our repository to Pagure. We're going to use this opportunity to revitalise the project. There's a tracker issue here on the Pagure repository.

- https://pagure.io/pagure/issue/1223
- https://pagure.io/Free-Media/Housekeeping/issue/1

Group membership refresh
========================

- https://pagure.io/Free-Media/Housekeeping/issue/7
- https://pagure.io/Free-Media/Housekeeping/issue/6

Unlike most teams where having inactive accounts doesn't affect the functioning of the group too much, it does tend to affect the Free Media team. This is because we really do need active members to be able to handle the load. Another issue here is privacy - only group members have access to the tickets, since the tickets contain the filers' addresses. So, ideally, only the smallest number of people needed must have access to these tickets.

The idea we're floating is that we'll clean the group and the mailing list up, and invite existing users to re-join the team. Ones that volunteer will be added back. Please note that it is mandatory for each volunteer to have a Fedora user page, and every group member must also be subscribed to the mailing list so that they can be easily contacted when needed.

New repository setup
====================

- https://pagure.io/Free-Media/Housekeeping/issue/9

We can either have one repository that handles all tickets, or we can make it more modular and have a few repositories that handle tickets for various regions. Multiple repositories will need more work to do with the scripts and the frontend.

Update form to work with Pagure based on our new setup
======================================================

- https://pagure.io/Free-Media/Housekeeping/issue/11

The form obviously needs to be updated to file tickets to the Pagure repository now. We have a new form that's much nicer, but it does need work before it can be deployed.

Translate form
==============

- https://pagure.io/Free-Media/Housekeeping/issue/10

It'll be even nicer if we can translate the form to make it more accessible to the different regions.

Use updated liveisos instead of release images
===============================================

- https://pagure.io/Free-Media/Housekeeping/issue/8

Since the entire point of the programme is to serve users with limited internet connectivity, some of us feel there is little point in providing them release media that then must be udpated. The community already generates `updated media <http://dl.fedoraproject.org/pub/alt/live-respins/>`__, and we'd like to use these instead. We'd also like to help maintain the updated media by mirroring/seeding the sources.

Of course, this also brings up the age old question of migrating to USB sticks. I don't think they're still cheap enough for the Free Media programme to send out.

Metrics
========

- https://pagure.io/Free-Media/Housekeeping/issue/5

We want to put scripts in place that will generate metrics for us at regular intervals - monthly maybe. This would really help gauge the work of the programme, and in turn, help us improve.

So, yeah!
---------

There's quite a lot of work to be done, as you can see.

We're `trying to ascertain if it's all worth it to begin with - are we servicing enough tickets, and do we have a sufficiently large team that can continue to do so <https://pagure.io/Free-Media/Housekeeping/issue/14>`__? Is the Free Media programme useful? The only way we'll know is if we check the recent metrics, and, of course, we'd like to hear what the community thinks. I think the programme is quite useful. When I was back in India, I'd send out media every month, and I'd usually get a very nice e-mail from the ticket owner telling me how much they appreciated the media.

The Free Media programme runs in isolation to the rest of the community, and we'd also like to change this. We want to see if we can have contributors from each region that also serve on the Fedora Ambassadors team - it'll help both teams keep up with each other to begin with, and it'll ensure that the Free Media team is not lost in the community. In order to make it a sustainable service, we need a constant influx of contributors to replace ones that leave or move and cannot contribute any more.

If you'd like to help out, please drop a comment on the tickets, or file a new one, or e-mail me, or drop a comment on this post, or catch me on IRC!


.. _Fedora Free Media programme: https://fedoraproject.org/wiki/FreeMedia
