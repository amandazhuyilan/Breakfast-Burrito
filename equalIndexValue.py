
# Given a sorted ascending array T, determine if there exists an extry 
# where the value equals to the corresposing index. 
# Prints "True" when it exists and "False" when doesnt exists.

def equalIndexValue(T):
	mid = len(T)/2

	print (mid)

	if mid == T[mid]:
		print ("True")
		exit()

	if mid == 0:
		print("False")
		exit()

	if mid < T[mid]:
		T = T[:mid]
		equalIndexValue(T)

	elif mid > T[mid]:
		T = T[mid:]
		equalIndexValue(T)



TEST_CASE = [1, 2, 5, 7, 9]

equalIndexValue(TEST_CASE)