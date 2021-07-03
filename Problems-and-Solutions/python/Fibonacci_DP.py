def Fibonacci_DP(n):
	if n is None:
		return -1
	fib = []
	fib.insert(0, 0)
	fib.insert(1, 1)

	for i in range(2, n + 1):
		fib.insert(i, (fib[i - 1] + fib[i - 2]))

	return fib[n]

print(Fibonacci_DP(6))