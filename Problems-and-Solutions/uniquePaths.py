# A robot is located at the top-left corner of a m x n grid.

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.

# Given m = 3 and n = 3, return 6.
# Given m = 4 and n = 5, return 35.

class Solutions:
	def uniquePaths(self,row, col):
		paths = [[0 for x in range(col)] for y in range(row)]
		print(paths)

		for i in range(row):
			paths[i][0] = 1

		for j in range(col):
			paths[0][j] = 1

		for i in range(1, row):
			for j in range(1, col):
				paths[i][j] = paths[i-1][j] + paths[i][j-1]

		return paths[i][j]

print(Solutions().uniquePaths(4,5))