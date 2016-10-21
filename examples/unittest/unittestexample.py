# Unit test example on module a test class in testclass.py.

import unittest
from testclass import Simple

class TestExample(unittest.TestCase):

	def test(self):
		t = Simple(3,4)
		z = t.compute(2)
		self.assertTrue(t.getx()==3)
		self.assertTrue(t.gety()==4)
		self.assertTrue(z==(2*3+4))

if __name__ == "__main__":
	unittest.main()

