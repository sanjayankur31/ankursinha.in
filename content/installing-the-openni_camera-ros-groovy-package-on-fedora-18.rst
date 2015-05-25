Installing the openni_camera ros groovy package on Fedora 18
############################################################
:date: 2013-04-08 15:09
:author: ankur
:category: Tech
:tags: Fedora
:slug: installing-the-openni_camera-ros-groovy-package-on-fedora-18

I needed to install the `openni\_camera`_ `ROS Groovy`_ package on my
Fedora 18 system. I ran into a few issues which I managed to solve.
Documenting it all here for any one else who might need it:

You need to clone the git repository in your catkin workspace src
directory, and then build the package using catkin:

::

    $ cd ~/ros_catkin_ws/src #your catkin source directory
    $ git clone https://github.com/ros-drivers/openni_camera

The Cmakelists.txt file looks for openni via a cmake system which
doesn't work in Fedora due to missing pkg-config files. This patch will
fix the CMakeLists.txt file for you. I've `hosted the patch here`_ for
your convenience.

::

    [ankur@localhost  openni_camera(groovy-devel *%=)]$ diff -u CMakeLists.txt.orig CMakeLists.txt
    --- CMakeLists.txt.orig 2013-04-08 14:40:39.798336741 +1000
    +++ CMakeLists.txt      2013-04-08 14:43:14.466829031 +1000
    @@ -5,9 +5,11 @@
     find_package(Boost COMPONENTS system filesystem thread REQUIRED)

     find_package(PkgConfig)
    -pkg_check_modules(PC_LIBOPENNI REQUIRED libopenni)
    +# pkg_check_modules(PC_LIBOPENNI REQUIRED libopenni)
    +FIND_PATH(PC_LIBOPENNI_INCLUDE_DIRS "XnOpenNI.h" "OpenNIConfig.h" HINTS "$ENV{OPEN_NI_INCLUDE}" "/usr/include/ni")
    +FIND_LIBRARY(PC_LIBOPENNI_LIBRARIES NAMES OpenNI libOpenNI HINTS "$ENV{OPEN_NI_LIB}" "/usr/lib64")

    -#message("Hello world ${PC_LIBOPENNI_LIBRARIES} ${PC_LIBOPENNI_INCLUDEDIR}")
    +message("Hello world ${PC_LIBOPENNI_LIBRARIES} ${PC_LIBOPENNI_INCLUDE_DIRS}")

     generate_dynamic_reconfigure_options(cfg/OpenNI.cfg)

    [ankur@localhost  openni_camera(groovy-devel *%=)]$

Once done patching, install the openni-devel package

::

    $ sudo yum install openni-devel

Then, simply run the catkin make command:

::

    $ cd ~/ros_catkin_ws
    $ catkin_make_isolated --install -DSETUPTOOLS_DEB_LAYOUT=OFF --pkg openni_camera

That's all. The package should now be set up.

.. _openni\_camera: http://ros.org/wiki/openni_camera
.. _ROS Groovy: http://www.ros.org/wiki/groovy
.. _hosted the patch here: https://github.com/sanjayankur31/ros-work/blob/master/patches/openni_camera-CMakeLists.patch
