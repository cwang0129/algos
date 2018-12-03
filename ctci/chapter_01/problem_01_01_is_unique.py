import unittest

def isUnique(str_input):
	characters = {}
	for char in str_input:
		if char in characters:
			return False
		characters[char] = 1
	return True

class isUniqueTest(unittest.TestCase):
	TEST_DATA = [
		('a', True),
		('aa', False),
		('ab', True),
		('ab ', True),
		('', True),
		(' ', True),
		('  ', False),
		('qwerty', True),
		('qwerte', False)
		]

	def test_isUnique(self):
		for str_, expected_result in self.TEST_DATA:
			result = isUnique(str_)
			self.assertEqual(result, expected_result)

if __name__ == '__main__':
	unittest.main()
