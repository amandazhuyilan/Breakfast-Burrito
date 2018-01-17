class Solution:
	def climbStairs(self, numStairs):
		return self.fib(numStairs + 1)

	def fib(self, n):
		if n <= 1:
			return n
		else: return self.fib(n-1) + self.fib(n-2)

print(Solution().climbStairs(5))
