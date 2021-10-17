#!/usr/bin/env python

import sys
import rospy
from robot_tutorials.srv import *
from std_msgs.msg import Int8

def mouse_clicks_client(x, y):
	# The wait_for_service blocks further execution of the function until a service under the name "max_two_ints" is available
	rospy.wait_for_service("mouse_clicks")
	try:
		# Creates a handle for our request and then we can call it with the two integers as its arguments
		MOUSE = rospy.ServiceProxy('mouse_clicks', mouse_clicks)
		resp = MOUSE(x, y)
		return resp
	# If the call fails, a service exception is thrown, which is caught here with an except block
	except rospy.ServiceException, e:
		print("Service call failed: %s"%e)

# This is to let the user know the proper usage of the client function
def usage():
	return("%s [%s %s]"%sys.srgv[0])

def compute(data):
	#print(data.data)
	x = data.data
	print("Requesting max(%s, %s)"%(x, 0))
	print("mouse clicks %s, %s = %s"%(x, 0, mouse_clicks_client(x, 0)))
	rospy.loginfo(data.data)

if __name__ == '__main__':
	# We'll receive two values from the input and pass them along to the client function
	#x = 0
	rospy.init_node('MouseDATA_Subscriber')
	rospy.Subscriber('Mouse_RawDATA', Int8, compute)
	# x = int(x)
	# print("Requesting max(%s, %s)"%(x, 0))
	# print("mouse clicks %s, %s = %s"%(x, 0, mouse_clicks_client(x, 0)))
	rospy.spin()
