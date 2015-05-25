Extracting raw data from ros topics
###################################
:date: 2013-04-07 15:22
:author: ankur
:category: Research
:tags: Robotics
:slug: extracting-raw-data-from-ros-topics

Recently, I needed to extract raw data that we had collected from the
`PR2`_ robot. It's easy to collect data from `topics`_, using the
`rosbag`_ tool. You can collect data from multiple topics in one bag at
a time.

Here's an example command that collects data from the robot:

::

    rosbag record -b 1024 "/joint_states" -e "(/.*)_scan$" "torso_lift_imu/data" "/base_odometry/odom" "/camera/rgb/image_rect_color" "/camera/depth_registered/image_rect" --duration=1m --split -O /removable/recordings/20130403_1218_navtest_data.bag

The rosbag then looks like this:

::

    [ankur@localhost  bag-test]$ rosbag info 20130403_1218_navtest_data_0.bag
    path:        20130403_1218_navtest_data_0.bag
    version:     2.0
    duration:    58.8s
    start:       Apr 03 2013 15:40:18.91 (1364964018.91)
    end:         Apr 03 2013 15:41:17.68 (1364964077.68)
    size:        3.3 GB
    messages:    17035
    compression: none [3295/3295 chunks]
    types:       nav_msgs/Odometry      [cd5e73d190d741a2f92e81eda573aca7]
                 sensor_msgs/Image      [060021388200f6f0f447d0fcd9c64743]
                 sensor_msgs/JointState [3066dcd76a6cfaef579bd0f34173e9fd]
                 sensor_msgs/LaserScan  [90c7ef2dc6895d81024acba2ac42f369]
    topics:      /base_odometry/odom                   5516 msgs    : nav_msgs/Odometry
                 /base_scan                            1176 msgs    : sensor_msgs/LaserScan
                 /camera/depth_registered/image_rect   1640 msgs    : sensor_msgs/Image
                 /camera/rgb/image_rect_color          1653 msgs    : sensor_msgs/Image
                 /joint_states                         5875 msgs    : sensor_msgs/JointState
                 /tilt_scan                            1175 msgs    : sensor_msgs/LaserScan
    [ankur@localhost  bag-test]$

You can also filter out individual topics into individual bags with the
tool:

::

    [ankur@localhost  bag-test]$ rosbag filter --help
    Usage: rosbag filter [options] INBAG OUTBAG EXPRESSION

    EXPRESSION can be any Python-legal expression.

    The following variables are available:
     * topic: name of topic
     * m: message
     * t: time of message (t.secs, t.nsecs)

    Filter the contents of the bag.

    Options:
      -h, --help            show this help message and exit
      -p PRINT-EXPRESSION, --print=PRINT-EXPRESSION
                            Python expression to print for verbose debugging. Uses
                            same variables as filter-expression
    [ankur@localhost  bag-test]$

Various other tools are available to visualize the data. With `groovy`_,
you have `rqt\_bag`_

Since I needed the raw messages, I had to hack up a python script using
the `rosbag API`_.

::

    #!/usr/bin/python

    # Copyright 2010 Ankur Sinha
    # Author: Ankur Sinha
    #
    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.
    #
    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.
    #
    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <http://www.gnu.org/licenses/>.
    #
    # File : extractRawInfo.py
    #

    import rosbag
    import sys
    import os
    import pickle

    # Global variable for input file name

    def run():
        """
        Main run method. Calls other helper methods to get work done
        """

        if len(sys.argv) != 2:
            sys.stderr.write('[ERROR] This script only takes input bag file as argument.n')
        else:
            inputFileName = sys.argv[1]
            print "[OK] Found bag: %s" % inputFileName

            bag = rosbag.Bag(inputFileName)
            topicList = readBagTopicList(bag)

            while True:
                if len(topicList) == 0:
                    print "No topics in list. Exiting"
                    break
                selection  = menu(topicList)

                if selection == -92:
                    print "[OK] Printing them all"
                    for topic in topicList:
                        extract_data(bag, topic, inputFileName)
                    break
                elif selection == -45:
                    break
                else:
                    topic = topicList[selection]
                    extract_data(bag, topic, inputFileName)
                    topicList.remove(topicList[selection])

            bag.close()

    def extract_data (bag, topic, inputFileName):
        """
        Spew messages to a file

        args:
            topic -> topic to extract and print to txt file
        """

        outputFileName = os.path.splitext(os.path.split(inputFileName)[1])[0] + topic.replace("/","-") + ".txt"
        print "[OK] Printing %s" % topic
        print "[OK] Output file will be called %s." % outputFileName

        outputFh = open(outputFileName, "w")

        for topic, msg, t in bag.read_messages(topics=topic):
            pickle.dump(msg,outputFh)

        outputFh.close()
        print "[OK] DONE"

    def menu (topicList):
        """
        Print the user menu and take input

        args:
            topicList: tuple containing list of topics

        returns:
            selection: user selection as integer
        """

        i = 0
        for topic in topicList:
            print '[{0}] {1}'.format(i, topic)
            i = i+1
        if len(topicList) > 1:
            print '[{0}] Extract all'.format(len(topicList))
            print '[{0}] Exit'.format(len(topicList) + 1)
        else:
            print '[{0}] Exit'.format(len(topicList))

        while True:
            print 'Enter a topic number to extract raw data from:'
            selection = raw_input('>>>')
            if int(selection) == len(topicList):
                return -92 # print all
            elif int(selection) == (len(topicList) +1):
                return -45 # exit
            elif (int(selection) < len(topicList)) and (int(selection) >= 0):
                return int(selection)
            else:
                print "[ERROR] Invalid input"

    def readBagTopicList(bag):
        """
        Read and save the initial topic list from bag
        """
        print "[OK] Reading topics in this bag. Can take a while.."
        topicList = []
        for topic, msg, t in bag.read_messages():
            if topicList.count(topic) == 0:
                topicList.append (topic)

        print '{0} topics found:'.format(len(topicList))
        return topicList

    if __name__ == "__main__":
        run()

I've `hosted it on my github repository`_. It'll be easier to
read/download it from there if you need to.

.. _PR2: http://www.willowgarage.com/pages/pr2/overview
.. _topics: http://www.ros.org/wiki/Topics
.. _rosbag: http://www.ros.org/wiki/rosbag
.. _groovy: http://www.ros.org/wiki/groovy/
.. _rqt\_bag: http://ros.org/wiki/rqt_bag
.. _rosbag API: http://www.ros.org/wiki/rosbag/Code%20API#py_api
.. _hosted it on my github repository: https://github.com/sanjayankur31/ros-work/blob/master/helper-scripts/extractRawInfo.py
