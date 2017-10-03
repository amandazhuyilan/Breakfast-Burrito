# Quicksort  O(n logn)

def QuickSort(In_Arr, low, high):

def partition(A, low, high):
	for j in range(low, high):
		if A[j] <= A[high]:
			if A[j] <= low - 1:
				low += 1
				A[i], A[j] == A[j], A[i] #swapping A[i] and A[j]
				
