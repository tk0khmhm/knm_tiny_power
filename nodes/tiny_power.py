#!/usr/bin/env python
# cofing: UTF-8

import rospy

import serial
import sys
import threading
from time import sleep


class TinyPower:
	def __init__(self, dev_name, baudrate):
		self.dev_name = dev_name
		self.baud = baudrate
		self.ser = serial.Serial(self.dev_name, self.baud, timeout=0.1)
		self.linear = 0.0
		self.angular = 0.0

		self.global_lock = threading.Lock()

		self.thread1 = threading.Thread(target=self.get_char_loop)
		self.thread1.start()

	def commVCX(self, linear):
		linear = str(round(linear, 2))
		#print 'linear : ', linear
		command = 'VCX'+linear+'\n\r'
		#self.global_lock.acquire()
		self.ser.write(command)
		#self.global_lock.release()

	def commVCR(self, angular):
		angular = str(round(angular, 2))
		#print 'angular : ', angular
		command = 'VCR'+angular+'\n\r'
		#self.global_lock.acquire()
		self.ser.write(command)
		#self.global_lock.release()

	def commMVV(self):
		#self.global_lock.acquire()
		self.ser.write('MVV\n\r')
		#self.global_lock.release()
		#line = self.ser.readline()
		#ch = self.ser.read()
		#print '%c'%(self.ser.read()),
		#sys.stdout.write(ch)
		#print '[%c] , [%d]'%(ch, ord(ch))
		#while ch != "$":
		#	ch = self.ser.read()
		#	print '[%c] , [%d]'%(ch, ord(ch))
		#line = self.ser.readline()
		#print line
		#print line
		#print line[0], line[1]
		#print self.hantei(line)
		#while not self.hantei(line):
		#	line = self.ser.readline()
		#	print line
		#print line
		#while True:
		#	if line[0:5] == '$MVV:':
		#		print 'hey'
		#		break
		#	else:
		#		print 'oh'
		#		line = self.ser.readline()
		#		print line

	def get_char_loop(self):
		print "Thread Started"
		while not rospy.is_shutdown():
			#self.global_lock.acquire()
			ch = self.ser.read()
			#self.global_lock.release()
			#sys.stdout.write(ch)
			if ch == "$":
				#self.global_lock.acquire()
				line = self.ser.readline()
				#print line
				#self.global_lock.release()
				if line[0:3] == 'MVV':
					data = line.split(':')
					data = data[1].split('\r')
					data = data[0].split(',')
					self.linear = float(data[0])
					self.angular = float(data[1])
					#print data
				else:
					print line
		print "Thread Finished"







