#geometri
import math

class Rect:
	def __init__(self,x,y,width,height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def IsInside(self,point):
		if point[0] > self.x and self.x+self.width > point[0] and point[1] > self.y  and self.y+self.width > point[1]:
			return True
		return False

	def GetCenter(self):
		center =((self.x+self.width)/2,(self.y+self.height)/2)
		return center

	def RectPlusVect(self,point):
		self.x += point[0]
		self.x += point[1]

class Vec2:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def MultipliByScalar(self,times):
		self.x *=times
		self.y *=times

	def Absolute(self):
		return sqrt(self.x**2 + self.y**2)

	def Direction(self):
		unitary = (self.x,self.y)
		return	unitary/self.Absolute()

	def Distance2Points(self,x,y):
		return sqrt((self.x-x)**2 + (self.y-y)**2)

	def Angle(self):
		return atan2(self.y,self.x)

	def Rotate(self,theta):
		self.x = self.x*cos(theta) - self.y*sin(theta)
		self.y = self.y*cos(theta) + self.x*sin(theta)
