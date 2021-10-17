#!/usr/bin/env python3
#This is required for when you use rosrun to execute this node from anywhere, it will tell ROS what to use to run this program
import rospy
from std_msgs.msg import String, Int8

def callback_str(data):
	rospy.loginfo(data.data)

def callback_int(data):
	rospy.loginfo(str(data.data))

def Listener():
	rospy.init_node('Subscribing_Node', anonymous = False)
	rospy.Subscriber('Topic_Name', String, callback_str) #callback_str here is the name of the function that is to be called when the message is received from the topic 'Topic_Name'
	rospy.Subscriber('Int8_type_topic', Int8, callback_int)
	rospy.spin() #Keeps the node from exiting, until the node has been shutdown!

if __name__ == '__main__':
	Listener()
