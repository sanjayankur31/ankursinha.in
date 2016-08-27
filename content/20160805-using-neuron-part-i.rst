Using NEURON - Part I
#####################
:date: 2016-08-05 13:24:48
:author: ankur
:category: Research
:tags: Fedora, Neuron, Computational neuroscience
:slug: using-neuron-part-i
:summary: I've got some time on my hands so I've decided to learn how to use the NEURON_ simulator. This series of posts are my personal notes. In this first one, we install NEURON_.

What is NEURON
---------------

From the `website <http://www.neuron.yale.edu/neuron/what_is_neuron>`__:

*NEURON is a simulation environment for modeling individual neurons and networks of neurons. It provides tools for conveniently building, managing, and using models in a way that is numerically sound and computationally efficient. It is particularly well-suited to problems that are closely linked to experimental data, especially those that involve cells with complex anatomical and biophysical properties.*

Installing NEURON on Fedora 24
-------------------------------

The first thing you do is install the simulator. I've been trying to build `copr <https://copr.fedorainfracloud.org/coprs/ankursinha/neuroscience-research/>`__ packages but they're not as simple as I'd have liked - the configurations that upstream uses for iv and neuron are outdated and require quite a bit of patching.

Download the sources
====================

First, download the source files:

.. code:: bash

    # Make sure we're in the /home/<user> directory
    cd
    # Make a new directory - use what you want but be consistent
    mkdir -p dump/neuron

    # Another one for the installed files
    # You can use /opt or /usr/local or any other directory
    # Using a directory in your home folder doesn't require root access
    mkdir -p dump/neuron-installation

    # Keep the sources here
    cd ~/dump/neuron

    # Install mercurial to checkout the neuron source code
    sudo dnf install hg
    # Download the source code
    # Can't build from the latest tar somehow.
    # http://www.neuron.yale.edu/neuron/download/getdevel
    hg clone http://www.neuron.yale.edu/hg/neuron/nrn

    # Check http://www.neuron.yale.edu/neuron/download/getstd for correct links
    wget http://www.neuron.yale.edu/ftp/neuron/versions/v7.4/iv-19.tar.gz

    # Untar the source for iv - this seems to work
    tar -xvf iv-19.tar.gz

Prep
====

We need to build iv first. On Fedora 24, the default gcc flags include :code:`-Wformat-security` so a quick patch needs to be applied to iv to get it to build. The patch `has been reported here <https://www.neuron.yale.edu/phpBB/viewtopic.php?f=20&t=3536>`__:

.. code:: diff

    diff -ur ../iv-18.orig/src/lib/IV-2_6/matcheditor.cpp ./src/lib/IV-2_6/matcheditor.cpp
    --- ../iv-18.orig/src/lib/IV-2_6/matcheditor.cpp   2014-01-08 19:10:44.895487120 +1100
    +++ ./src/lib/IV-2_6/matcheditor.cpp   2014-01-08 19:11:05.949315579 +1100
    @@ -82,7 +82,7 @@
             strncpy(buf, text->Text(), length);
             while (length > 0) {
                 buf[length] = '\0';
    -            if (sscanf(buf, pattern) == EOF) {
    +            if (sscanf(buf, "%s", pattern) == EOF) {
                     break;
                 }
                 --length;

Copy the diff into a file and call it :code:`iv-format-security.patch`. Place this in the directory where you have the neuron sources (:code:`~/dump/neuron`).
To apply the patch, enter the uncompressed iv directory:

.. code:: bash

    cd iv
    patch -p1 < ../iv-format-security.patch
    # On success, it'll say:
    # patching file src/lib/IV-2_6/matcheditor.cpp

Before we build either iv or neuron, we need to install the build dependencies:

.. code:: bash

    # Install dependencies from the standard repositories
    sudo dnf install xorg-x11-server-devel chrpath libtiff-devel imake libX11-devel automake autoconf libtool libXext-devel ncurses-devel readline-devel Random123-devel Cython openmpi-devel

I've left out Java - I have no intention of using the Java support. Instead of openmpi, you can also use mpich - that's up to you - replace :code:`openmpi-devel` with :code:`mpich-devel`.

Build
=====

Follow the instructions `here <http://www.neuron.yale.edu/neuron/download/compile_linux>`__.
First we build iv:

.. code:: bash

    # we're already in the iv source directory
    # ./configure --help for all available options
    # I use the default Fedora CFLAGS and CXXFLAGS
    # You needn't use these
    # rpm -E %optflags will tell you what the default ones on your system are
    # echo $CFLAGS
    # -O2 -g -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic
    # echo $CXXFLAGS
    # -O2 -g -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic

    # iv doesn't build with -Wnarrowing which is also default, so we disable it
    export CFLAGS="$CFLAGS -Wno-narrowing"
    export CXXFLAGS="$CXXFLAGS -Wno-narrowing"

    # configure, make, make install
    ./configure --prefix=/home/asinha/dump/neuron-installation/ --with-x
    # I have 24 processors, check to see how many you do
    make -j24
    make install

Then, we build neuron

.. code:: bash

    cd ../nrn
    # configure --help to see all options
    # Enable MPI
    module load mpi/openmpi-x86_64
    # More change to flags to get the thing to build
    export CFLAGS="$CFLAGS -Wno-narrowing -std=c99 -D_POSIX_C_SOURCE=200809L"
    export CXXFLAGS="$CXXFLAGS -Wno-narrowing -D_POSIX_C_SOURCE=200809L"
    ./build.sh
    ./configure --prefix=/home/asinha/dump/neuron-installation/ --with-x --with-paranrn --with-mpi --with-multisend --with-nrniv --with-iv=/home/asinha/dump/neuron-installation
    # I have 24 processors, check to see how many you do
    make -j24
    make install

Check
=====

Follow the instructions `here <http://www.neuron.yale.edu/neuron/download/compile_linux>`__.

.. code:: bash

    cd 
    cd dump/neuron-installation/
    find . -name "neurondemo"
    # You'll get something like: ./x86_64/bin/neurondemo
    ./86_64/bin/neurondemo
    # Will give out something like:
    # NEURON -- VERSION 7.5 (1454:2350fc838a79) 2016-08-01
    # Duke, Yale, and the BlueBrain Project -- Copyright 1984-2016
    # See http://neuron.yale.edu/neuron/credits
    # 
    # loading membrane mechanisms from /home/asinha/dump/neuron-installation/share/nrn/demo/release/x86_64/.libs/libnrnmech.so
    # Additional mechanisms from files
    #  cabpump.mod cachan1.mod camchan.mod capump.mod invlfire.mod khhchan.mod mcna.mod nacaex.mod nachan.mod release.mod
    # first instance of j
    # first instance of itmp
    # first instance of using_cvode_
    # first instance of movie_frame_dur_
    # first instance of realtime
    # first instance of running_
    # first instance of rtstart
    # first instance of stdrun_quiet
    # first instance of screen_update_invl
    # first instance of tstop
    # first instance of steps_per_ms
    # first instance of nstep_steprun
    # first instance of runStopAt
    # first instance of runStopIn
    # first instance of global_ra
    # first instance of mapped_nrnmainmenu_
    # first instance of v_init
    # first instance of n_graph_lists
    # first instance of i
    # first instance of eventslow
    # first instance of eventcount
    # first instance of cnt
    # oc>
    # 

Post
=====

Last, we update the PATH and things so that everything works smoothly in the future. The docs suggest an :code:`nrnenv` file that can be sourced in the :code:`.bashrc` file. We'll just follow the suggested method.

.. code:: bash

    cat >> ~/dump/neuron-installation/x86_64/bin/nrnenv << EOF
    export NRNINSTALLATION="\$HOME/dump/neuron-installation"
    export NRNCPU="x86_64"
    export PATH="\$PATH:\$NRNINSTALLATION/\$NRNCPU/bin"

    EOF

and modify :code:`.bashrc` to source it:

.. code:: bash

    echo "source /home/asinha/dump/neuron-installation/x86_64/bin/nrnenv" >> ~/.bashrc


Log out and back in, or source the file again: :code:`source ~/.bashrc`.  All the binaries for neuron should then be available to you:

.. code:: bash

    $ ls ~/dump/neuron-installation/x86_64/bin/
    bbswork.sh   iclass  idraw  memacs        modlunit  mos2nrn2.sh  nocmodl  nrngui  nrniv_makefile  nrnmech_makefile  nrnoc_makefile  nrnpyenv.sh  set_nrnpyenv.sh
    hel2mos1.sh  idemo   ivoc   mkthreadsafe  mos2nrn   neurondemo   nrnenv   nrniv   nrnivmodl       nrnoc             nrnocmodl       oc           sortspike

    $ which idraw 
    ~/dump/neuron-installation/x86_64/bin/idraw
    $ which nrniv
    ~/dump/neuron-installation/x86_64/bin/nrniv
    $ which nrnoc
    ~/dump/neuron-installation/x86_64/bin/nrnoc
    $ which oc
    ~/dump/neuron-installation/x86_64/bin/oc

I think that should be it! I've tested the instructions on my Fedora 24 machine but if you run into issues, drop a comment and I'll look into it.

.. _NEURON: http://www.neuron.yale.edu/neuron/
