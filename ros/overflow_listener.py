#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def overflow_listener():
    rospy.init_node('overflow_listener', anonymous=True)

    namespace = rospy.get_namespace()
    rospy.Subscriber(namespace + 'overflow', Int32, overflow_callback)
    rospy.spin()

def overflow_callback(data):
    rospy.loginfo("Overflow detected: %d", data.data)

if __name__ == '__main__':
    overflow_listener()
