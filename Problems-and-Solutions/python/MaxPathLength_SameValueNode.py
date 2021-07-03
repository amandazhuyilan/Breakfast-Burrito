# This is an coding sample encountered in an Online Assement.
# Given two int arrays A, E, while A[j] stores the value of the node in a binary tree on their (j+1)th index, 
# while E indicates edge connection between node j and j+1 on E[2j] and E[2j+1] 

# return the longest length between two tree nodes who have the same value

# My approach is to construct a boolean adjacency matrix to respresent the exisiting(?) edge bewteen nodes by running through 
# the contents in array E (if there is an edge then True, else False), a counter_list is created to keep track of the length of the
# nodes with same value. Finally this method will return the maximum value of the contents in counter_list. 


def MaxPathlength_SameValueNode(A, E):
    # write your code in Python 2.7
    if len(A) < 2:
        return 1

    table = [[False] * len(A) for i in range(len(A))]
    for i in range(0, len(E), 2):
        table[int(E[i]) - 1][int(E[i + 1]) - 1] = True

    counter_list = []
    for i in range(0, len(A)):
        for j in range(0, len(A)):
            if table[i][j] == True and A[i] == A[j]:
                counter = 1
                for k in range(1, len(A) - j):
                    if table[i][j + k] == True and A[i] == A[j + k]:
                        counter += 1

                counter_list.append(counter)
    if len(counter_list) > 0:
        return max(counter_list)
    else:
        return 0


print(solution([1, 1, 1, 2, 2], [1, 2, 1, 3, 2, 4, 2, 5]))
