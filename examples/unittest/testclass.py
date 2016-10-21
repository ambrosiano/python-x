# An example class to test.

class Simple():
	"""An example class to test."""
	def __init__(self,x,y):
		"""Constructor."""
		self.x = x
		self.y = y

	def compute(self,p):
		"""Computes p*x + y."""
		return (p*self.x + self.y)

	def getx(self):
		"""Gets x."""
		return self.x

	def gety(self):
		"""Gets y."""
		return self.y

