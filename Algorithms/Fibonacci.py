def Recursive_Fib(self, n):
	if n == 0 or n == 1:
		return n
	else:
		return Recursive_Fib(n-1) + Recursive_Fib(n-2)

def DP_Fib(self,n):
	if n == 0 or n == 1:
		return n
	else: 
		arr = []
		arr[0] = arr[1] = 1
		for i in range(2, n):
			arr[i] = arr[i-1] + arr[i-2]
	return arr[n]


TEST_CASE = 10
print("Recursive Method: "Recursive_Fib(TEST_CASE))
print("DP Method:" DP_Fib(TEST_CASE))
