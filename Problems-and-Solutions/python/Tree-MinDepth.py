class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.right, self.left = None, None


class Solution():
	def MinDepth(self, root):
		if root is None:
			return 0
		if root.left is None and root.right is None:
			return 1
		if root.left is None:
			return self.MinDepth(root.right) + 1
		if root.right is None:
			return self.MinDepth(root.left) + 1
		return min(self.MinDepth(root.left), self.MinDepth(root.right)) + 1