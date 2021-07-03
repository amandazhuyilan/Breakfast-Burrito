# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution():
	def levelOrder(self, root):
		result = []
		this_level = [root]

		if root is None:
			return result

		while this_level:
			temp = []
			next_level = []

			for node in this_level:
				if node.left:
					next_level.append(node.left)
				if node.right:
					next_level.append(node.right)
				temp.append(node.val)

			result.append(temp)
			this_level = next_level
		return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.root = TreeNode(5)

print(Solution().levelOrder(root))


