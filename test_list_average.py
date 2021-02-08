import unittest
import list_average

class TestListAverage(unittest.TestCase):

	def test_empty_list(self):
		result = list_average.list_average({})
		self.assertEqual(result, None)
		
	def test_filled_list(self):
		result = list_average.list_average({0, 2, 7})
		self.assertEqual(result, 3)
		
	def test_non_number(self):
		result = list_average.list_average({0, 2, "hello"})
		self.assertEqual(result, None)
		
if __name__ == "__main__":
	unittest.main()
