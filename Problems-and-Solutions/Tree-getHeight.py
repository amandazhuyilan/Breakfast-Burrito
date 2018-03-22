class TreeNode(object):
	def __init__(self, val):
		self.val = val;
		self.left, self.right = None, None
class Solution():
	def getHeight(self, root):
		if root is None:
			return 0
		left, right = self.getHeight(root.left), self.getHeight(root.right)
		return max(left, right) + 1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(5)
root.left.right = TreeNode(6)
root.left.left.left = TreeNode(8)

print(Solution().getHeight(root))
