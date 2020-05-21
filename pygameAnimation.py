import pygame
from time import sleep as wait

class Animation:
	def moveUp(self, maxMove, angle):
		index = self.cycle.index(self.currentImg)
		if index + 1 == len(self.cycle):
			self.currentImg = self.cycle[0]
			return False
		else:
			self.currentImg = self.cycle[index + 1]
			index = index + 1
			self.y -= maxMove / len(self.cycle)
		return

	def tilt(self, img, angle):
		return pygame.transform.rotate(img, angle)