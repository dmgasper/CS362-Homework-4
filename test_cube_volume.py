import unittest
import cube_volume

class TestCubeVolume(unittest.TestCase):

	def test_real_num(self):
		result = cube_volume.cube(3)
		self.assertEqual(result, 27)
	
	def test_negative_num(self):
		result = cube_volume.cube(-1)
		self.assertEqual(result, -1)
		
	def test_not_real_num(self):
		result = cube_volume.cube("hello")
		self.assertEqual(result, -1)
		
if __name__ == "__main__":
	unittest.main()
