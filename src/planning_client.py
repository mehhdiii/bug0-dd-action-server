#! /usr/bin/env python

import rospy

# Brings in the SimpleActionClient
import actionlib
import assignment_2_2023.msg
from geometry_msgs.msg import PoseStamped

def planning_client():
    client = actionlib.SimpleActionClient('/reaching_goal', assignment_2_2023.msg.PlanningAction)
    print("planning_client waiting for server")
    client.wait_for_server()
    rospy.loginfo("server ready. publishing goal")
    pose = PoseStamped()
    pose.pose.position.x = 7
    pose.pose.position.y = 7

    goal = assignment_2_2023.msg.PlanningGoal(target_pose=pose)

    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()

def main():
# Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
    rospy.init_node('planning_client', log_level=rospy.DEBUG)
    result = planning_client()
    print("Result:", result)

if __name__ == "__main__":

    main()
