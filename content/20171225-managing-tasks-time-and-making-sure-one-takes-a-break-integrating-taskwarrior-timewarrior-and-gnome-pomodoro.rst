Managing tasks, time, and making sure one takes a break: Integrating Taskwarrior, Timewarrior, and Gnome Pomodoro
#################################################################################################################
:date: 2017-12-25 01:16:02
:author: ankur
:category: Tech
:tags: Bash, Fedora, Timewarrior, Taskwarrior, Pomodoro, Gnome-Pomodoro, Time management
:slug: managing-tasks-time-and-making-sure-one-takes-a-break-integrating-taskwarrior-timewarrior-and-gnome-pomodoro
:summary: As the amount of work increases, it becomes ever so more important to
          manage time and work in an efficient way. So, there's Taskwarrior_
          for managing tasks, Timewarrior_ for tracking them, and `Gnome
          Pomodoro`_ for making sure one takes regular breaks and doesn't let
          the long hours affect their health in a bad way.

With the new year, come resolutions. On many a list will there be a
determination to do better in the coming year, to be more organised, more
efficient, more productive.

I'm quite organised myself. I have lists, calendars, reminders, budgets, and
all of that. Being a FOSS person, my first thought, inevitably, is to see if
there's a piece of software that would aid me.

This post documents how one can get Taskwarrior_, Timewarrior_, and `Gnome
Pomodoro`_ to work together to manage tasks, track them, and break those long
hours into smaller bits with regular breaks.

Taskwarrior helps manage tasks
------------------------------

For managing tasks, there's the rather excellent Taskwarrior_. It's command
line, and there are various user interfaces that have been developed for it
too. (Vit_ is one that provides a terminal interface with Vim_ like
keybindings, and there's a `Vim plugin
<https://github.com/blindFS/vim-taskwarrior>`__ too.) One can even set up a
Taskwarrior_ server to sync the data between different machines. There are a
few hosted services that give free Taskwarrior_ server accounts too. Perhaps
the best bit, is excellent documentation.  Taskwarrior_ really does make it
easy to `get things done <https://taskwarrior.org/news/news.20150627.html>`__.

Timewarrior tracks time spent on tasks
----------------------------------------

Taskwarrior_ is not meant to be a time tracker, and upstream says so quite
plainly. In fact, upstream went ahead and wrote Timewarrior_ for that purpose
entirely. Like Taskwarrior_, Timewarrior_ is also a command line tool.

Integrating the two is quite easy, using a Taskwarrior_ hook, as `documented
here <https://taskwarrior.org/docs/timewarrior/taskwarrior.html>`__. Each time
a task is started, or stopped in Taskwarrior_, the hook calls Timewarrior_ to
start or stop tracking the task too.

Note: to ensure that this hook is run before the `Gnome Pomodoro`_ hook that we
set up in the next section, please save the hook file as
:code:`~/.task/hooks/on-modify.00-timewarrior`

Gnome Pomodoro reminds us to take regular breaks
-------------------------------------------------

So, one can manage tasks, and track the time spent working on them, and that's
great. It was sufficient for me for quite a while, before I realised that I was
spending too much time at my desk. What made it worse was the realisation that
for us white collar professionals, a majority of our lives will be spent at a
desk typing away on a computer. There's enough research to show that spending
all those long hours working in a seated position is bad for one's health.

So, I went looking for the changes I should make to my work regime, and ran
into the Pomodoro_ technique. The idea is to take short breaks at regular
intervals. One can use these to get up and walk around a bit, get them 10,000
steps! There are plenty of tools that implement the Pomodoro_ technique. A
simple timer works too. The one I settled on is `Gnome Pomodoro`_ which
integrates really well with Gnome Shell. Every 25 minutes, it'll remind the
user to take a 5 minute break.

Now, let us integrate `Gnome Pomodoro`_ with both Taskwarrior_ and Timewarrior_:

- When a task is started using :code:`task <filter> start`, Taskwarrior_
  already begins to track it using the hook, and a Pomodoro should also be
  started.
- When a Pomodoro is over and `Gnome Pomodoro`_ notifies of a break,
  Timewarrior_ should be paused too.
- When the break is over, and another Pomodoro starts, Timewarrior_ should
  resume tracking the task.
- When a task is stopped, Taskwarrior_ will stop tracking it via the hook
  already, and the Pomodoro should be stopped as well.

This is a very simple set up. A task must be started using Taskwarrior_ here,
and each time `Gnome Pomodoro`_ pauses and resumes from breaks, the same task
will be resumed unless it was stopped and another started.

It turned out to be quite easy because of how well these three tools have been
designed. Here's a Taskwarrior_ hook for `Gnome Pomodoro`_ similar to the one
for Timewarrior_:

.. code:: python

    #!/usr/bin/env python2
    # API is here: https://taskwarrior.org/docs/hooks.html
    # To be saved at ~/.task/hooks/on-modify.01-gnome-pomodoro to ensure it is
    # run after the timewarrior hook, which should be saved as
    # ~/.task/hooks/on-modify.00-timewarrior
    # Otherwise, this is run before which then runs the Gnome-Pomodoro actions
    # things get quite messy!
    import json
    import os
    import sys

    # Make no changes to the task, simply observe.
    old = json.loads(sys.stdin.readline())
    new = json.loads(sys.stdin.readline())
    print(json.dumps(new))

    # Start pomodoro when task is started
    if 'start' in new and 'start' not in old:
        os.system('gnome-pomodoro --start')
    # Stop pomodoro when a task is stopped
    elif 'start' not in new and 'start' in old:
        os.system('gnome-pomodoro --stop')


It's called when a task is modified. It checks the old and new states. If a
task is started, it starts :code:`gnome-pomodoro`, and when it's stopped, it
stops it. This is one direction.

The other direction requires some tinkering with `Gnome Pomodoro`_ to set up
custom scripts. In the preferences, one must enable the "Custom actions"
plugin:

.. figure:: {static}/images/20171225-gnome-pomodoro-plugins.png
    :align: center
    :height: 500px
    :scale: 60%
    :target: {static}/images/20171225-gnome-pomodoro-plugins.png
    :alt: A screenshot showing the plugin preferences in Gnome Pomodoro.

Then, a "Custom Actions" entry will be added to the preferences. We need to add
two of them. The first, resumes Timewarrior_ tracking when the Pomodoro
resumes:

.. figure:: {static}/images/20171225-gnome-pomodoro-action-resume-timew.png
    :align: center
    :height: 500px
    :scale: 60%
    :target: {static}/images/20171225-gnome-pomodoro-action-resume-timew.png
    :alt: A screenshot showing custom action that will resume timew after a break.

Similarly, the second stops Timewarrior_ when a break begins, or the user
pauses the Pomodoro_:

.. figure:: {static}/images/20171225-gnome-pomodoro-action-stop-timew.png
    :align: center
    :height: 500px
    :scale: 60%
    :target: {static}/images/20171225-gnome-pomodoro-action-stop-timew.png
    :alt: A screenshot showing custom action that will stop timew at the start of a break.

(If no tasks are active, Timewarrior_ doesn't do anything, so that case does
not need to be handled separately.)

There are certain `limitations to what commands can go in there
<https://github.com/codito/gnome-pomodoro/issues/275#issuecomment-282494447>`__,
so I've used a shell script to implement the required logic:

.. code:: bash

    #!/bin/bash
    # save as ~/bin/track-timew.sh
    # note that ~/bin/ must be in PATH

    resume ()
    {
        timew || timew continue
    }

    pause ()
    {
        timew && timew stop
    }

    clean ()
    {
        # sed only does greedy regex so it's slightly complicated
        # could use perl to make this a lot simpler because perl does non
        # greedy too.
        for entry in $(timew summary :ids | grep -o '@.*' | sed -E 's/(^@[[:digit:]]+[[:space:]]+)/\1 |/' | sed -E 's/([[:digit:]]+:[[:digit:]]+:[[:digit:]]+ )/| \1/' | sed 's/|.*|//' | sed -E 's/[[:space:]]{2,}/ /' | cut -d ' ' -f 1,4 | grep -E '0:0[01]:..' | cut -d ' ' -f 1 | tr '\n' ' '); do timew delete "$entry"; done
    }

    usage ()
    {
        echo "$0: wrapper script around timewarrior to carry out common tasks"
        echo "For use with Gnome-Pomodoro's action plugin"
        echo
        echo "Usage: $0 <option>"
        echo
        echo "OPTIONS:"
        echo "-r    resume tracking of most recently tracked task"
        echo "-p    pause tracking"
        echo "-c    clean up short tasks (less than 2 minutes long)"
    }

    # check for options
    if [ "$#" -eq 0 ]; then
        usage
        exit 1
    fi

    # parse options
    while getopts "rpch" OPTION
    do
        case $OPTION in
            r)
                resume
                exit 0
                ;;
            p)
                pause
                exit 0
                ;;
            c)
                clean
                exit 0
                ;;
            h)
                usage
                exit 1
                ;;
            ?)
                usage
                exit 1
                ;;
        esac
    done


The script is quite simple, and I hope, self-explanatory too. I'll leave
interpretation of the :code:`clean` function to the reader ;)

That's all there is to it. There must be other ways of doing the same thing,
possibly with different tools too, but this system required least changes to my
current workflow. Do remember that these tools can only aid us. It is us that
need to show that bit of discipline to follow the plan through. I hope some
will find it helpful, and may the new year be healthier and more productive for
us all! :)

.. _Taskwarrior: https://taskwarrior.org/
.. _Timewarrior: https://timewarrior.net/
.. _Gnome Pomodoro: http://gnomepomodoro.org/
.. _Vit: https://tasktools.org/projects/vit.html
.. _Vim: https://vim.org
.. _Pomodoro: https://en.wikipedia.org/wiki/Pomodoro_Technique
