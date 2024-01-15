#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Point
from monitoring_package.msg import poseVelocity

current_pose_subscriber = None
posePublisher = None

def currentPoseHandler(data):
    pointMsg = Point()
    pointMsg.x = data.x*3.28
    pointMsg.y = data.y*3.28
    pointMsg.z = 0


    posePublisher.publish(pointMsg)

def main():
    global current_pose_subscriber, posePublisher
    rospy.init_node('pose_in_feet_publisher', log_level=rospy.DEBUG)
    posePublisher = rospy.Publisher('current_pose_in_feet', Point)
    current_pose_subscriber = rospy.Subscriber('current_pose_velocity_publisher', poseVelocity, currentPoseHandler)
    rospy.spin()

if __name__ == "__main__":
    main()

