F-I curves for the AdEx neuron model - tonic spiking without adaptation
#######################################################################
:date: 2015-06-24 21:30:16
:author: ankur
:category: Research
:tags: Computational neuroscience
:slug: f-i-curves-for-the-adex-neuron-model-without-adaptation
:summary: I'm looking into the AdEx neuron model right now and this post has some information on how the model's tonic spiking behaviour varies with different input currents and reset voltages.

I'm looking into the `Adaptive exponential integrate and fire neuron model`_ (AdEx) in my research at the moment. This neuron model includes various improvements over the simple `Leaky integrate and fire`_ (LIF) neuron model. AdEx, depending on various parameters, `can exhibit different spiking behaviours`_. I'm looking at the simplest one at the moment - tonic spiking in the absence of adaptation **(a,b=0)**. With this parameter set, the AdEx is simplified to a simple LIF model. The figure below shows the "firing rate (spikes per second) vs current" graph for different reset voltages (-58mV, -60mV, -65mV, -70mV).

.. image:: {static}/images/AdEx-ab0-FI.png
    :align: center
    :width: 800px
    :target: {static}/images/AdEx-ab0-FI.png
    :alt: AdEx F-I curve with different reset voltages

The variation here is quite expected - if the neuron is reset to a lower voltage after a spike, it'll take more time to spike again and the firing rate will be less as a result. The second figure shows the membrane potential plotted as a function of time with the reset voltage at -70mV and the external current being given to the neuron is 500pA.

.. image:: {static}/images/adex-70mV-500pA.png
    :align: center
    :width: 800px
    :target: {static}/images/adex-70mV-500pA.png
    :alt: AdEx tonic spiking without adaptation membrane potential with 70mV reset voltage and 500pA external current.

This graph is self-explanatory too. The upswing in membrane potential brought about by the exponential term is quite apparent. The lack of adaptation is shown by the constant inter spike interval (ISI). In the presence of adaptation, the ISI would steadily increase. I've looked in to that too, but I haven't a pretty graph to show at the moment. 

The Auryn_ code required to generate the graphs is given below. You can use a different simulator - Nest_ or PyNN_ and so on - and you should receive the same results. I've already verified_ with Brian_.

.. code-block:: c

    #include "auryn_global.h"
    #include "auryn_definitions.h"
    #include "System.h"
    #include "SpikeMonitor.h"
    #include "VoltageMonitor.h"
    #include "Logger.h"
    #include "AdExGroup.h"

        int
    main ( int ac, char *av[] )
    {

        mpi::environment env(ac, av);
        mpi::communicator world;
        communicator = &world;
        logger = new Logger("output.log",world.rank(),PROGRESS,EVERYTHING);
        sys = new System(&world);

        logger->msg("Setting up single neuron ...",PROGRESS,true);
        AdExGroup * neurons_e = new AdExGroup(1);


        /* Parameters for the model */
        neurons_e->set_c_mem(200e-12);
        float g_leak = 10.0;
        neurons_e->set_g_leak((g_leak*1e-9));
        neurons_e->set_e_rest(-70e-3);
        neurons_e->set_e_thr(-50e-3);
        neurons_e->set_a((0.0/g_leak));
        neurons_e->set_tau_w(30e-3);
        neurons_e->set_b((0e-3/g_leak));
        neurons_e->set_e_reset(-58e-3);

        /* External current */
        neurons_e->set_bg_current(0,2000e-3/g_leak);

        /* Output files */
        SpikeMonitor * smon = new SpikeMonitor(neurons_e, "spikes.ras");
        VoltageMonitor * vmon = new VoltageMonitor(neurons_e, 0, "voltages.txt");

        /* Run the simulation */
        sys->run(81);

        return 0;
    }

The program outputs two files - a ras file with spike times in it that one can use to calculate the firing rate of the neuron; and a voltages file if you'd like to plot the membrane potential too. More information on these can be found in the `Auryn documentation`_. 

I maintain `an autotoolised version`_ of Auryn that you can use. I track the development branch there, though, so if you do find bugs, please report them upstream. 

I'm looking into AdEx in quite a bit of detail at the moment. I'll write more about it when I run more simulations and generate graphs and things that are worth sharing. Cheers!


.. _Adaptive exponential integrate and fire neuron model: http://www.scholarpedia.org/article/Adaptive_exponential_integrate-and-fire_model
.. _Leaky integrate and fire: http://icwww.epfl.ch/~gerstner/SPNM/node26.html
.. _Auryn: https://github.com/fzenke/auryn
.. _can exhibit different spiking behaviours: http://link.springer.com/article/10.1007/s00422-008-0264-7
.. _Auryn documentation: https://fzenke.net/auryn/doku.php?id=start
.. _an autotoolised version: https://github.com/sanjayankur31/auryn/tree/autotoolize
.. _Nest: http://nest.github.io/nest-simulator/
.. _PyNN: https://github.com/NeuralEnsemble/PyNN
.. _verified: https://github.com/sanjayankur31/adex-pybrian-tests/tree/master/results
.. _Brian: http://briansimulator.org/
