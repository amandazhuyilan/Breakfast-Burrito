# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

# Calling next() will return the next smallest number in the BST.

# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class BSTIterator(object):
	def __init__(self, root):
		self.stack = []
		self.push_stack(root)

	def hasNext(self):
		return self.stack

	def Next(self):
		top = self.stack.pop()
		self.push_stack(top)
		return top.val

	def push_stack(self, node):
		while node:
			self.stack.append(node)
			node = node.left

