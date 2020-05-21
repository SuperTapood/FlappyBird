from pygameAnimation import Animation as anim
from time import time

class Bird(anim):
	def __init__(self, animCycle):
		self.x = 50
		self.y = 300
		self.cycle = animCycle
		for i in range(1, len(self.cycle), 1):
			self.cycle[i] = self.tilt(self.cycle[i], 45)
		self.cycle[0] = self.tilt(self.cycle[0], 325)
		self.currentImg = animCycle[0]
		self.jump = False
		return

	def blit(self, win):
		win.blit(self.currentImg, (self.x, self.y))
		return

	def tick(self):
		return self.moveUp(80, 45)

	def fall(self):
		self.y += 4
		return
