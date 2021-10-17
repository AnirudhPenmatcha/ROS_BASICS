#!/usr/bin/env python3

import struct
import rospy
from std_msgs.msg import Int8

file = open( "/dev/input/mice", "rb" );

def publish():
	data_pub = rospy.Publisher('Mouse_RawDATA', Int8, queue_size=10)
	rospy.init_node('Mouse_Data_Publisher')
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		buf = file.read(3)
		#button = ord( buf[0] )
		button = buf[0]
		bLeft = button & 0x1
		bMiddle = ( button & 0x4 ) > 0
		bRight = ( button & 0x2 ) > 0
		x,y = struct.unpack( "bb", buf[1:] )
		print ("L:%d, M: %d, R: %d, x: %d, y: %d\n" % (bLeft,bMiddle,bRight, x, y) )
		data_var = bLeft+bRight*2
		data_pub.publish(data_var)
		rospy.loginfo(data_var)
		rate.sleep()


if __name__ == '__main__':
	try:
		publish()
	except rospy.ROSInterruptException:
		pass
