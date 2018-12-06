import unittest

def zero_matrix(m):
	row_len = len(m)
	col_len = len(m[0])
	row = []
	col = []

	for r in range(row_len):
		for c in range(col_len):
			if m[r][c] == 0:
				row.append(r)
				col.append(c)

	for r in row:
		nullify_row(m, r)
		

	for c in col:
		nullify_col(m, c)

	return m


def nullify_row(m, row):
	for i in range(len(m)):
		m[row][i] = 0

def nullify_col(m, col):
	for i in range(len(m[0])):
		m[i][col] = 0




class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()