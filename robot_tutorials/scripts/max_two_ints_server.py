#!/usr/bin/env python

from robot_tutorials.srv import *
import rospy

def handle_max_two_ints(req):
	# Return the max of the two integers
	print("Returning max(%s, %s) = %s"%(req.a, req.b, max(req.a, req.b)))
	return maxTwoIntsResponse(max(req.a, req.b))

def max_two_ints_server():
	# rospy.init_node this will register the node on the graph
	rospy.init_node('max_two_ints_server')
	# rospy.service takes 3 arguments: the name of the service, the type of the service and the callback function
	m = rospy.Service('max_two_ints', maxTwoInts, handle_max_two_ints)
	print("Ready to compute max(a,b)")
	# rospy.spin() keeps your code from exiting until the service is shutdown
	rospy.spin()

if __name__ == '__main__':
	max_two_ints_server()
