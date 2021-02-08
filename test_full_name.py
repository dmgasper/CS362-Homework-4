import unittest
import full_name

class TestFullName(unittest.TestCase):
	
	def test_empty_input(self):
		result = full_name.full_name("", "")
		self.assertEqual(result, "")
		
	def test_full_input(self):
		result = full_name.full_name("Hello", "World")
		self.assertEqual(result, "Hello World")
		
	def test_bad_input_type(self):
		result = full_name.full_name(None, None)
		self.assertEqual(result, "")
		
if __name__ == "__main__":
	unittest.main()
