#tile class to store my tiles
from Sprite import Sprite
from geometry import Rect

class TileSet:
	def __init__(self,path,tileWidth,tileHeight):
		self.box = Rect(0,0,0,0)
		self.tileWidth = tileWidth
		self.tileHeight = tileHeight
		self.tileSet = Sprite(path)
		self.box.width = self.tileSet.GetWidth()
		self.box.height = self.tileSet.GetHeight()
		self.columns = self.box.width/tileWidth
		self.rows = self.box.height/tileHeight
		self.dimension = [0,0,0]

	def Render(self,index,x,y):
		xPos = 0		
		yPos = 0
		if(index>-1 and index<self.rows*self.columns-1):
			xPos = index%self.columns
			xPos *= self.tileWidth
			yPos = index/self.columns
			yPos *= self.tileHeight
			self.tileSet.SetClip(xPos,yPos,self.tileWidth,self.tileHeight)
			self.tileSet.Render(x,y)

	def GetTileWidth(self):
		return self.tileWidth

	def GetTileHeight(self):
		return self.tileHeight


class TileMap:

	def __init__(self,file,tileSet):
		self.tileMatriz = []
		self.tileSet = tileSet
		self.Load(file)

	def Load(self,file):
		#le o arquivo de tile set
		with open(file) as arq:
		    lines =  [line.rstrip('\n') for line in open(file)]

		#lines possui todo meu arquivo txt
		self.dimension = [int(x) for x in lines[0].split(',')]
		lines.pop(0)
		lines.pop(0)
		#lines possui apenas as matrizes agora
		#dimension possui as dimensoes da matriz
		for line in lines:
			if line:
		 		temp=[int(x)-1 for x in line.split(',')]			
		 		for x in temp:
					self.tileMatriz.append(x)

	def SetTileSet(self,tileSet):
		self.tileSet = tileSet

	def At(self,x,y,z):
		rigthPos = x*self.dimension[0] + y + z*self.dimension[0]*self.dimension[1]
		return self.tileMatriz[rigthPos]

	def RenderLayer(self,layer,cameraX,cameraY):
		xPoint = 0
		yPoint = 0
		for i in range(self.dimension[0]):
			xPoint = 0
			for j in range(self.dimension[1]):
				self.tileSet.Render(self.At(i,j,layer),xPoint,yPoint)
				xPoint += self.tileSet.GetTileWidth()

			yPoint += self.tileSet.GetTileHeight()

	def Render(self,cameraX,cameraY):
		for x in range(self.dimension[2]):
			self.RenderLayer(x,cameraX,cameraY)

	def GetWidth(self):
		return self.dimension[0]

	def GetHeight(self):
		return self.dimension[1]

	def GetDepth(self):
		return self.dimension[2]

