#!/usr/bin/env python

from robot_tutorials.srv import *
import rospy
import os

def handle_mouse_clicks(req):
	# Return the max of the two integers
	mouse_button = req.L + req.R
	print("mouse%s"%(mouse_button))
	if mouse_button == 1:
		os.system('xrandr --output eDP-1 --brightness .5')
	elif mouse_button == 2:
		os.system('xrandr --output eDP-1 --brightness 0.1')
	elif mouse_button == 3:
		os.system('xrandr --output eDP-1 --brightness 1')
	return mouse_clicksResponse(mouse_button)

def mouse_click_server():
	# rospy.init_node this will register the node on the graph
	rospy.init_node('mouse_clicks_server')
	# rospy.service takes 3 arguments: the name of the service, the type of the service and the callback function
	m = rospy.Service('mouse_clicks', mouse_clicks, handle_mouse_clicks)
	print("Ready to read mouse clicks mouse1, mouse2 and mouse3")
	# rospy.spin() keeps your code from exiting until the service is shutdown
	rospy.spin()

if __name__ == '__main__':
	mouse_click_server()
