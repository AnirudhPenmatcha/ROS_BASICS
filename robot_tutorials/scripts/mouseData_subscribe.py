import rospy
from std_msgs.msg import Int8

def compute(data):
	#print(data.data)
	rospy.loginfo(data.data)

def Subscriber():
	rospy.init_node('MouseDATA_Subscriber')
	rospy.Subscriber('Mouse_RawDATA', Int8, compute)
	rospy.spin()

if __name__ == '__main__':
	Subscriber()
