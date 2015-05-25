ROS groovy on Fedora 18
#######################
:date: 2013-03-28 04:33
:author: ankur
:category: Tech
:tags: Robotics
:slug: ros-groovy-on-fedora-18

|ros-groovy|

ROS? What is ROS?
-----------------

ROS is the `Robot Operating System`_. It provides a huge set of software
that can be used to robotics research. It provides simulators,
algorithms and well, a lot more. For example, it lets one interface with
the `PR2 robot`_!

I've only learnt of ROS now, during my masters. However, if you're an
undergrad that is interested in AI and robotics, it's a great tool to
know. Look it up!

Groovy?!
--------

`Ros Groovy`_ is the latest ROS release. The older one is `Fuerte`_.
There are quite a few `changes in Groovy`_, one of the biggest ones
being the new build system "`Catkin`_\ ". A lot of the software has been
upgraded too. One of my project members gave Groovy a whirl and was
impressed with the improvements.

ROS and Fedora??
----------------

For the time being, the `Robotics SIG is working on packaging Fuerte`_.
The new build system will take some time to figure out. While it works
well to compile from source, it doesn't quite work well when you want to
make stand alone packages. We plan to move to Groovy in good time, but
for now Fuerte will have to do. If you're interested in helping out,
give us a shout on the `Robotics mailing list`_. There are quite a few
`packages that Rich has already submitted for review`_ that could use
your help.

Why Groovy?
-----------

Well, like I said, Groovy seems to have quite a few improvements. My
project team, has indicated that we will switch to Groovy sometime soon.
I therefore decided to use Groovy from the start.

How Groovy?
-----------

The `install instructions on the ROS wiki`_ work well. Do read the
complete document before you begin. I ended up hitting the some errors
already documented in the\ `troubleshooting section`_ and had to rebuild
`PCL`_. (Just so you know, building PCL can suck your system dry. It
took a couple of hours on my laptop which is a i5 2 core 4 thread
system. It used my processor continuously causing my laptop to overheat
and shut down twice. Keep your laptop near an AC when you build it!)

A few unsolved errors persist. I've asked questions on the `ros askbot
instance`_. I will file bugs upstream if nothing comes of it in a while.

.. _Robot Operating System: http://www.ros.org/
.. _PR2 robot: http://www.willowgarage.com/pages/pr2/overview
.. _Ros Groovy: http://www.ros.org/wiki/groovy
.. _Fuerte: http://ros.org/wiki/fuerte
.. _changes in Groovy: http://www.ros.org/wiki/groovy#Major_Updates
.. _Catkin: http://www.ros.org/wiki/groovy#New_Build_System_-_catkin
.. _Robotics SIG is working on packaging Fuerte: http://fedoraproject.org/wiki/SIGs/Robotics/ROS_Packaging
.. _Robotics mailing list: https://admin.fedoraproject.org/mailman/listinfo/robotics
.. _packages that Rich has already submitted for review: https://bugzilla.redhat.com/buglist.cgi?list_id=1231339&short_desc=ros&classification=Fedora&query_format=advanced&bug_status=NEW&short_desc_type=anywords&component=Package%20Review&product=Fedora
.. _install instructions on the ROS wiki: http://www.ros.org/wiki/groovy/Installation/Fedora
.. _troubleshooting section: http://www.ros.org/wiki/groovy/Installation/Fedora#Troubleshooting
.. _PCL: http://www.pointclouds.org/downloads/
.. _ros askbot instance: http://answers.ros.org/questions/

.. |ros-groovy| image:: http://ankursinha.in/wp/wp-content/uploads/2013/03/ros-groovy.png?w=300
   :target: http://ankursinha.in/wp/wp-content/uploads/2013/03/ros-groovy.png
