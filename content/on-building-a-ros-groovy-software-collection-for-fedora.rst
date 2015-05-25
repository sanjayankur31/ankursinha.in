On building a ROS Groovy Software collection for Fedora
#######################################################
:date: 2013-08-27 23:47
:author: ankur
:category: Tech
:tags: Fedora
:slug: on-building-a-ros-groovy-software-collection-for-fedora

ROS currently has two stable versions: `Fuerte`_ and `Groovy`_; with
another one coming out: `Hydro`_. All of them are designed to run in
parallel. Having all three of them available in Fedora is difficult,
since they packages will conflict. It therefore makes sense to keep only
one version of ROS available in the main Fedora repositories.

The first issue we ran into was getting a list of packages to build for
ROS, and what order to they should be built in. Some hacking on bloom
has made this simpler. I've documented what needs to be done in `this
git commit message`_. Now, I have a directory of `template files`_ that
I need to complete and build RPMs off.

Recently, I looked up `SCL (Software collections)`_ which are designed
to permit the parallel install of software on a system. I've recently
started working on making a ROS-Groovy SCL. Here's what the spec for the
`metadata rpm`_ looks like.

Once the rpm has been built, using
``rpmbuild -ba --define 'scl ros-groovy'``, it must be placed in a
temporary repository and a `new configuration file`_ created so that the
other packages of the SCL can be built in mock. I've just finished
building the first package according to the `build sequence`_: catkin
(`rpm`_, `srpm`_, `spec`_).

Even though the templates fill up some parts of the spec, a lot of work
still needs to be done to complete them. It's going to take time, but I
hope to be able to do them all one by one. The fun part is that scl
packages can be easily converted to Fedora repository packages. This
way, we can maintain multiple SCLs for ROS versions, and choose one of
them as the official Fedora supported version when we get to that.

If you're interested in helping out, get in touch with me!

.. _Fuerte: http://ros.org/wiki/fuerte/
.. _Groovy: http://www.ros.org/wiki/groovy/
.. _Hydro: http://www.ros.org/wiki/hydro
.. _this git commit message: https://github.com/sanjayankur31/bloom/commit/d5c5f636e11b6e4b76ed82fdfd69879e76964f62
.. _template files: http://ankursinha.fedorapeople.org/fedora-ros-groovy/TEMPLATES/
.. _SCL (Software collections): http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation/1/html/Software_Collections_Guide/
.. _metadata rpm: http://ankursinha.fedorapeople.org/fedora-ros-groovy/SPECS/ros-groovy.spec
.. _new configuration file: http://ankursinha.fedorapeople.org/fedora-ros-groovy/OTHER/fedora-19-ros-groovy-x86_64.cfg
.. _build sequence: http://ankursinha.fedorapeople.org/fedora-ros-groovy/TEMPLATES/BUILDORDER
.. _rpm: http://ankursinha.fedorapeople.org/fedora-ros-groovy/RPMS/ros-groovy-catkin-0.5.71-1.fc19.noarch.rpm
.. _srpm: http://ankursinha.fedorapeople.org/fedora-ros-groovy/SRPMS/ros-groovy-catkin-0.5.71-1.fc19.src.rpm
.. _spec: http://ankursinha.fedorapeople.org/fedora-ros-groovy/SPECS/ros-groovy-catkin.spec
