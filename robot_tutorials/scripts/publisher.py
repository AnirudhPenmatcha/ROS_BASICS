#!/usr/bin/env python3 
#This is required for when you use rosrun to execute this node from anywhere, it will tell ROS what to use to run this program
import rospy
from std_msgs.msg import String, Int8

def function_to_publish():
	hello_pub = rospy.Publisher('Topic_Name', String, queue_size=10)
	hello_pub_int = rospy.Publisher('Int8_type_topic', Int8, queue_size=10)
	rospy.init_node('Node_Name', anonymous = True)
	rate = rospy.Rate(10)
	counter = 0
	while not rospy.is_shutdown():
		greeting = "Hello, This is the message that is being broadcasted"
		greeting_int = ord(greeting[counter%len(greeting)])
		rospy.loginfo(greeting) #For Debugging (it prints our published message on the terminal and writes it to the nodes logfile and rosout)
		hello_pub.publish(greeting) #The command that publishes the message
		hello_pub_int.publish(greeting_int) #This command also publishes, but to the topic 'Int8_type_topic' and with an 8bit Integer type
		counter += 1
		rate.sleep() #Makes it sleep enough for publishing once every 100 milliseconds



if __name__ == '__main__':
	try:
		function_to_publish()
	except rospy.ROSInterruptException:
		pass
