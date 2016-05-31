Some tips and tricks for running simulations on a cluster
#########################################################
:date: 2016-05-31 19:17:32
:author: ankur
:category: Research
:tags: Bash, Computational neuroscience, Git, Linux, NEST, Programming, Fedora
:slug: some-tips-and-tricks-for-running-simulations-on-a-cluster
:summary: I use the cluster here at university to run my simulations in Nest_. This post documents some tips and tricks I've come up with to make my cluster tasks easier.


To begin with, you must use a terminal multiplexer! I use `Byobu with tmux <http://byobu.org/>`__ to multiplex a single SSH session. I use it on all my machines. It's an excellent tool.

Monitoring your jobs
--------------------

Three of my Byobu screens run these commands to monitor the queue and my jobs:

.. code:: bash

    watch -n 30 qstat main
    watch -n 30 qstat -B
    watch -n 30 /usr/local/maui/bin/showq -u asinha

:code:`showq` may be installed elsewhere. Use :code:`which showq` to locate it. More information on the commands can be found in their manuals:

.. code:: bash

    man watch
    man qstat

Remember, to find a man page, you can use the :code:`apropos` command.

I run all my simulations in a specific directory on the shared data disk. I usually also monitor this folder. It gives me an idea of how much my simulations have progressed. Something like this works:

.. code:: bash

    watch -n 30 'du -sch *' # in the directory that stores simulation results*

Use Git
-------

Of course. If you make frequent changes, you must use a version control system. I stick to :code:`git` myself. You can use :code:`svn` or :code:`hg` if you wish - whatever floats your boat.

An issue I've stumbled upon while working with the cluster is that the program you want it to run is not loaded into memory until your job begins to run. So, if you want to run a certain version of your program on the cluster, say some version_1, you must not make any changes to this version until the queued job has begun to run. This is extremely inconvenient, especially if you make frequent changes to your simulations, as is often the case in research. I would, for example, like to queue separate jobs in parallel for a myriad of tiny changes and then compare results.

Enter `git work-tree <https://git-scm.com/docs/git-worktree>`__! The simplest solution to the aforementioned issue is to checkout different work-trees for commits you want to test and queue up jobs for each individually. This would work really well. Once the simulation finishes, you can remove the work-tree.

Unfortunately, clusters usually run stable long term support oriented versions of Linux distributions - EL/CentOS/Scientific. As a result, it's quite probable that the version of git on the cluster doesn't support work-trees - as is the case with the cluster I use. I came up with a workaround which works somewhat like work-trees - I manually clone my source repository to a temporary location, checkout the commit I want to run (which is what work-trees sort of are), and set up a job that runs this particular simulation version. It uses two scripts:

- A template PBS script for the simulation run. This will be passed to :code:`qsub`.
- A script that clones my repo, checks out the required commit, completes the template script, and calls :code:`qsub` to queue up the job.

The first is a simple PBS script:

.. code:: bash

    # File: run-sim.sh

    #PBS -l walltime=48:00:00
    #PBS -l nodes=50
    #PBS -m abe
    #PBS -N nest_v_s

    module unload mpi/mpich-x86_64
    module load mvapich2-1.7

    SIM_PATH="/stri-data/asinha/simulations-nest/"
    SIM_TIME=""
    PROGRAM_PATH="$SIM_PATH""$SIM_TIME""/Sinha2016/src/Sinha2016.py"
    RESULT_PATH="$SIM_PATH""$SIM_TIME""/result/"
    NUM_NODES=50

    echo ------------------------------------------------------
    echo 'Job is running on nodes'; cat $PBS_NODEFILE
    echo ------------------------------------------------------
    echo PBS: qsub is running on $PBS_O_HOST
    echo PBS: originating queue is $PBS_O_QUEUE
    echo PBS: executing queue is $PBS_QUEUE
    echo PBS: working directory is $PBS_O_WORKDIR
    echo PBS: execution mode is $PBS_ENVIRONMENT
    echo PBS: job identifier is $PBS_JOBID
    echo PBS: job name is $PBS_JOBNAME
    echo PBS: node file is $PBS_NODEFILE
    echo PBS: current home directory is $PBS_O_HOME
    echo PBS: PATH = $PBS_O_PATH
    echo ------------------------------------------------------

    echo "ANKUR>> Begun at $SIM_TIME"
    echo "ANKUR>> Script: ${0}"

    mkdir -pv $RESULT_PATH
    cd $RESULT_PATH

    /usr/local/bin/mpiexec -n $NUM_NODES python $PROGRAM_PATH

    END_TIME=$(date +%Y%m%d%H%M)
    echo "ANKUR>> Ended at $END_TIME"


It sets up the required PBS options, then loads the MPI module I wish to use. It creates a directory where my simulation's results will be stored, enters it, and then uses :code:`mpiexec` to run my Python program.

The second script is a wrapper that clones the required commit, sets up the correct paths in the above script and the calls :code:`qsub`:

.. code:: bash

    # File: setup-job.sh

    SOURCE_PATH="/home/asinha/Documents/02_Code/00_repos/00_mine/Sinha2016/"
    GIT_COMMIT=""
    SIM_PATH="/stri-data/asinha/simulations-nest/"
    SIM_TIME=$(date +%Y%m%d%H%M)
    RUN_SCRIPT="scripts/cluster/nest-runsim.sh"
    RUN_NEW=""
    ERROR="no"
    NUM_NODES=50
    CUR_SIM_PATH=""

    function queue_task
    {
        pushd "$CUR_SIM_PATH"
            qsub "$RUN_NEW"
        popd
    }

    function setup_env
    {
        CUR_SIM_PATH="$SIM_PATH""$SIM_TIME"
        echo "This simulation will run in: $CUR_SIM_PATH"
        mkdir -pv "$CUR_SIM_PATH"

        pushd "$CUR_SIM_PATH"
            echo "Cloning source repository..."
            git clone "$SOURCE_PATH" "Sinha2016"

            pushd "Sinha2016"
                echo "Checking out commit $GIT_COMMIT..."
                git checkout -b this_sim "$GIT_COMMIT"
                if [ "$?" -ne 0 ]
                then
                    echo "Error occured. Could not checkout $GIT_COMMIT. Exiting..."
                    ERROR="yes"
                fi
            popd

            if [ "xyes" ==  x"$ERROR" ] 
            then
                exit -1
            fi

            RUN_NEW="nest_""$GIT_COMMIT"".sh"
            echo "Setting up $RUN_NEW..."
            cp "$SOURCE_PATH""$RUN_SCRIPT" "$RUN_NEW" -v
            sed -i "s|nest_v_s|nest_$GIT_COMMIT|" "$RUN_NEW"
            sed -i "s|nodes=.*|nodes=$NUM_NODES|" "$RUN_NEW"
            sed -i "s|NUM_NODES=.*|NUM_NODES=$NUM_NODES|" "$RUN_NEW"
            sed -i "s|SIM_TIME=.*|SIM_TIME=$SIM_TIME|" "$RUN_NEW"
        popd
    }

    function usage
    {
        echo "Usage: $0"
        echo "Queue up a job to run a particular git commit"
        echo "$0 <git_commit> <number_nodes>"
    }

    if [ "$#" -ne 2 ];
    then
        echo "Error occurred. Exiting..."
        echo "Received $# arguments. Expected: 3"
        usage
        exit -1
    fi

    GIT_COMMIT="$1"
    NUM_NODES="$2"
    setup_env
    queue_task

    exit 0


This takes two arguments, as the :code:`usage` function will tell you. The first argument is the commit you want to run the simulation for, and the second is the number of nodes you want to use. It'll clone your repository to a temporary location and checkout this specified commit. Then, it'll modify the first script :code:`run-sim.sh` to set up the correct path to the code and also correctly specify the number of nodes you'd want to request. Finally, once all this is done, it'll call :code:`qsub run-sim.sh` to queue up your job. I use unique date stamps as directory names to distinguish between simulation runs, but you can use another unique identifier.

Now, this copy of your code, at the specified commit will be used for the job you've queued. You can merrily go about tinkering with the main source repo without affecting queued up jobs. Yay!

Even though I've used Python here, you can use similar scripts for compiled languages. You'll simply have to compile your executable after you checkout the required commit.

Other miscellaneous stuff
-------------------------

My lab mate, Alex, recently introduced me to `Anaconda <https://www.continuum.io/downloads>`__. It's a great tool for that lets you install packages in your user specific directory. It contains quite a few python and other related packages. No need to use :code:`sudo` with it, and you can use :code:`pip` etc. with it too. It even lets you set up virtual environments and things.

I think that's it for today. I'll update the post with other things I find/learn as I continue my adventures with the cluster.

.. _Nest: https://github.com/nest/nest-simulator
