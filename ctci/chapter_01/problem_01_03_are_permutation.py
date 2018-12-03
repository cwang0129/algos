import unittest
from collections import Counter

def arePermutation(s1, s2):
	if len(s1) != len(s2):
		return False

	counter = Counter()
	for char in s1:
		counter[char] += 1
	for char in s2:
		if counter[char] == 0:
			return False
		counter[char] -= 1
	return True

class arePermutationTest(unittest.TestCase):
	dataT = (
		('abcd', 'bacd'),
		('3563476', '7334566'),
		('wef34f', 'wffe34'),
		)
	dataF = (
		('abcd', 'd2cba'),
		('2354', '1234'),
		('dcw4f', 'dcw5f'),
		)

	def test_cp(self):
		# true check
		for test_strings in self.dataT:
			result = arePermutation(*test_strings)
			self.assertTrue(result)
		# false check
		for test_strings in self.dataF:
			result = arePermutation(*test_strings)
			self.assertFalse(result)

if __name__ == '__main__':
	unittest.main()