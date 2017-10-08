# Quicksort  O(n log n) in-place. Chooses a pivot (the last one in this 
# case, can be any number in the input array) and compare the elements in
# the input array with the pivot. If greater than pivot, append to the 
# more array, else if less than put in less array, put element in equal 
# array if it equals to pivot. 
# Do this recursively and finally return the sorted array.
def QuickSort(In_Arr):
	less = []
	more = []
	equal = []

	if len(In_Arr) > 1:
		# Pick last element of array as pivot
		pivot = In_Arr[-1]
		for i in range(len(In_Arr)):
			if pivot > In_Arr[i]:
				less.append(In_Arr[i])
			elif pivot < In_Arr[i]:
				more.append(In_Arr[i])
			elif pivot == In_Arr[i]:
				equal.append(In_Arr[i])

		return QuickSort(less) + equal + QuickSort(more)

	else:
		return In_Arr


TEST_CASE = [10,5,45,3,2,12]
print(QuickSort(TEST_CASE))




