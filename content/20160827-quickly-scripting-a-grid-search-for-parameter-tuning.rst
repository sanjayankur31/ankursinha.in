Quickly scripting a grid-search for parameter tuning
####################################################
:date: 2016-08-27 10:10:04
:author: ankur
:category: Research
:tags: Computational neuroscience, Fedora, Git, Programming, Python
:slug: quickly-scripting-a-grid-search-for-parameter-tuning
:summary: Finding the right set of parameters is quite important in a lot of research - machine learning and computational neuroscience are two fields that I know of. I recently had to ascertain the optimal parameter set for my simulations too. I came up with a quick script to do it for me.

A lot of models rely on different parameters. In my cortical models, these are usually variables like conductances of different sets of synapses, the sparsity of different synapse sets, learning rates of spike time dependent plasticity learning rules and so on. Given how finely tuned neuronal networks sometimes are, models don't depict the expected behaviours for the entire domain of parameter values. Instead, we often must find the right ranges of these parameters.

In my simulations, I have some sets of synapses, and in my recent investigations, I needed to find the right "balance" between them. The standard way of going about this is to carry out an organised parameter search, what I think is referred to as a "grid search". In a grid search, each point in the parameter space is tested to find the ranges where the required behaviour is simulated - really just simple brute force at play here. Now, since I have three parameters to test, my parameter space would be a three dimensional grid - the Cartesian product of the domains of the three parameters - :code:`p1 x p2 x p3`. For all possible ordered sets of p1, p2, and p3, I need to run my simulation - the number of possible combinations being :code:`n(p1) x n(p2) x n(p3)`, where :code:`n` is the cardinality of each set.

Of course, I wrote myself a script. Modifying the parameters by hand and then queuing up all these simulations manually on the cluster would just take too much time. 

The idea
--------

It's a simple Python script, and this fits well with my `workflow <20160531-some-tips-and-tricks-for-running-simulations-on-a-cluster.rst>`__ (which intensively uses Git and scripts to queue jobs on the cluster). The idea is:

- create a new Git branch for the grid search (so we keep things organised!)
- use a simple scripting language to iterate over the parameter space
- modify the parameters in the simulation source code
- create a new commit for each point in the parameter space
- queue up all these commits on the cluster


The script
----------

I've used Python - you can use another scripting language that you prefer. I wouldn't recommend a shell script - even though it's powerful, handling arrays and floats and the sort is quite tedious in bash.

.. code:: Python

    #!/usr/bin/env python3
    """
    Copyright 2016 Ankur Sinha
    Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    """

    import sys
    import os
    import numpy
    import subprocess
    import datetime


    class GridSearch:

        """Set up your simulations for a grid search.


        This will modify the source in a branch, make changes, commit
        and then you can set these commits up on the cluster.
        """

        def __init__(self):
            """Initialise."""
            self.source = "/path/to/source/file/"
            self.branch = "master"

        def usage(self):
            """Print usage."""
            print("Usage:", file=sys.stderr)
            print("python3 grid_search.py <branch>", file=sys.stderr)
            print("Branch MUST be specified.", file=sys.stderr)

        def setup(self, branch, range_dict):
            """Set it up."""
            self.branch = branch

            if len(range_dict['param1']) == 1:
                self.param1_increment = 0.5
                self.param1_min = range_dict['param1'][0]
                self.param1_max = range_dict['param1'][0] + self.param1_increment
            elif len(range_dict['param1']) == 3:
                self.param1_increment = range_dict['param1'][2]
                self.param1_min = range_dict['param1'][0]
                self.param1_max = range_dict['param1'][1] + self.param1_increment
            else:
                print("param1 not found in dict. Exiting.", file=sys.stderr)
                return False

            if len(range_dict['param2']) == 1:
                self.param2_increment = 0.5
                self.param2_min = range_dict['param2'][0]
                self.param2_max = range_dict['param2'][0] + self.param2_increment
            elif len(range_dict['param2']) == 3:
                self.param2_increment = range_dict['param2'][2]
                self.param2_min = range_dict['param2'][0]
                self.param2_max = range_dict['param2'][1] + self.param2_increment
            else:
                print("param2 not found in dict. Exiting.", file=sys.stderr)
                return False

            if len(range_dict['param3']) == 1:
                self.param3_increment = 0.5
                self.param3_min = range_dict['param3'][0]
                self.param3_max = range_dict['param3'][0] + self.param3_increment
            elif len(range_dict['param3']) == 3:
                self.param3_increment = range_dict['param3'][2]
                self.param3_min = range_dict['param3'][0]
                self.param3_max = range_dict['param3'][1] + self.param3_increment
            else:
                print("param3 not found in dict. Exiting.", file=sys.stderr)
                return False

            return True

        def run(self):
            """Run."""
            # checkout the branch
            git_args = ["checkout", "-b", "grid_search-{}".format(
                str(datetime.date.today())), self.branch]
            subprocess.call(['git'] + git_args)

            for param1 in numpy.arange(self.param1_min, self.param1_max, self.param1_increment):
                for param2 in numpy.arange(self.param2_min, self.param2_max, self.param2_increment):
                    for param3 in numpy.arange(self.param3_min, self.param3_max, self.param3_increment):

                        sed_args_param1 = ['sed', '-i',
                                    "s/param1 = .*$/param1 = {}/".format(param1),
                                    self.source]
                        subprocess.call(sed_args_param1)

                        sed_args_param2 = ['sed', '-i',
                                    "s/param2 = .*$/param2 = {}/".format(param2),
                                    self.source]
                        subprocess.call(sed_args_param2)

                        sed_args_param3 = ['sed', '-i',
                                    "s/param3 = .*$/param3 = {}/".format(param3),
                                    self.source]
                        subprocess.call(sed_args_param3)

                        git_args = ["add", self.source]
                        subprocess.call(['git'] + git_args)

                        commit_msg = """{} {} {} {}""".format(
                            str(datetime.date.today()), param1,
                            param2, param3)

                        git_args = ["commit", "-m", commit_msg]
                        subprocess.call(['git'] + git_args)

            git_args = ["checkout", self.branch]
            subprocess.call(['git'] + git_args)

    if __name__ == "__main__":
        search = GridSearch()
        if len(sys.argv) != 2:
            search.usage()
            sys.exit(-1)
        else:
            branch = sys.argv[1]
            # dictionary that holds the required grid ranges
            # specify min, max if want a grid search, else specify only one value
            # if you specify max, min, you must specify increment
            setup_dict = {
                'param1': [3.],
                'param2': [0.5, 3., 0.5],
                'param3': [-5., -30., -5.],
            }
            if search.setup(branch, setup_dict):
                search.run()

Since I'm calling :code:`sed` to modify my source and replace the parameter values, the only requirement here is that my source code needs to have the three lines (look at the regular expressions):

.. code:: Python

    param1 = ..
    param2 = ..
    param3 = ..

If all goes well, you should have a new branch:

.. code:: console

    * 74866b6 - (3 months ago) Bugfix - neurons first, synapses later — Ankur Sinha (Ankur Sinha Gmail)
    | * fd6a7fa - (5 days ago) 2016-08-22 3.0 3.0 -30.0 — Ankur Sinha (Ankur Sinha Gmail) (origin/grid_search-2016-08-22, grid_search-2016-08-22)
    | * 33c95be - (5 days ago) 2016-08-22 3.0 3.0 -25.0 — Ankur Sinha (Ankur Sinha Gmail)
    | * 51f96c1 - (5 days ago) 2016-08-22 3.0 3.0 -20.0 — Ankur Sinha (Ankur Sinha Gmail)
    | * e8c106e - (5 days ago) 2016-08-22 3.0 3.0 -15.0 — Ankur Sinha (Ankur Sinha Gmail)
    | * eaa7341 - (5 days ago) 2016-08-22 3.0 3.0 -10.0 — Ankur Sinha (Ankur Sinha Gmail)
    | * 4597114 - (5 days ago) 2016-08-22 3.0 3.0 -5.0 — Ankur Sinha (Ankur Sinha Gmail)
    | * a111e00 - (5 days ago) 2016-08-22 3.0 2.5 -30.0 — Ankur Sinha (Ankur Sinha Gmail)
    | * 5261f4b - (5 days ago) 2016-08-22 3.0 2.5 -25.0 — Ankur Sinha (Ankur Sinha Gmail)
    | * d10a686 - (5 days ago) 2016-08-22 3.0 2.5 -20.0 — Ankur Sinha (Ankur Sinha Gmail)
    | * 91bc10e - (5 days ago) 2016-08-22 3.0 2.5 -15.0 — Ankur Sinha (Ankur Sinha Gmail)
    | * add5188 - (5 days ago) 2016-08-22 3.0 2.5 -10.0 — Ankur Sinha (Ankur Sinha Gmail)
    | * c93c817 - (5 days ago) 2016-08-22 3.0 2.5 -5.0 — Ankur Sinha (Ankur Sinha Gmail)
    | * 8e779b9 - (5 days ago) 2016-08-22 3.0 2.0 -30.0 — Ankur Sinha (Ankur Sinha Gmail)
    | * 9f67e1c - (5 days ago) 2016-08-22 3.0 2.0 -25.0 — Ankur Sinha (Ankur Sinha Gmail)
    .....

Now, with the help of some bash hacking I get a list of all the commits I need to queue up in a single line:

.. code:: bash

    # list all commits reachable from grid_search.. branch but not from the base_branch
    $ git log base_branch..grid_search-2016-08-22  --oneline | cut -f1 -d" " | tr "\n" " " 
    fd6a7fa 33c95be 51f96c1 .. e8c106e eaa7341

Then, I use the bash :code:`for` construct to queue them all up as before:

.. code:: bash

    $ for commit in fd6a7fa 33c95be 51f96c1 .. e8c106e eaa7341; do ./start-job.sh "$commit" 32; sleep 1m; done

Note - I used the :code:`sleep` command to space out each job by a minute. This is because my workflow uses folder names which are timestamps of when the job was queued up, like this: :code:`201608121234` (YYYYMMDDHHMM). So, I can't have two commits starting at the same minute.

There are many ways of carrying out the same method. This is what I quickly came up with. `Scikit <http://scikit-learn.org>`__, for example has `methods for grid search <http://scikit-learn.org/stable/modules/grid_search.html>`__, but they don't gel well with my simulations.

Postprocessing all this data
-----------------------------

I have a bunch of scripts for post processing too - this grid search had 36 simulations, the postprocessing is still trudging along. The bigger question is: is there a good way of visualising all these results? I've had to resort to a spreadsheet - but if you have any suggestions, please do let me know. I really haven't found a nice front-end that would let me log results to a database and visualise them - over time, over parameters and so on - does anyone know one? What do people use to keep track of all their data?

Anyway, it's a long weekend here with Monday being a bank holiday. Enjoy the weekend, everyone!
