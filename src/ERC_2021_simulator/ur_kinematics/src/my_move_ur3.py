#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy, sys
import moveit_commander
from geometry_msgs.msg import Pose
from copy import deepcopy
from math import pi 
from moveit_commander.conversions import pose_to_list
import moveit_msgs.msg
import time
from aruco_detect.msg import stup

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('moveit_ur3', anonymous=False)

pose_goal =Pose()
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = 'manipulator'
group  = moveit_commander.MoveGroupCommander(group_name)
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)
def go_to_pose_goal(msg):
    rospy.init_node('moveit_ur3', anonymous=False)
    wpose = group.get_current_pose().pose
    #rospy.loginfo(wpose.orientation.y)
    
    pose_goal.position.x = wpose.position.x + msg.x1 + 0.1
    pose_goal.position.y = wpose.position.y + msg.x2 
    pose_goal.position.z = wpose.position.z + msg.x3
    pose_goal.orientation.x = wpose.orientation.x + msg.x4
    pose_goal.orientation.y = wpose.orientation.y + msg.x5
    pose_goal.orientation.z = wpose.orientation.z + msg.x6
    pose_goal.orientation.w = wpose.orientation.w + msg.x7
    rospy.loginfo(pose_goal.position.x)
    rospy.loginfo(wpose.position.x)

    

def main():
    time.sleep(3)
    stuo = Pose()
    pose_goal.orientation.w = 0.0
    pose_goal.position.x = 0.2   # red line      0.2   0.2
    pose_goal.position.y = 0.0 # green line  0.15   0.15
    pose_goal.position.z = 0.2 # blue line   # 0.35   0.6
    #rospy.init_node('listener1', anonymous=True)
    rospy.Subscriber("/chatter", stup ,go_to_pose_goal,queue_size=1)
    group.set_pose_target(pose_goal)
    group.go(pose_goal, wait=True)
    time.sleep(1)
    rospy.spin()

while not rospy.is_shutdown():
    group.set_pose_target(pose_goal)
    group.go(pose_goal, wait=True)
    time.sleep(0.5)
if __name__ == '__main__':
    main()
