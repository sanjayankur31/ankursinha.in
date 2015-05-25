Installing gazebo with your ros groovy install on Fedora 18
###########################################################
:date: 2013-04-08 22:04
:author: ankur
:category: Tech
:tags: Fedora
:slug: installing-gazebo-with-your-ros-groovy-install-on-fedora-18

I need to use the `PR2-simulator package`_ on my groovy installation.
One must first set up `gazebo`_ for this.

Installing gazebo is pretty straight forward `as described in this
post`_.

If you used the `instructions from the ros wiki`_, you'd have a ros
workspace set up.

A few devel packages are required though. I think the following list
covers it. Look out for any build errors. If there are any more packages
to be installed, the error messages will tell you:

::

    sudo yum install freeimage-devel player-devel libtool-ltdl-devel cegui-devel libtar-devel protobuf-devel libXaw-devel ois-devel

    cd ros_ws #your ros workspace

    #common_rosdeps: required by ogre
    rosws set common_rosdeps --hg https://kforge.ros.org/common/rosdepcore
    !source setup.sh
    rosws update common_rosdeps
    rosmake common_rosdeps

    #vizualization_common. The fedora ogre package doesn't appear to cut it.
    rosws set visualization_common --svn https://code.ros.org/svn/ros-pkg/stacks/visualization_common/trunk
    source setup.sh
    rosws update visualization_common
    rosmake visualization_common

    #gazebo
    rosws set simulator_gazebo --svn https://code.ros.org/svn/ros-pkg/stacks/simulator_gazebo/trunk
    source setup.sh
    rosws update simulator_gazebo
    rosmake simulator_gazebo

It'll take a while to install. Took about 30 minutes on my system. That
completes the install. I'm still trying to figure out how to use it
though. Maybe I'll write another post when I get somewhere with that.

It's worth mentioning that `Rich`_ submitted `gazebo for review
already`_. It has a few build requires that need to be reviewed.

EDIT: While this appears to install gazebo properly, it doesn't run. It
gives me an OGRE missing openGL error, but OGRE is indeed installed with
openGL support.

.. _PR2-simulator package: http://www.ros.org/wiki/pr2_simulator
.. _gazebo: http://www.ros.org/wiki/simulator_gazebo
.. _as described in this post: http://answers.ros.org/question/49397/how-to-install-gazebo-from-source-in-ros-fuerte/
.. _instructions from the ros wiki: http://www.ros.org/wiki/groovy/Installation/Fedora
.. _Rich: http://fedoraproject.org/wiki/User:Rmattes
.. _gazebo for review already: https://bugzilla.redhat.com/show_bug.cgi?id=825409
