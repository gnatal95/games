import GameObject
import Sprite
import geometry

class Face(GameObject.GameObject):

	def __init__(self,x,y):
		self.box = geometry.Rect(x,y,0,0)
		self.hitPoints = 30
		self.sp = Sprite.Sprite('img/penguinface.png')
		self.box.width = self.sp.GetWidth()
		self.box.height = self.sp.GetHeight()
		self.box.x = (2*self.box.x-self.box.width)/2		
		self.box.y = (2*self.box.y-self.box.height)/2
	
	def Damage(self,damage):
		self.hitPoints -= damage

	def Update(self):
		pass
	def Render(self):

		self.sp.Render(self.box.x,self.box.y)

	def IsDead(self):
		if  0 >= self.hitPoints:
			return True 
		return False
