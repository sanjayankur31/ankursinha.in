New Zaphod release - v0.5.7
###########################
:date: 2016-02-28 16:52:27
:author: ankur
:category: Research
:tags: LaTeX, Programming, Git, Fedora, Zaphod
:slug: new-zaphod-release-v0-5-7
:summary: I've released a new version of `Zaphod <https://github.com/sanjayankur31/zaphod>`__ - A LaTeX change tracking tool that I've been working on recently.

`I'd written about Zaphod recently <{filename}/20160213-zaphod-a-latex-change-tracking-tool.rst>`__. I've been making some tweaks to it - just some enhancements to the revision bit which will make it easier to use. The diff bit is still the same - I didn't see the need to make too many improvements there. 

New revision bits
------------------

Now, it looks like this when you start it up:

.. code:: bash

    [asinha@cs-as14aho-2-herts-ac-uk  latex-changes(201602281328-latexdiff-annotated)]$ python3 ../zaphod/zaphod.py revise -m paper.tex -s src
    [Zaphod] LaTeX files with annotations:
    [1] src/discussion.tex
    [2] src/introduction.tex
    [3] src/paper.tex
    [4] src/methods.tex

    Pick file to revise? 1-4/Q/q:

The idea here is that the user should be able to pick what file they want to edit. Previously, Zaphod just went file after file.

Once you pick a file, it'll look like this:

.. code:: bash

    ....
    Pick file to revise? 1-4/Q/q: 1

    ====== src/discussion.tex ======
    +++ Addition found +++
    \section{Discussion}

    Add a new file.

    +++ Addition found +++
    Accept addition? Y/N/Q/y/n/q: y
    [Zaphod] Addition accepted.

    [Zaphod] File src/discussion.tex revised and saved.
    [Zaphod] LaTeX files with annotations:
    [1] src/introduction.tex
    [2] src/paper.tex
    [3] src/methods.tex

    Pick file to revise? 1-3/Q/q:

But, you can also make partial revisions. This is handy in situations where you have a long file and do not have the time to go over all of it at once. So, here's an example. I go over some changes, but I need to stop there for the moment:

.. code:: bash

    ...
    [Zaphod] LaTeX files with annotations:
    [1] src/introduction.tex
    [2] src/paper.tex
    [3] src/methods.tex

    Pick file to revise? 1-3/Q/q: 2

    ====== src/paper.tex ======
    --- Deletion found ---
    Tracking
    --- Deletion found ---
    Accept deletion? Y/N/Q/y/n/q: y
    [Zaphod] Deletion accepted.

    ====== src/paper.tex ======
    +++ Addition found +++
    Visualising
    +++ Addition found +++
    Accept addition? Y/N/Q/y/n/q: y
    [Zaphod] Addition accepted.

    ====== src/paper.tex ======
    +++ Addition found +++
    \input{discussion}

    +++ Addition found +++
    Accept addition? Y/N/Q/y/n/q: q
    Save partial file? Y/N/y/n: y
    [Zaphod] Some files still have latexdiff annotations:
    [1] src/introduction.tex
    [2] src/methods.tex

    Generate pdf? Y/y/N/n: n
    [Zaphod] Not generating pdf.
    [Zaphod] Following files have been revised (maybe partially):
    [1] src/discussion.tex
    [2] src/paper.tex

    Commit current changes? Y/y/N/n: n
    [Zaphod] Exiting without committing.


There's one catch here, though. Because I want to make absolutely sure that Zaphod doesn't make any changes "by mistake", you'll have to either stash or commit these changes before you can run Zaphod again. This is just to be on the safer side. A better way would probably be for Zaphod to remember what files were partially revised, but I haven't implemented it at the moment. I'd actually just commit the changes - I mean, that's why we've got Git, right?

.. code:: bash

    [asinha@cs-as14aho-2-herts-ac-uk  latex-changes(201602281328-latexdiff-annotated *)]$ python3 ../zaphod/zaphod.py revise -m paper.tex -s src
    Modifed or untracked files found.
    git status output:
     M src/discussion.tex
     M src/paper.tex

    Please stash or commit and rerun Zaphod.



That's it. I think it's a lot easier to use now, and in this design addresses a lot more use cases than it did before. 

`Give it a go <https://github.com/sanjayankur31/zaphod/releases>`__ and `let me know <https://github.com/sanjayankur31/zaphod/issues/new>`__ if things break - I've tested it myself, but only on a mock document.
