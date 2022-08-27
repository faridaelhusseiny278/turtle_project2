#!/usr/bin/env python3
from math import sqrt
import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
x=0
y=0
z=0
flag= False


def pose_callback(pose):
    global x,y,z
    x= pose.x
    y=pose.y
    z=pose.theta

    

def go_to_controller(xgoal,ygoal):
    global x,y,z,flag
    cmd=Twist()
    while(True):
        kv=rospy.get_param('/turtle_project/beta',default =0)
        kw=rospy.get_param('/turtle_project/fai',default =0)
        distance=abs(math.sqrt(((xgoal-x) ** 2 )+((ygoal-y) ** 2)))
        linear_v=float(kv*distance)
        angular_v=kw*(-1*(z)+math.atan2((ygoal-y),(xgoal-x)))
        cmd.linear.x=linear_v
        cmd.angular.z=angular_v 
        flag=True
        pub.publish(cmd)
        if distance<=0.01:
            cmd.linear.x=0
            cmd.angular.z=0
            flag= False
            print("arrived to goal")
            break
        
      




if __name__=='__main__':
    
        try:
            
            rospy.init_node('turtle_project')
            while (flag==False):
                pub= rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
                sub= rospy.Subscriber("/turtle1/pose",Pose,pose_callback)
                rospy.loginfo("publisher node has been started")
                x_coordinate=input("x coordinate goal : ")
                y_coordinate=input("y coordinate goal : ")
                go_to_controller(float(x_coordinate),float(y_coordinate))
            rospy.spin()
        except rospy.ROSInterruptException:
            rospy.loginfo("node terminated")




