#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import common

from std_msgs.msg import Header
from geometry_msgs.msg import TwistStamped
from nav_project_athena.msg import athena_RemoteMsg

def bsCallback(data):
    remoteMsg.f32_order_linearVelocity = data.twist.linear.x;
    remoteMsg.f32_order_rotationVelocity = data.twist.angular.z;
	remoteMsg.i8_order_priority = 9;
	remoteMsg.f32_order_validityTime = 1.0;
	remoteMsg.str_order_etc = "OK";
    publisher.publish(remoteMsg)

if __name__ == '__main__':
	rospy.init_node('vw2athena', anonymous=True)
	rate_mgr = rospy.Rate(10)  # Hz
    publisher = rospy.Publisher('athena_remoteMsg', athena_RemoteMsg, queue_size=1)
	rospy.Subscriber("blackship/vw_imput", TwistStamped, bsCallback)
	rospy.spin()
