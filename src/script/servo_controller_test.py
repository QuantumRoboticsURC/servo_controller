#!/usr/bin/env python3

from adafruit_servokit import ServoKit
import rospy
from std_msgs.msg import Int64

def callback_s1(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    print ("entre a callback")
    kit.servo[servo_cero].angle=data.data

def callback_s2(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    print ("entre a callback")
    kit.servo[servo_uno].angle=data.data

def callback_s3(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    print ("entre a callback")
    #kit.servo[servo_dos].angle= data.data
    if (data.data >= -90 and data.data <= 90):
        kit.servo[servo_dos].angle=int(map(data.data, -90, 90, 236, 416))
        kit.servo[servo_dos].duty_cycle = 0

    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("servo1", Int64, callback_s1)
    rospy.Subscriber("servo2", Int64, callback_s2)
    rospy.Subscriber("servo3", Int64, callback_s3)

    print ("entre a listener")

    rospy.spin()

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

if __name__ == '__main__':
    kit = ServoKit(channels=16)
    servo_cero = 0
    servo_uno = 1
    servo_dos = 2
    servo_tres = 15
    kit.servo[servo_dos].set_pulse_width_range(500, 2500)
    kit.servo[servo_dos].actuation_range = 640
    kit.servo[servo_tres].angle=180

    #500 = 0
    #2500 = 642 = 180
    #1500 = 321 = 90
    # x   = 90
    print ("entre a main")
    listener()
