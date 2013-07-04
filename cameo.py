#!/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from managers import WindowManager, CaptureManager
import pickle


#DUMMY = True


class Cameo(object):
	def __init__(self , w , h , d):
		self._windowManager = WindowManager('Cameo',self.onKeypress)
		self.w = w
		self.h = h
		self.device = d
		
		if self.device == 'dummy':
			self._captureManager = CaptureManager(None,640,480, self._windowManager, True)
		else:
			self._captureManager = CaptureManager(cv2.VideoCapture(self.device),self.w,self.h,self._windowManager, True)		
			#self.pickleArray = np.zeros([100,480,640,3])
		
	def run(self):
		"""Run the main loop."""
		self._windowManager.createWindow()
		
		i = 0
		
		while self._windowManager.isWindowCreated:
			self._captureManager.enterFrame()
			frame = self._captureManager.frame
			
			#if not DUMMY:
				#if i < 100:
					#print 'Dopisuje klatke'
					#self.pickleArray[i] = frame
					#i += 1
				#else:
					#pass
			
			#cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
			
			# TODO: Filter the frame

			self._captureManager.exitFrame()
			self._windowManager.processEvents()

	def onKeypress (self, keycode):
		"""Handle a keypress.
			space -> Take a screenshot.
			tab -> Start/stop recording a screencast.
			escape -> Quit.
		"""

		if keycode == 32: # space
			self._captureManager.writeImage('screenshot.png')
		elif keycode == 9: # tab
			if not self._captureManager.isWritingVideo:
				self._captureManager.startWritingVideo('screencast.avi')
			else:
				self._captureManager.stopWritingVideo()
		elif keycode == 27: # escape
			self._windowManager.destroyWindow()
			#if not DUMMY:
				#print 'zapisuje sloik'
				#nameOfFile = 'pickle'
				#f = open( nameOfFile , 'w' )
				##self.pickleArray.tofile(f)
				#np.save(nameOfFile , self.pickleArray)
				#f.close()
				#print 'sloik zapisany'
			


if __name__=="__main__":
	Cameo(640,480,0).run()
