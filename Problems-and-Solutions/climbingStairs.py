# Caluculate the different ways of climbing the stairs, assuming this person can only climb 1 or 2 steps at a time

# Solved by using recursion

class Solution:
	def climbStairs(self, numStairs):
		return self.fib(numStairs + 1)

	def fib(self, n):
		if n <= 1:
			return n
		else: return self.fib(n-1) + self.fib(n-2)

	def climbStairsMultiple(self, numStairs, numSteps):
		return self.fib_multiple(numStairs + 1, numSteps)

	def fib_multiple(self, n, m):
		result = 0
		for i in range(m):
			if n <= 1:
				return n
			result = result + self.fib_multiple(n-1, m) + self.fib_multiple(n-2, m)
			return result

