import pygame
import Game

class Sprite:
	def __init__(self,path):
		self.image = self.Open(path)
		size = self.image.get_rect().size
		self.showedImage = self.image
		self.width = size[0]
		self.height = size[1]
		self.clipRect = (0,0,0,0)
	def Open(self,path):
		return pygame.image.load(path)

	def Scale(self,xtimes,ytimes):
		self.showedImage = pygame.transform.scale(self.image,(self.width*xtimes,self.height*ytimes))

	def SetClip(self,x,y,width,height):
		self.clipRect = (x,y,width,height)
		self.showedImage = self.image.subsurface(self.clipRect)
	def Render(self,x,y):
		screen = Game.Game.window
		screen.blit(self.showedImage,(x,y))

	def GetWidth(self):
		return self.width

	def GetHeight(self):
		return self.height

	def IsOpen(self):
		if self.image:
			return True
		return False
