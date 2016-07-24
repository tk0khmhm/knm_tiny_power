#!/usr/bin/env python
import roslib; roslib.load_manifest('knm_tiny_power')
import rospy

from nav_msgs.msg import Odometry
from knm_tiny_msgs.msg import Velocity

import time
from time import sleep
import serial
import threading
import math

import tiny_power

#tinypower = tiny_power.TinyPower('/dev/tiny', 115200)
tinypower = tiny_power.TinyPower('/dev/tiny', 57600)
#tinypower = tiny_power.TinyPower('/dev/tiny', 38400)
#tinypower = tiny_power.TinyPower('/dev/tiny', 19200)
#tinypower = tiny_power.TinyPower('/dev/tiny', 9600)

global_lock = threading.Lock()
####
####
def commandCallback(data):
	#global_lock.acquire()
	tinypower.commVCX(data.op_linear)
	tinypower.commVCR(data.op_angular)
	#global_lock.release()
	pass
####	global global_lock
####	print 'linear : ', data.op_linear
####	#global_lock.acquire()
####	#ser.write('VCX'+str(data.op_linear)+'\n\r'+'VCR'+str(data.op_angular)+'\n\r')
####	ser.write('VCX'+str(round(data.op_linear, 2))+'\n\r')
####	#line = ser.readline()
####	#line = ser.readline()
####	print 'VCX'+str(round(data.op_linear, 2))+'\n\r'
####	#print line
####	ser.write('VCR'+str(round(data.op_angular, 2))+'\n\r')
####	#global_lock.release()
####	line = ser.readline()
####	line = ser.readline()
####	print 'angular : ', data.op_angular
####	#print 'VCR'+str(round(data.op_angular, 2))+'\n\r'
####	#print line
####
####
####def calcOdometry(pose, data, dt):
####	pass

if __name__ == '__main__':
	rospy.init_node('tiny_power')


	command_sub = rospy.Subscriber('tinypower/command_velocity', Velocity, commandCallback)
	odom_pub = rospy.Publisher('/tinypower/odom', Odometry, queue_size = 10)

	#ser = serial.Serial('/dev/ttyUSB2', 57600)
	#ser = serial.Serial('/dev/tiny', 57600)
	#ser = serial.Serial('/dev/tiny', 115200)

	odom_data = Odometry()

	r = rospy.Rate(50) 
	
	####global global_lock
	
	while not rospy.is_shutdown():
		tinypower.commMVV()
		r.sleep()
	#while True:

		####global_lock.acquire()
		####ser.write("MVV\n")
		####sleep(0.01)
		####line = ser.readline()
		####global_lock.release()
		####print line
		####print len(line)
		####if len(line)>4:
		####	data = line.split(':')
		####	data = data[1].split('\r')
		####	data = data[0].split(',')
		####	#print data
		####	global_lock.acquire()
		####	ser.readline()
		####	global_lock.release()

		####	#calcOdometry(pose, tiny_state, dt);

		odom_data.header.stamp = rospy.Time.now()
		####	odom_data.pose.pose.position.x = float(data[2])
		####	odom_data.pose.pose.position.y = float(data[3])
		####	odom_data.twist.twist.linear.x = float(data[0])
		####	odom_data.twist.twist.angular.z = float(data[1])
		####odom_pub.publish(odom_data)
		odom_data.twist.twist.linear.x = tinypower.linear
		odom_data.twist.twist.angular.z = tinypower.angular
		odom_pub.publish(odom_data)

		#ser.readline()
		#global_lock.release()

		#sleep(0.5)
		#r.sleep()
	print "Programm is finished"
	#tinypower.stop()
	rospy.spin()


