# Quicksort  O(n log n) in-place. Chooses a pivot (the last one in this 
# case, can be any number in the input array) and compare the elements in
# the input array with the pivot. If greater than pivot, append to the 
# more array, else if less than put in less array, put element in equal 
# array if it equals to pivot. 
# Do this recursively and finally return the sorted array.

def QuickSort(A):
	if len(A) < 2:
		return A

	equal = []
	less = []
	more = []

	pivot = A[-1]

	for i in A:
		if i < pivot:
			less.append(i)
		elif i > pivot:
			more.append(i)
		elif i == pivot:
			equal.append(i)

	return QuickSort(less) + equal + QuickSort(more)

def QuickSort_in_place(A, start, end):
	if start >= end:
		return 

	left = start
	right = end 
	pivot = A[(start+end)//2]

	while left <= right:
		while left <= right and A[left] < pivot:    # if the elements are in their right places, leave them alone and move the left/right pointers to the next one
			left += 1

		while left <= right and A[right] > pivot:
			right -= 1

		if left <= right:
			A[left], A[right] = A[right], A[left]
			left += 1
			right -= 1

	QuickSort_in_place(A, start, right)
	QuickSort_in_place(A, left, end)

	return A

TEST_CASE = [10,5,45,3,2,12]
print(QuickSort(TEST_CASE))
print(QuickSort_in_place(TEST_CASE,0,5))



