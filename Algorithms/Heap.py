# Binary heap is a complete binary tree where the parent node is alaways 
# smaller or greater than the child node. 
# Binary heaps can be implemented using arrays and it is very space 
# efficient. 
# If the parent node is stored in at index i, the left child 
# can be stored in the array as 2*i + 1 and the right child can be stored 
# as 2*i + 2.

# Implementing a max heap
def MaxHeapify(In_Arr, index):
	largest = index
	left = 2 * index + 1
	right = 2 * index + 2

	if left < len(In_Arr) and In_Arr[largest] < In_Arr[left]:
		largest = left
	if right < len(In_Arr) and In_Arr[largest] < In_Arr[right]:
		largest = right

	if largest != index:
		In_Arr[index], In_Arr[largest] = In_Arr[largest], In_Arr[index]
		MaxHeapify(In_Arr, largest)

def MaxHeapSort(In_Arr):
	N = len(In_Arr)

	# build a max heap
	for i in range(N//2, -1, -1):
		MaxHeapify(In_Arr, i)

	# putting the elements in descending order
	for i in range(1, len(In_Arr), 2):
		if In_Arr[i] < In_Arr[i + 1]:
			In_Arr[i] , In_Arr[i + 1] = In_Arr[i + 1] , In_Arr[i]

	return In_Arr

TEST_CASE = [5, 7, 8, 19, 2]
print(MaxHeapSort(TEST_CASE))

# Can also use heapq module (kinda cheating though :/)
import heapq

test_list = [5, 7, 8, 19, 2]

# heapify: convert list into min-heap. In place, linear time.
heapq.heapify(test_list)
print("heapified list: ")
print(list(test_list))

# heappush: push elements into heap
heapq.heappush(test_list, 4)
print("The modified list after pushing element is: ")
print(list(test_list))

#heappop: pop the smallest element
print("The smallest element popped is: ") 
print(heapq.heappop(test_list))







