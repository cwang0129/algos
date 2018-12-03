import unittest

def string_compression(str_input):
	count = 0
	compressed = []

	for i in range(len(str_input)):
		if i != 0 and str_input[i] != str_input[i - 1]:
			compressed.append(str_input[i - 1] + str(count))
			count = 0
		count += 1

	compressed.append(str_input[-1]+ str(count))

	return min(str_input, ''.join(compressed), key=len)

class Test(unittest.TestCase):
	'''Test Cases'''
	data = [
		('aabcccccaaa', 'a2b1c5a3'),
		('abcdef', 'abcdef')
	]

	def test_string_compression(self):
		for [test_string, expected] in self.data:
			actual = string_compression(test_string)
			self.assertEqual(actual, expected)

if __name__ == "__main__":
	unittest.main()
	