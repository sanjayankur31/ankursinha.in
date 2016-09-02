Using NEURON - Part II
######################
:date: 2016-09-02 13:39:16
:author: ankur
:category: Research
:tags: Fedora, Neuron, Computational neuroscience
:slug: using-neuron-part-ii
:summary: This second post on using NEURON_ documents how to run an existing model, for example, from ModelDB_.

ModelDB_ is a popular resource where the computational neuroscience community puts up models that were used in various publications. Since I'm quite new to NEURON_, I thought I'd play with some existing models to get a hang of things. Here I document how to run an existing model.

ModelDB_ has quite a few models that use NEURON_. Find one that suits you. I'll pick `L5b PC model constrained for BAC firing and perisomatic current step firing (Hay et al., 2011) <https://senselab.med.yale.edu/ModelDB/ShowModel.cshtml?model=139653>`__ for now.

Download the model
-------------------

`Download the zip <https://senselab.med.yale.edu/modeldb/eavBinDown.cshtml?o=139653&a=23&mime=application/zip>`__ file from the model page to a convenient location. There's a link right on the top of the page. Extract it.

.. code:: bash

    $ unzip L5bPCmodelsEH.zip
    $ lash
    total 668K
    4.0K drwxr-xr-x. 7 asinha asinha 4.0K Mar 30  2013 L5bPCmodelsEH
    664K -rw-r-----. 1 asinha asinha 662K Sep  2 13:55 L5bPCmodelsEH.zip


Building and running the model
-------------------------------

Enter the directory:

.. code:: bash

    cd L5bPCmodelsEH/

NEURON_ code comprises of two sets of code files. You have the HOC files, and the NMODL files. NMODL files need to be compiled before the model can be run.

.. code:: bash

    $ ~/dump/neuron-installation/x86_64/bin/nrnivmodl mod
    Creating x86_64 directory for .o files.

    /home/asinha/dump/neuron-blog/L5bPCmodelsEH
    mod/CaDynamics_E2.mod mod/Ca_HVA.mod mod/Ca_LVAst.mod mod/epsp.mod mod/Ih.mod mod/Im.mod mod/K_Pst.mod mod/K_Tst.mod mod/Nap_Et2.mod mod/NaTa_t.mod mod/NaTs2_t.mod mod/SK_E2.mod mod/SKv3_1.mod
    CaDynamics_E2.mod Ca_HVA.mod Ca_LVAst.mod epsp.mod Ih.mod Im.mod K_Pst.mod K_Tst.mod Nap_Et2.mod NaTa_t.mod NaTs2_t.mod SK_E2.mod SKv3_1.mod
    "/home/asinha/dump/neuron-installation/x86_64/bin/nocmodl" CaDynamics_E2
    Translating CaDynamics_E2.mod into CaDynamics_E2.c
    Thread Safe
    "/home/asinha/dump/neuron-installation/share/nrn/libtool" --tag=CC --mode=compile mpicc -DHAVE_CONFIG_H  -I. -I.. -I"/home/asinha/dump/neuron-installation/include/nrn" -I"/home/asinha/dump/neuron-installation/x86_64/lib"      -O2 -g -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic -c -o CaDynamics_E2.lo CaDynamics_E2.c
    libtool: compile:  mpicc -DHAVE_CONFIG_H -I. -I.. -I/home/asinha/dump/neuron-installation/include/nrn -I/home/asinha/dump/neuron-installation/x86_64/lib -O2 -g -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic -c CaDynamics_E2.c  -fPIC -DPIC -o .libs/CaDynamics_E2.o
    CaDynamics_E2.c:94:34: warning: missing braces around initializer [-Wmissing-braces]
      static VoidFunc hoc_intfunc[] = {
      ...
      ....
      ...
      ...


You'll see a new :code:`x86_64` directory which contains the compiled code. Now, simply run NEURON_ as usual. If everything went well, the simulation will run:

.. code:: bash

    $ ~/dump/neuron-installation/x86_64/bin/nrngui mosinit.hoc

Remember that you must run :code:`nrngui` in the directory where the :code:`x86_64` directory resides for NEURON_ to find it.

That's it!

.. _NEURON: http://www.neuron.yale.edu/neuron/
.. _ModelDB: https://senselab.med.yale.edu/ModelDB/ModelList.cshtml?id=1882
