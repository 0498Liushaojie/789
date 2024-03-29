#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def even_publisher():
    rospy.init_node('even_publisher', anonymous=True)

    namespace = rospy.get_namespace()
    pub_even = rospy.Publisher(namespace + 'even_numbers', Int32, queue_size=10)
    pub_overflow = rospy.Publisher(namespace + 'overflow', Int32, queue_size=10)
    rate = rospy.Rate(10) # 10Hz

    num = 0
    while not rospy.is_shutdown():
        if num % 2 == 0:
            pub_even.publish(num)

    if num == 100:
        pub_overflow.publish(num)
        num = 0
    else:
        num += 1

    rate.sleep()

if __name__ == '__main__':
    try:
        even_publisher()
    except rospy.ROSInterruptException:
        pass