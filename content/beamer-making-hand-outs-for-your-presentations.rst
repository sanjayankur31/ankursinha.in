Beamer: making hand outs for your presentations
###############################################
:date: 2012-10-07 15:55
:author: ankur
:category: Tech
:tags: LaTeX
:slug: beamer-making-hand-outs-for-your-presentations

It's often handy to create hand-outs for your presentations. (I need
them for my master's assessments at the moment). It's really simple to
make hand-outs. What we do is first create a presentation, like we
normally do. Then, since the presentation generally contains overlays
(the ``pause`` command and more), we make another version where these
commands are ignored. That's the most of it. I go ahead another step and
create another TeX file to print multiple slides in a single page.

As you'll notice, between the presentation, and it's hand out version,
the only change is in the ``documentclass`` options, where you add a
"``handout``\ " option in the latter. Instead of copy pasting and
keeping these two files in sync, a smart thing to do is to write
everything other than the ``documentclass`` line in another text file
and then simply include it using an ``input`` command in two files for
the two versions.

So, the files you have are:

#. **mypresentation-src.tex**: the file that contains your entire
   presentation, other than the ``documentclass`` line
#. **mypresentation.tex**: this file will contain the ``documentclass``
   line for your presentation
#. **mypresentation-hand-out.tex**: this file contains another
   ``documentclass`` line for your presentation's hand-out version where
   overlays are ignored
#. **mypresentation-hand-out-print-multiple.tex**: this file will
   generate a pdf file with multiple slides on a single page

This is what your **mypresentation-src.tex** file looks like (Observe
the lack of a document class definition):

::

    usepackage{color}

    % links, urls, refs
    definecolor{links}{HTML}{2A1B81}
    usepackage{hyperref}
    hypersetup{colorlinks,linkcolor=,urlcolor=links}

    % graphics
    usepackage{graphicx}

    % algorithm
    usepackage{algorithmic}

    usepackage{textcomp}

    % beamer theme
    % use defaults for theme
    usetheme{Berlin}
    usecolortheme[RGB={41,65,114}]{structure}
    logo{includegraphics[width=2.5cm,angle=0]{uts-logo.jpg}}

    %% title %%
    title{Week review: October 2 2012}
    author[Ankur Sinha]{Ankur SinhaUTS ID: 11484312}
    institute{University of Technology, Sydney}
    date{October 2 2012}

    %% document begins %%
    begin{document}

    %% title frame %%
    begin{frame}
    titlepage

    end{frame}

    .....
    ..
    ...
    end{document}

This is how your **mypresentation.tex** file looks like:

::

    documentclass[usenames,dvipsnames,10pt]{beamer}
    input{mypresentation-src.tex}

This is how your **mypresentation-hand-out.tex** file looks like
(Observe that the only addition is the "handout" option):

::

    documentclass[usenames,dvipsnames,10pt,handout]{beamer}
    input{mypresentation-src.tex}

This is how your **mypresentation-hand-out-print.tex** file looks like:

::

    documentclass[a4paper]{article}
    usepackage{pdfpages}

    begin{document}
    includepdf[pages=1-last,nup=2x2,landscape=false,frame=true,
    noautoscale=true,scale=0.6,delta=5mm 5mm]{mypresentation-hand-out.pdf}
    end{document}

You need to compile the 3 TeX files (not the mypresentation-src.tex
file). Note that the -hand-out-print.tex file should be compiled last,
since it requires the hand-out.pdf file. It's pretty simple. I ran in to
all of this via Google of course. I just thought it'd be nice to have it
all in one place. Hope it helps. Cheers!
