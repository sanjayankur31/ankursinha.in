Zaphod - a LaTeX change tracking tool
#####################################
:date: 2016-02-13 17:16:24
:author: ankur
:category: Research
:tags: LaTeX, Programming, Git, Fedora, Zaphod
:slug: zaphod-a-latex-change-tracking-tool
:summary: Introducing `Zaphod <https://github.com/sanjayankur31/zaphod>`__ - a `Python <https://www.python.org/>`__ script that attempts to help `LaTeX <https://en.wikipedia.org/wiki/LaTeX>`__ users collaborate over their academic writing. It uses the power of `Git <https://en.wikipedia.org/wiki/Git_(software)>`__ to track changes, `latexdiff <https://www.ctan.org/pkg/latexdiff?lang=en>`__ to generate a PDF with annotated additions and removals from the document, and provides a simple interactive review tool that lets the user pick what changes they want to accept. You can use Zaphod to track changes in your LaTeX documents.

The name
---------
Well, I needn't say much here, need I? `Hitchhiker's guide to the galaxy <https://en.wikipedia.org/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy>`__, anyone?

Of course, a good tip to naming a new open source tool is to pick a project name that is easily searchable. With `LaTeX <https://en.wikipedia.org/wiki/LaTeX>`__ related searches, it's a tad difficult - the addition of the word to LaTeX to anything tends to generate rather undesirable results. Fortunately, `Zaphod <https://en.wikipedia.org/wiki/Zaphod_Beeblebrox>`__ seems to have been spared the honour..

LaTeX is great!
---------------
Academics really like `LaTeX <https://en.wikipedia.org/wiki/LaTeX>`__ - it's a brilliant tool, the best one in my opinion, for academic writing. Using LaTeX is widely accepted to be more complex than using a simple `WYSIWYG <https://en.wikipedia.org/wiki/WYSIWYG>`__ tool like Word. One writes in plain text using LaTeX constructs and then compiles it to produce a brilliantly formatted PDF. The point of using LaTeX is that you get to focus on the matter - the actual text, and LaTeX largely takes care of the look, the formatting and all that. There are `quite a few applications <https://en.wikipedia.org/wiki/Comparison_of_TeX_editors>`__ that provide one click compilation and other features, by the way, so you don't absolutely have to use the command line. There's even `Lyx <https://www.lyx.org/>`__ which is quite close to a WYSIWYG application for LaTeX.

Tracking changes
================
Another limitation of using LaTeX is that you can't easily see what's changed between versions of PDFs. This makes collaboration using LaTeX difficult.

Word, for example, has a very useful "`Track changes <https://support.office.com/en-us/article/Track-changes-while-you-edit-024158a3-7e62-4f05-8bb7-dc3ecf0295c4>`__" feature that lets you record your changes and then lets the next person easily review them and decide which ones are to be applied.

There are various tools strewn over the Internet that do help with this, but they aren't quite as convenient as I'd have hoped. Some examples:

- `latexdiff <https://www.ctan.org/pkg/latexdiff?lang=en>`__ (Zaphod is based on this and uses it to generate changes - why reinvent the wheel?)
- the `changes <http://www.ctan.org/pkg/changes>`__ package
- `track changes <http://trackchanges.sourceforge.net/>`__ (didn't try this out)

So - Zaphod
-----------
Various editors make writing LaTeX quite easy. That isn't much of an issue any more. Zaphod tries to address the second issue - tracking changes. It combines existing tools to implement a certain workflow where you can write text, send it to people, verify and include their changes.

The workflow - an example
=========================

- Create a Git repository for your LaTeX paper.
- Write your draft.

I'm using a `test repository <https://github.com/sanjayankur31/latex-changes>`__ which looks like this:

.. code:: bash

    [asinha@ankur  latex-changes(master=)]$ tree
    .
    ├── LICENSE
    ├── README.rst
    └── src
        ├── abstract.tex
        ├── conclusion.tex
        ├── discussion.tex
        ├── introduction.tex
        ├── Makefile
        ├── methods.tex
        ├── paper.pdf
        ├── paper.tex
        └── results.tex

    1 directory, 19 files
    [asinha@ankur  latex-changes(master=)]$

- Commit your changes.

Your repository will look something like this:

.. code:: bash

    [asinha@ankur  latex-changes(master=)]$ git lg
    * 280fef6 - (4 days ago) Subsection test — Ankur Sinha (Ankur Sinha Gmail) (HEAD -> master, origin/master, origin/HEAD)
    * 0c0238b - (4 days ago) Moved script to its own repository — Ankur Sinha (Ankur Sinha Gmail)
    ....
    * 164e0d3 - (8 days ago) Add vim temp files to gitignore — Ankur Sinha (Ankur Sinha Gmail)
    * bd02966 - (8 days ago) Commit fake paper — Ankur Sinha (Ankur Sinha Gmail)
    * 11ad32b - (8 days ago) Initial commit — Ankur Sinha


This is all pretty standard Git usage. Now, the interesting part:

- Send your PDF and LaTeX sources to your collaborator (or give them access to your repository).
- They make changes and commit them. Now, your Git revision tree will look something like this:

.. code:: bash

    [asinha@ankur  latex-changes(master=)]$ git lg
    * 46d0c11 - (4 hours ago) Add a new file. — Ankur Sinha (Ankur Sinha Gmail) (HEAD -> master, origin/master, origin/HEAD)
    * ba4b06d - (3 days ago) Update readme — Ankur Sinha (Ankur Sinha Gmail)
    * 53033b8 - (3 days ago) Remove example output directory — Ankur Sinha (Ankur Sinha Gmail)
    * d82266b - (4 days ago) More subsection changes — Ankur Sinha (Ankur Sinha Gmail)
    * 280fef6 - (4 days ago) Subsection test — Ankur Sinha (Ankur Sinha Gmail)
      ...

Zaphod lets you specify two Git revisions and generates a list of changes between these two. So, for example, running the diff command would do this:

.. code:: bash

   [asinha@ankur  latex-changes(master=)]$ python3 ../zaphod/zaphod.py diff -r bd02966 -m paper.tex -s src
    ....
    ....
    COMPLETE: The following branches have been created:
    201602131935-latexdiff-rev1: Revision 1.
    201602131935-latexdiff-rev2: Revision 2.
    201602131935-latexdiff-annotated: Branch with annotated versions of sources and diff pdf.
    The generated diff pdf is: src/diff-bd02966-master.pdf.

and your repository now looks like this:

.. code:: bash

    * 9e58178 - (2 minutes ago) Save annotated changes between bd02966 and master — Ankur Sinha (Ankur Sinha Gmail) (HEAD -> 201602131935-latexdiff-annotated)
    * 46d0c11 - (5 hours ago) Add a new file. — Ankur Sinha (Ankur Sinha Gmail) (origin/master, origin/HEAD, master, 201602131935-latexdiff-rev2)
    * ba4b06d - (3 days ago) Update readme — Ankur Sinha (Ankur Sinha Gmail)
    ....
    * bd02966 - (8 days ago) Commit fake paper — Ankur Sinha (Ankur Sinha Gmail) (201602131935-latexdiff-rev1)
    * 11ad32b - (8 days ago) Initial commit — Ankur Sinha

Zaphod uses latexdiff to check for differences between the two revisions, marks them as branches for easy reference, and then creates a new branch with annotated source files and a nice pdf which looks like this:

.. image:: {static}/images/20160213-zaphod-screenshot.png
    :align: center
    :height: 800px
    :scale: 50 %
    :target: {static}/images/20160213-zaphod-screenshot.png
    :alt: Screenshot of annotated PDF

That looks rather nice, isn't it? And it resembles what a Word document with annotations looks like too. latexdiff has various markup styles which can be passed to Zaphod as arguments to modify how the annotations look. The most important part here is that because Zaphod is using mighty Git, there's no chance of you losing any work at all. *In fact, if you have untracked and uncommitted changes in your repository, Zaphod refuses to run at all.*

Now, a look at how the revise function works:

.. code:: bash

    [asinha@ankur  latex-changes(201602131935-latexdiff-annotated)]$ python3 ../zaphod/zaphod.py revise -s src/ -m paper.tex
    Working on file: src/paper.tex.
    File under revision: src/paper.tex

    Deletion found:
    ---
    Tracking
    ---

    Delete? Y/N/y/n: y
    Deleted

    File under revision: src/paper.tex

    Addition found:
    +++
    Visualising
    +++

    Add? Y/N/y/n: n
    Skipped

    File under revision: src/paper.tex

    Addition found:
    +++
    \input{discussion}

    +++

    Add? Y/N/y/n:
    ....
    ....
    ....
    [201602131935-latexdiff-annotated 3ba757f] Save after going through changes
     5 files changed, 34 insertions(+), 56 deletions(-)
     create mode 100644 src/accepted.pdf
     rewrite src/paper.tex (72%)

    COMPLETE: Changes accepted and committed.
    The generated pdf is: src//accepted.pdf.
    You can merge this branch to master if you wish.

and your repository looks like this:

.. code:: bash

    [asinha@ankur  latex-changes(201602131935-latexdiff-annotated)]$ git lg
    * 3ba757f - (53 seconds ago) Save after going through changes — Ankur Sinha (Ankur Sinha Gmail) (HEAD -> 201602131935-latexdiff-annotated)
    * 9e58178 - (17 minutes ago) Save annotated changes between bd02966 and master — Ankur Sinha (Ankur Sinha Gmail)
    * 46d0c11 - (5 hours ago) Add a new file. — Ankur Sinha (Ankur Sinha Gmail) (origin/master, origin/HEAD, master, 201602131935-latexdiff-rev2)
    ....

The new pdf, accepted.pdf, is the latest version of your document and includes the changes you think should make the cut. If you're happy with these, you can simply merge this branch into master, and continue working. If you're not, you can go back to master, or another commit, and tinker some more - we're using Git, do what you want. In line with what I did above, the PDF looks like this:

.. image:: {static}/images/20160213-zaphod-2.png
    :align: center
    :height: 800px
    :scale: 50 %
    :target: {static}/images/20160213-zaphod-2.png
    :alt: Screenshot of annotated PDF

Pretty neat, huh? At least I think so ;)

Give it a go!
-------------
I've tested the tool out myself on a number of different cases, but I'm quite certain I've missed some and there are always bugs that I haven't run into yet. It's a rather simple script in its current version - not all the commands that are called are checked for errors and so on. As I get more time in the future, I'll keep improving it. For the time being, though, it does work.

Give it a go and let me know what you think? It's `hosted on Github <https://github.com/sanjayankur31/zaphod>`__, so feel free to report issues and open pull requests. Let's make LaTeX even more usable!
