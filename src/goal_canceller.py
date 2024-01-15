#! /usr/bin/env python

import rospy
from monitoring_package.srv import cancelgoal, cancelgoalResponse
import actionlib
import assignment_2_2023.msg



def cancel_goal_handler(request):
    client = actionlib.SimpleActionClient('/reaching_goal', assignment_2_2023.msg.PlanningAction)
    print("planning_client waiting for server")
    client.wait_for_server()
    rospy.loginfo("server ready. cancelling goal")
    client.cancel_all_goals()
    return cancelgoalResponse()

def main():
    rospy.init_node('cancel_goal_service', log_level=rospy.DEBUG)
    s = rospy.Service('cancel_goal', cancelgoal, cancel_goal_handler)
    rospy.spin()

if __name__ == "__main__":
    main()


