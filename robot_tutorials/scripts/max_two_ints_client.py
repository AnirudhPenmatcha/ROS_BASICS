#!/usr/bin/env python

import sys
import rospy
from robot_tutorials.srv import *

def max_two_ints_client(x, y):
	# The wait_for_service blocks further execution of the function until a service under the name "max_two_ints" is available
	rospy.wait_for_service("max_two_ints")
	try:
		# Creates a handle for our request and then we can call it with the two integers as its arguments
		max_two_ints = rospy.ServiceProxy('max_two_ints', maxTwoInts)
		resp = max_two_ints(x, y)
		return resp.max
	# If the call fails, a service exception is thrown, which is caught here with an except block
	except rospy.ServiceException, e:
		print("Service call failed: %s"%e)

# This is to let the user know the proper usage of the client function
def usage():
	return("%s [%s %s]"%sys.srgv[0])

if __name__ == '__main__':
	# We'll receive two values from the input and pass them along to the client function
	if len(sys.argv) == 3:
		x = int(sys.argv[1])
		y = int(sys.argv[2])
	else:
		print usage()
		sys.exit(1)
	print("Requesting max(%s, %s)"%(x, y))
	print("max(%s, %s) = %s"%(x, y, max_two_ints_client(x, y)))
