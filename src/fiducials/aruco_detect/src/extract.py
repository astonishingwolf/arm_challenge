#!/usr/bin/env python
import rospy
from vision_msgs.msg import Detection2DArray
from aruco_detect.msg import stup

pub = rospy.Publisher('/chatter', stup)
def iot_sensor_callback(msg):
    rospy.loginfo("zvfvsv") 
    a=stup()
    for m in msg.detections:
        for x1 in m.results:
            a.x1=x1.pose.pose.position.x
            a.x2=x1.pose.pose.position.y
            a.x3=x1.pose.pose.position.z
            a.x4=x1.pose.pose.orientation.x
            a.x5=x1.pose.pose.orientation.y
            a.x6=x1.pose.pose.orientation.z
            a.x7=x1.pose.pose.orientation.w
            rate = rospy.Rate(1)
            pub.publish(a)
            rate.sleep()
            rospy.loginfo(a.x6) 

rospy.init_node('listener', anonymous=True)
rospy.Subscriber("/fiducial_transforms", Detection2DArray ,iot_sensor_callback)

# spin() simply keeps python from exiting until this node is stopped
rospy.spin()