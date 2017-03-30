import pygame
import os
import State

class Game:
	size =(1024,600)
	window  = pygame.display.set_mode(size)
	pygame.display.set_caption('penguinGame')
	def __init__(self):
		pygame.init()
		self.state = State.State()
		self.clock = pygame.time.Clock()

	def Run(self):
			while not self.state.quitRequest:
				self.state.Update()
				self.state.Render()
				self.clock.tick(60)

	def GetState(self):
		return self.state

	def GetRenderer(self):
		return self.screen

