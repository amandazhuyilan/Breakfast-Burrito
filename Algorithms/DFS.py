# Depth First Traversals: In-order/Pre-order/Post-order
class node:
	def __init__(self,data):
		self.left = None
		self.right = None
		self.data = data

def printInOrder(self, root):
	if root is None:
		return False

	else: 
		printInOrder(root.left)
		print(root.data)
		printInOrder(root.right)

def printPreOrder(self, root):
	if root is None:
		return False

	else: 
		print(root.data)
		printPreOrder(root.left)
		printPreOrder(root.right)

def printPostOrder(self, root):
	if root is None:
		return False

	else:
		printPostOrder(root.left)
		printPostOrder(root.right)
		print(root.data)

		
