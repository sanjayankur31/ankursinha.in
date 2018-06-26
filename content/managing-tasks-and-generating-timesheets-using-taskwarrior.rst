Managing tasks and generating timesheets using taskwarrior
##########################################################
:date: 2014-04-09 09:41
:author: ankur
:category: Tech
:tags: Fedora, Taskwarrior
:slug: managing-tasks-and-generating-timesheets-using-taskwarrior
:summary: Taskwarrior is a great utility that helps you manage your tasks.

A while back, I `had blogged on how one can use gtg and
hamster-time-tracker to manage their tasks`_, and track them. Now, I
personally prefer the terminal. A few days ago, I was talking to
`threebean`_ and he pointed me to his `time sheet`_. Helpful as always,
threebean told me how he'd generated the time sheet. I document the
steps here for any one else that's interested in doing the same.

What you need
-------------

::

    $ sudo dnf install ansi2html task #use yum if you prefer

This will provide you with the **task** command. Read the quick tutorial
on using it `here`_. As usual, RTFM at `` $ man task``.

Generating time sheets
----------------------

Then, you need two shell scripts. The first, generates your time sheet
from **task**:

::

    #!/bin/bash
    # File : timesheet.sh
    #
    # This generates timesheet data for my fedora tasks only

    source /home/<USER>/.bashrc
     
    phrase="1-weeks-ago"
    #fmt="%m/%d/%Y"
    fmt="%Y-%m-%d"
    start=$(date +$fmt -d $phrase)
    end=$(date +$fmt)
    filter="project.is:fedora"
     
    echo " (generated at $(date))"
    echo
    echo " -- Tasks completed from $start to $end (back $phrase) -- "
    /usr/bin/task work_report $filter end.after:$start
     
    echo
    echo " -- Upcoming tasks -- "
    /usr/bin/task next $filter
     
    echo
    echo " -- Blocked tasks -- "
    /usr/bin/task blocked $filter

    echo
    echo " -- Blocking tasks -- "
    /usr/bin/task blocking $filter

    echo
    echo " -- Summary -- "
    /usr/bin/task summary $filter
     
    echo
    echo " -- History -- "
    /usr/bin/task history $filter
    /usr/bin/task ghistory $filter
    /usr/bin/task burndown.daily
    /usr/bin/task burndown

The second just converts it into an html file that you can host. This
one looks like this:

::

    # File : make-report.sh 
    # 
    # Generates reports from my task data
    #

    #!/bin/bash
     
    today=$(date +%Y-%m-%d)
    /home/<USER>/bin/timesheet.sh | ansi2html > /tmp/timesheet-fedora.html
    /home/<USER>/bin/timesheet-all.sh | ansi2html > /tmp/timesheet-all.html
    cp /tmp/timesheet-fedora.html ~/timesheets/$today.html
    cp /tmp/timesheet-fedora.html ~/timesheets/latest.html

    cp /tmp/timesheet-all.html ~/timesheets/$today-all.html
    cp /tmp/timesheet-all.html ~/timesheets/latest-all.html

    scp -i /home/<USER>/.ssh/id_fedora_rsa /tmp/timesheet-fedora.html <FAS USER>@fedorapeople.org:./public_html/timesheets/$today.html
    scp -i /home/<USER>/.ssh/id_fedora_rsa /tmp/timesheet-fedora.html <FAS USER>@fedorapeople.org:./public_html/timesheets/latest.html
    rm /tmp/timesheet*.html

This will generate a pretty time sheet for you, like the one threebean
hosts, or `the one I host`_. Taskwarrior is quite the same as gtg. I've
moved to it because I prefer using the terminal as much as possible, and
it lets me create sheets where I can keep an eye on my tasks. Yes, I'll
continue to maintain gtg in Fedora. Don't worry ;)

Customizing your time sheet
---------------------------

You can customize your time sheets and other options by creating a
``~/.taskrc`` file. More themes are available in
``/usr/share/doc/task/rc/``

My .taskrc looks like this:

::

    # Files
    data.location=/home/asinha/.task
     
    _forcecolor=yes
    defaultwidth=160
     
    include /usr/share/doc/task/rc/dark-blue-256.theme
     
    report.work_report.description=now
    report.work_report.columns=priority,project,description,end,entry,entry.age
    report.work_report.labels=priority,project,description,completed,entered on,age
    report.work_report.sort=project+,end-
    report.work_report.filter=status:completed
    journal.time=on

Play around with it. There's quite a bit you can do.

Some more: taskserver
---------------------

I haven't tried this out myself. I don't need it yet. However, you can
run a taskserver on your host and log tasks from anywhere over the
internet. Documentation can be found
`here <http://taskwarrior.org/docs/server_setup.html>`__. If you do
figure it out, please write a blog post documenting it for Fedora.
`threebean's working on the taskd`_ package already.

Cheers!

.. _had blogged on how one can use gtg and hamster-time-tracker to manage their tasks: http://ankursinha.in/blog/2013/12/16/time-and-task-tracking.html
.. _threebean: https://fedoraproject.org/wiki/User:Ralph
.. _time sheet: http://threebean.org/timesheets/latest.html
.. _here: http://taskwarrior.org/docs/
.. _the one I host: http://ankursinha.fedorapeople.org/timesheets/latest.html
.. _threebean's working on the taskd: https://bugzilla.redhat.com/show_bug.cgi?id=1066573
