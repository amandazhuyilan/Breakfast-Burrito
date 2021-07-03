class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.right, self.left = None, None

class Solution:
	def maxDepth(self, root):
		if root is None:
			return 0
		return max(self.maxDepth(root.left), self.maxDepth(root.right))+1