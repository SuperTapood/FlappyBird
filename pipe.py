from random import randint as rand
import pygame



class Pipe:
	def __init__(self, img):
		self.array = []
		self.heights = []
		self.pipeLen = 100
		self.img = [img, pygame.transform.flip(img, False, True)]
		self.size = 320
		self.createPipe()	
		return

	def __getitem__(self, index):
		return self.array[index]

	def createPipe(self):
		self.array.append(288)
		y1 = rand(self.size, 430)
		y2 = 212 - y1
		self.heights.append([y1, y2])
		return

	def delOut(self):
		for pipeX, pipeY in zip(self.array, self.heights):
			if pipeX < -50:
				self.array.remove(pipeX)
				self.heights.remove(pipeY)
		return

	def blit(self, win):
		for pipeX, pipeY in zip(self.array, self.heights):
			for img, y in zip(self.img, pipeY):
				win.blit(img, (pipeX, y))
		return

	def tick(self):
		array = []
		for x in self.array:
			array.append(x - 1)
		self.array = array
		return

	def checkLength(self):
		if self.__getitem__(-1) < 288 - self.pipeLen:
			self.createPipe()
		return

	def checkForHit(self, y, x):
		for pipeX, pipeY in zip(self.array, self.heights):
			if pipeX >= 50 and pipeX <= 90:
				if y > pipeY[0]:
					return True
				elif y < pipeY[1] + 320:
					return True
		return False
