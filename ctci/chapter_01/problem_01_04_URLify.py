import unittest

def urlify(str,length):
	total_length = len(str)

	for i in range(length-1, -1, -1):
		if str[i] == ' ':
			str[total_length - 3 : total_length] = '%20'
			total_length -= 3
		else:
			str[total_length - 1] = str[i]
			total_length -= 1
	return str


class Test(unittest.TestCase):
	'''Test Cases'''
	# Using lists because Python strings are immutable
	data = [
		(list('much ado about nothing      '), 22,
		 list('much%20ado%20about%20nothing')),
		(list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

	def test_urlify(self):
		for [test_string, length, expected] in self.data:
			actual = urlify(test_string, length)
			self.assertEqual(actual, expected)

if __name__ == "__main__":
	unittest.main()