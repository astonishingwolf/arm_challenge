#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import rospy
import tf
import moveit_commander  # https://answers.ros.org/question/285216/importerror-no-module-named-moveit_commander/
import random
from geometry_msgs.msg import Pose, Point, Quaternion
#from vision_msgs.msg import Detection2DArray
from math import pi
import time
from ur_kinematics.msg import stup
pose_goal = Pose()
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('ur3_move',anonymous=True)
group = [moveit_commander.MoveGroupCommander("manipulator")]  # ur3 moveit group name: manipulator

xx = 1
def go_to_pose_goal(msag):
    #wpose = group.get_current_pose().pose
    rospy.loginfo("hjbinnk")
    #pose_goal =Pose()
    #pose_goal.position.x = wpose.position.x + msg.position.x
    #pose_goal.position.y = wpose.position.y + msg.position.y
    #pose_goal.position.z = wpose.position.z + msg.position.z
    #pose_goal.orientation.x = wpose.orientation.x + msg.orientation.x
    #pose_goal.orientation.y = wpose.orientation.y + msg.orientation.y
   # pose_goal.orientation.z = wpose.orientation.z + msg.orientation.z
   # pose_goal.orientation.w = wpose.orientation.w + msg.orientation.w
   # group.set_pose_target(pose_goal)
   # group.go(pose_goal, wait=True)
   # time.sleep(10)
    #group.stop()
    #group.clear_pose_targets()


def main():
    #time.sleep(3)
    rospy.loginfo("dfdv")
    stuo = stup()
   # rospy.init_node('listener3', anonymous=True)
    rospy.Subscriber("/chatter", stup ,go_to_pose_goal)


if __name__ == '__main__':
    main()
