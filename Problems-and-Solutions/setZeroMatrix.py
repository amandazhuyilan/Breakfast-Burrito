# Given an n x m matrix, if an element is 0, set its entire row and
# column to 0. Do it in place.

# Use the first row and column as an indicator to decide accordinating row
# or column has an zero.

class solution:
	def setZeroMatrix(self, matrix):
		if matrix == None or len(matrix) == 0:
			return False

		set_first_row = False
		set_first_column = False

		# Check if first row/column has zeros in it.
		if 0 in matrix[0]:
			set_first_row = True

		for i in range(len(matrix[0])):
			if matrix[0][i] == 0:
				set_first_column = True

		# Check everything else in the matrix to see if there are any zeros
		# and set the corresonding first row/column to zero.

		for i in range(1, len(matrix)):
			for j in range(1, len(matrix[0])):
				if matrix[i][j] == 0:
					matrix[0][j] = 0
					matrix[i][0] = 0

		for i in range(1, len(matrix)):
			for j in range(1, len(matrix[0])):
				if matrix[i][0] == 0 or matrix[0][j] == 0:
					matrix[i][j] = 0

		if set_first_column:
			for i in range(len(matrix[0])):
				matrix[i][0] = 0

		if set_first_row:
			for i in range(len(matrix)):
				matrix[0][j] = 0

		return matrix 


TEST_CASE = [[1, 2, 3], [5, 6, 0]]
func = solution()
print(func.setZeroMatrix(TEST_CASE))