#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Pose, Point, Quaternion
from ur_kinematics.msg import stup
import moveit_commander  # https://answers.ros.org/question/285216/importerror-no-module-named-moveit_commander/
pose_goal = Pose()
#moveit_commander.roscpp_initialize(sys.argv)
#rospy.init_node('ur3_move',anonymous=True)
group = [moveit_commander.MoveGroupCommander("manipulator")]  # ur3 moveit group name: manipulator
def callback(data):
    rospy.loginfo("hjbinnk")
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/chatter", stup, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()