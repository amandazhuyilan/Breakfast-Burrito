class Node:
	def __init__(self,data):
		self.data = data 
		self.left = None
		self.right = None

def size(node):
	if node == None:
		return 0
	else:
		return (size(node.left)+1+size(node.right))

def maxDepth(node):
	if node == None:
		return 0
	else:
		return max(maxDepth(node.left), maxDepth(node.right))+ 1
def minDepth(node):
	if node == None:
		return 0
	if node.left is None and node.right is None:
		return 1
	if node.left is None:
		return minDepth(node.right) + 1
	if node.right is None:
		return minDepth(node.left) + 1
	return min(minDepth(node.right), minDepth(node.right)) + 1

def preorder(root):
	if root != None:
		print(root.data)
		preorder(root.left)
		preorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.right.right.right.right = Node(7)

print ("Size of the tree is %d" %(size(root)))
print ("Max depth of the tree is", maxDepth(root))
print ("Min depth of the tree is", minDepth(root))
print("Preorder:", preorder(root))

