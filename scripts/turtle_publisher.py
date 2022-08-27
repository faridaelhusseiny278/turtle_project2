#!/usr/bin/env python3
from distutils import cmd
from math import sqrt
import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
x=0
y=0
z=0

def pose_callback(pose):
    global x,y,z
    x= pose.x
    y=pose.y
    z=pose.theta

     #el mafrod enaha hena hatpublish el velocity el gdeda ll position
    

def go_to_controller(xgoal,ygoal):
    global x,y,z
    cmd=Twist()
    while(True):
        kv=0.5
        kw=4.0
        linear_v=kv*math.sqrt(pow((xgoal-Pose.x),2)+pow((ygoal-Pose.y),2))
        angular_v=kw(-1*(Pose.theta)-math.atan((ygoal-Pose.y)/(xgoal-Pose.x)))
        cmd.linear.x=linear_v
        cmd.angular.z=angular_v 

        if math.sqrt(pow((xgoal-Pose.x),2)+pow((ygoal-Pose.y),2))<0.01:
            break
    pub.publish(cmd)
    #when arriving to goal ?
    #rospy.loginfo("arrived to goal")
    



if __name__=='__main__':

    rospy.init_node="turtle_publisher.py"
    pub= rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    sub= rospy.Subscriber("/turtle1/pose",Pose,pose_callback)
    rospy.loginfo("publisher node has been started")
    rospy.spin()
    go_to_controller(5.0,9.0)




