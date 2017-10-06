# Counting sort, sorting in O(n)
# In_Array is the input array of numbers, 
# Out_Array is the output sorted array.
# Index_Array is the auxiliary array that holds the number of elememts 
# equal to the # index of Index_Arr. Based on the number of entires 
# specified in th Index_Arr, the Out_Arr stores the sorted array in an 
# ascending order.

def CountingSort(In_Arr):
	Out_Arr = [] * len(In_Arr)
	Index_Arr = [0] * (max(In_Arr) + 1)

	for i in range(len(In_Arr)):
		Index_Arr[In_Arr[i]] += 1
		#  C contains the number of elements equal to i

	for i in range(len(Index_Arr)):
		if Index_Arr[i] != 0:
			for j in range(Index_Arr[i]):
				Out_Arr.append(i)

	return Out_Arr

TEST_CASE = [2,3,1,5,4,4]

print(CountingSort(TEST_CASE))
