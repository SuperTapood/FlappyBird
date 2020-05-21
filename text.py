import pygame

class Text:
	def __init__(self, txt, x, y, size, win, color=(255, 255, 255)):
		"""
		add text to the window (will later be added to the button function)
		txt - str, the text to be written
		x - int, the position on the x-axis
		y - int, the position on the y-axis
		size - int, the size of the text
		win - the window to be drawnned on
		color - 3-item-tuple, the RGB values of the color
		"""
		x *= 2
		y *= 2
		font = "freesansbold.ttf"
		# render the text
		font = pygame.font.Font(font, size)
		# position the text
		text = font.render(txt, True, color)
		self.rectText = text.get_rect()
		self.rectText.center = (x // 2, y // 2)
		# add the text
		win.blit(text, self.rectText) 
		return
	pass