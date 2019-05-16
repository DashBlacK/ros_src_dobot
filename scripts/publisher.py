#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Pose
import time
from math import sin, cos

def talker():
    pub = rospy.Publisher('geometry_pose', Pose, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(0.5) # 10hz

    t = 0
    xpos = 255.0916
    ypos = -76.1602
    zpos = 7.0887
    xrot = 36.1545
    switch = 0
    gripper = 0
    # simple repetitive motion - modify to fit your own
    while 1:
	msg = Pose()
	xpos = 265.0916
    	ypos = -60.1602
        zpos = .7887
        xrot = 36.1545
	msg.position.x = xpos
	msg.position.y = ypos
        msg.position.z = zpos
	msg.orientation.x = gripper
 	pub.publish(msg)
	time.sleep(2)
	gripper = 1
	msg.orientation.x = gripper
 	pub.publish(msg)
	time.sleep(3)
	xpos = 265.3635
    	ypos = -94.0161
        zpos = 85.5436
        xrot = 33.2692
	msg.position.x = xpos
	msg.position.y = ypos
        msg.position.z = zpos
	msg.orientation.x = gripper
 	pub.publish(msg)
	time.sleep(2)
	print "x: "+str(msg.position.x)+" y: "+str(msg.position.y)+" z: "+str(msg.position.z)
        t += 1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
