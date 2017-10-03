# Level order traversal of a binary tree
class node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Solution 1: traversal through tree. Need height, print given level to 
# get to final print traversal order.

def printTraversalOrder(root):
	if root == None:
		return False

	else: 
		for i in range(1, height(root)):
			printGivenLevel(root, i)
# Using function to print a given level. From root traversal left/right 
# while level decreases.
def printGivenLevel(root, level):
	if root is None:
		return False
	if level == 1:
		print (root.data)

	elif level > 1:
		printGivenLevel(root.left, level - 1)
		printGivenLevel(root.right, level -1)

# Recursive function to return the height of the node. 
def height(node):
	if node == None:
		return 0
	else:
		left_height = height(node.left)
		right_height = height(node.right)

		if left_height > right_height:
			return left_height + 1
		else: return right_height + 1

# Solution 2: Using a FIFO queue. Append left child then right child into 
# queue. Then pop from queue to print.
def printTraversalOrder_queue(root):
	if root is None:
		return False

	queue = []

	queue.append(root)

	while(len(queue)) > 0:
		print (queue[0].data)
		node = queue.pop(0) #removes and returns the last item in the list

		if node.left is not None:
			queue.append(node.left)

		if node.right is not None:
			queue.append(node.right)

# Test cases:
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)
root.right.right.left = node(8)

print("BFS traversal:")
printTraversalOrder(root)

print("BFS traversal with queue:")
printTraversalOrder_queue(root)





