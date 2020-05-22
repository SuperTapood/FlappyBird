import os
import pygame
from time import sleep as wait
from bird import Bird
from math import floor
from pipe import Pipe
from text import Text

class Screen:
	def __init__(self):
		self.window = pygame.display.set_mode((288, 512))
		pygame.display.set_caption("Flappy Bird")
		direct = os.listdir(r"imgs")
		self.birdAnim = []
		self.base = pygame.image.load(r"imgs\\" + direct[0])
		self.bg = pygame.image.load(r"imgs\\" + direct[1])
		self.pipe = pygame.image.load(r"imgs\\" + direct[-1])
		self.border = 450
		self.baseEnd = 336
		self.jump = False
		for img in direct:
			if img[0:4] == "bird":
				if int(img[4]) > 1:
					self.birdAnim.append(pygame.image.load(r"imgs\\" + img))
					self.birdAnim.append(pygame.image.load(r"imgs\\" + img))
				self.birdAnim.append(pygame.image.load(r"imgs\\" + img))
		self.bird = Bird(self.birdAnim)
		self.score = 0
		return

	def blitGame(self):
		x = 0
		pygame.init()
		self.pipeArray = Pipe(self.pipe)
		while True:
			self.bird.fall()
			self.window.blit(self.bg, (0, 0))
			self.pipeArray.blit(self.window)
			txt = Text(str(self.score), 50, 144, 50, self.window, (255, 255, 255))
			x -= 1
			if x == -(self.baseEnd):
				x = 0
			self.window.blit(self.base, (x, self.border))
			self.window.blit(self.base, (x + self.baseEnd, self.border))
			self.bird.blit(self.window)
			wait(1 / 30)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				elif event.type == pygame.KEYDOWN and chr(event.key) == " ":
					self.jump = True
			if self.bird.y >= self.border - 30:
				print(f"You lost with a score of {floor(self.score)}")
				quit()
			self.pipeArray.delOut()
			if self.pipeArray[0] == 50:
				self.score += 1
			if self.jump:
				if self.bird.tick() is False:
					self.jump = False
			self.pipeArray.tick()
			self.pipeArray.checkLength() 
			if self.pipeArray.checkForHit(self.bird.y, self.bird.x):
				print(f"You lost with a score of {floor(self.score)}")
				quit()
			pygame.display.update()
		return
	pass