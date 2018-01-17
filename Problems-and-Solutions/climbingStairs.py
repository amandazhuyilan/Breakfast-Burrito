# Caluculate the different ways of climbing the stairs, assuming this person can only climb 1 or 2 steps at a time

# Solved by using recursion

class Solution:
	def climbStairs(self, numStairs):
		return self.fib(numStairs + 1)

	def fib(self, n):
		fib = []
		fib.insert(0, 0)
		fib.insert(1, 1)

		for i in range(2, n + 1):
			fib.insert(i, fib[i - 1] + fib[i - 2])

		return fib[n]

	def climbStairsMultiple(self, numStairs, numSteps):
		return self.fib_multiple(numStairs + 1, numSteps)

	def fib_multiple(self, n, m):
		result = 0
		for i in range(m):
			if n <= 1:
				return n
			result = result + self.fib_multiple(n-1, m) + self.fib_multiple(n-2, m)
			return result

print(Solution().climbStairsMultiple(4,2))
print