#!/usr/bin/env python
"""Import statements"""
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
#Defined the value of Pi.
PI = 3.1415926535897

def pose_callback(msg):

    """Definition of the callback function."""
    if msg.theta != 0:
        #To print this when the turtle is on its way of completing a revolution.
        rospy.loginfo("Moving in a circle")
    else:
        #To print this before the turtle begins to move.
        rospy.loginfo("starting")


def turtle_revolve():
    """Python program to move the turtle inside the turtlesim window in a circle and,
       stop at its initial location."""
    #  To Create a handle to publish messages to the topic /turtle1/cmd_vel.
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    #  Initializes the ROS node 'turtle_revolve for the process.
    rospy.init_node('turtle_revolve', anonymous=True)

    #  Set the Loop Rate .
    var_loop_rate = rospy.Rate(1)

    vel_msg = Twist()
    msg = Pose()
    i = 0
    while not rospy.is_shutdown() and i >= 0:
        #Declaring the values of linear and angular velocities in different directions .
        vel_msg.linear.x = 12
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        # Value of 2*Pi is taken to ensure a complete revolution.
        vel_msg.angular.z = 2*PI

        velocity_publisher.publish(vel_msg)
        rospy.Subscriber("/turtle1/pose", Pose, pose_callback)
        var_loop_rate.sleep()

        # The 'i' variable is used so that the initial value of theta for turtle =0 is ignored .
        #theta = (angle made by the turtle with horizontal axis).
        i = i+1

        if i != 1:
            if msg.theta == 0:
                # Setting the values of linear velocity=0 and angular velocity=0.3 .
                vel_msg.linear.x = 0
                vel_msg.angular.z = 0.3
                velocity_publisher.publish(vel_msg)

                # To indicate the turtle has succesfully completed a revolution .
                rospy.loginfo("Goal Reached")
            break

# Python Main
if __name__ == '__turtle_revolve__':
    try:
        turtle_revolve()
    except rospy.ROSInterruptException:
        pass
