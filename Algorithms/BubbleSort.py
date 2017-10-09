# Bubble sort, inefficient but easy sorting algorithm. Runs in O(n^2).
# It works by repeatedly swapping adjacent elements that are out of order.
def BubbleSort(In_Arr):
	if len(In_Arr) < 2:
		return In_Arr
	else:
		for i in range(len(In_Arr)):
			for j in range(len(In_Arr)-i-1):
				if In_Arr[j] > In_Arr[j+1]:
					In_Arr[j], 	In_Arr[j+1] = In_Arr[j+1], 	In_Arr[j] 

	return In_Arr


TEST_CASE = [3, 80, 23, 78, 12]
print(BubbleSort(TEST_CASE)) 