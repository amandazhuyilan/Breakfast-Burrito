#sort the input array in ascending order.
#Worst-case: O(n^2)
def Insertion_Sort_Ascending (A):
	for j in range (1, len(A)):
		key = A[j]
		i = j - 1

		while i >= 0 and A[i] > key:
			A[i + 1] = A[i]
			i = i - 1

		A[ i + 1 ] = key 

	return A

def Insertion_Sort_Descending (A):
	for j in range (1, len(A)):
		key = A[j]
		i = j - 1

		while i >= 0 and A[i] < key: 
			A[i + 1] = A[i]
			i = i - 1

		A[i + 1] = key

	return A 

TEST_CASE = [1,20,4,78]

print (Insertion_Sort_Ascending(TEST_CASE))
print (Insertion_Sort_Descending(TEST_CASE))


