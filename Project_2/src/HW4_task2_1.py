#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from std_msgs.msg import Float64

# Initialize the angular tolerance
angl_tol = 3


def callback(data):
    vel_pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg  = Twist()

    rospy.loginfo(data.data)
    if (data.data > 0):
        vel_msg.linear.x  =  0.00
        vel_msg.angular.z =  0.25
        if (data.data < angl_tol):
            vel_msg.linear.x  =  1.00
            vel_msg.angular.z =  0.00
    elif (data.data < 0):
       vel_msg.linear.x  = 0.00
       vel_msg.angular.z = - 0.25
       if (abs(data.data) < angl_tol):
            vel_msg.linear.x  =  1.00
            vel_msg.angular.z =  0.00

    # Since the Wall-E moving just in x-axis
    # vel_msg.linear.x = speed
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0 
    
    vel_pub.publish(vel_msg)

# # Get the aligment angular error 
# def set_angl():

#     anglSub = rospy.Subscriber("/aligment_error")

while not rospy.is_shutdown():

    # Initialize a sub nod
    rospy.init_node("subcriber", anonymous=True)

    # Subcribe the alignment angular error
    anglSub = rospy.Subscriber("/aligment_error", Float64, callback)

    rospy.spin()











    


