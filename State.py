from Sprite import Sprite
import pygame
from Face import Face
from TileClass import TileMap
from TileClass import TileSet
import random
import math

class State:
	radius = 200
	objectCount = 0
	hit = 10
	objectArray = []
	tileSet = TileSet('img/tileset.png',64,64)
	tileMap = TileMap('map/tileMap.txt',tileSet)
	backGround = Sprite('img/ocean.jpg')
	def __init__(self):
		self.quitRequest = False
	def QuitRequest(self):
		return self.quitRequest
	def LoadAssets(self):
		pass

	def Update(self):
		self.Input()
		for i in sorted(range(len(self.objectArray)), reverse=True):
			if(self.objectArray[i].IsDead()):
				self.objectArray.pop(i)

	def Render(self):
		self.backGround.Render(0,0)
		self.tileMap.RenderLayer(0,0,0)
		for x in self.objectArray:
			x.Render()

		self.tileMap.RenderLayer(1,0,0)

	def Input(self):
		if not self.quitRequest:
			for event in  pygame.event.get():
				if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
					self.quitRequest = True
				if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					pos = pygame.mouse.get_pos()
					angle = random.random()*2*math.pi
					x = (pos[0]+self.radius*math.cos(angle))
					y = (pos[1]+self.radius*math.sin(angle))
					self.AddObject(x,y)

				if event.type == pygame.MOUSEBUTTONUP:
					pos = pygame.mouse.get_pos()
					for i in range(len(self.objectArray)):
						if(self.objectArray[i].box.IsInside(pos)):
							self.objectArray[i].Damage(self.hit)

	def AddObject(self,x,y):
		face = Face(x,y)
		self.objectArray.append(face)
		self.objectCount +=1
