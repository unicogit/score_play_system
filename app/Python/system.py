# pip3 install python-vlc
# pip3 install schedule
# pip3 install pyside6

import argparse
import cv2
import numpy as np
import os
import os.path
import sys
import time
import vlc
import lib.fileio as fileio
from PySide6 import QtWidgets, QtGui, QtCore

class playerWindow(QtWidgets.QMainWindow) :
	def __init__(self, master=None):
		QtWidgets.QMainWindow.__init__(self, master)
		self.setWindowFlags(QtCore.Qt.CustomizeWindowHint
							| QtCore.Qt.WindowMaximizeButtonHint
							| QtCore.Qt.WindowStaysOnTopHint)
		self.instance = vlc.Instance('-q')
		self.mediaplayer = self.instance.media_player_new()
		self.videoframe = QtWidgets.QLabel()
		self.setCentralWidget(self.videoframe)
		if sys.platform.startswith('linux'): # for Linux using the X Server
			self.mediaplayer.set_xwindow(self.videoframe.winId())
		elif sys.platform == "win32": # for Windows
			self.mediaplayer.set_hwnd(self.videoframe.winId())
		elif sys.platform == "darwin": # for MacOS
			self.mediaplayer.set_nsobject(int(self.videoframe.winId()))

		self.p = indexProcess()
		self.p.indexThread.connect(self.dspBox)
		self.p.start()

		self.img = 0

	def pstop(self) :
		self.p.stop()
		self.p.wait()

	def dspBox(self, idx):
		playIndex = 0
		if self.vlcisplaying() :
			chk = self.mediaplayer.get_time() 
			for i in range(len(self.start)) :
				if i+1 < len(self.start) :
					if self.start[i][1] <= chk < self.start[i+1][1]:
						playIndex = self.start[i][0]
						break
				elif i == len(self.start)-1 :
					if self.start[i][1] <= chk :
						playIndex = self.start[i][0]
					else :
						playIndex = -1

		bimg = np.copy(self.img)
		l, t, r, b = getbox(self.pt, playIndex)
		cv2.rectangle(bimg, (l, t), (r, b), (0,0,255), 3)
		cv2.imshow('chartwindow', bimg)

	def dspChartWindow(self, folder, debug) :
		self.img = cv2.imread(folder+'/chart.png')
		cv2.putText(self.img, 'close', (20, 100), cv2.FONT_HERSHEY_TRIPLEX, 2, (255,0,0), 3, cv2.LINE_AA)
		cv2.putText(self.img, 'play', (400, 100), cv2.FONT_HERSHEY_TRIPLEX, 2, (255,0,0), 3, cv2.LINE_AA)
		cv2.putText(self.img, 'stop', (600, 100), cv2.FONT_HERSHEY_TRIPLEX, 2, (255,0,0), 3, cv2.LINE_AA)

		self.start = fileio.readtimestamp(folder, debug)
		self.pt = fileio.readbarpoint(folder, debug)

		cv2.imshow('chartwindow', self.img)
		cv2.setMouseCallback('chartwindow', self.click_pos)

	def click_pos(self, event, x, y, flags, params) :
		if event == cv2.EVENT_LBUTTONDOWN:
			playIndex = click2index(self.pt, x, y)
			if playIndex != 0 :
				self.vlcstop()
				if playIndex > 0 :
					self.vlcplay()
					self.vlcsettime(gettime(self.start, playIndex))
				elif playIndex == -2 :
					self.vlcplay()
				elif playIndex == -1 :
					self.windowclose()

	def loadfile(self, target) :
		print(target)
		video_file = self.instance.media_new(target)
		self.mediaplayer.set_media(video_file)

	def windowclose(self) :
		self.close()

	def vlcplay(self) :
		self.mediaplayer.play()

	def vlcstop(self) :
		self.mediaplayer.stop()

	def vlcsettime(self, timestamp) :
		self.mediaplayer.set_time(timestamp)

	def vlcisplaying(self) :
		return self.mediaplayer.is_playing()


class indexProcess(QtCore.QThread):

	indexThread = QtCore.Signal(int)

	def __init__(self, parent=None):
		QtCore.QThread.__init__(self, parent)

		self.mutex = QtCore.QMutex()
		self.stopped = False

	def stop(self):
		with QtCore.QMutexLocker(self.mutex):
			self.stopped = True

	def restart(self):
		with QtCore.QMutexLocker(self.mutex):
			self.stopped = False

	def run(self):
		countNum = 0
		while not self.stopped:
			self.indexThread.emit(countNum)
			countNum += 1
			time.sleep(0.02)


def click2index(ary, x, y) :
	for n, l, t, r, b in ary :
		if l<=x<=r and t<=y<=b :
			return n

	if 0<=x<=250 and 0<=y<=120 :
		return -1

	if 390<=x<=540 and 0<=y<=120 :
		return -2

	if 590<=x<=740 and 0<=y<=120 :
		return -3

	return 0


def gettime(ary, bar) :
	for i in range(len(ary)) :
		if ary[i][0] == bar :
				return ary[i][1]
	return 0


def getbox(ary, tar) :
	for n, l, t, r, b in ary :
		if tar == n :
			return l, t, r, b
	return 0, 0, 0, 0


#########################################################
# main proc
def main(folder, debug=False) :
	app = QtWidgets.QApplication(sys.argv)
	
	pw = playerWindow()
	pw.show()
	pw.dspChartWindow(folder, debug)
	
	target = folder + '/movie.mp4'
	if os.path.exists(target) :
		pw.loadfile(target)
	else :
		target = folder + '/music.wav'
		if os.path.exists(target) :
			pw.loadfile(target)

	app.exec()
	pw.pstop()
	cv2.destroyAllWindows()


#########################################################
# system boot proc
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', type=str, default='out', help='対象フォルダ')
	args = parser.parse_args()

	# main(args.f, True)
	main(args.f)
