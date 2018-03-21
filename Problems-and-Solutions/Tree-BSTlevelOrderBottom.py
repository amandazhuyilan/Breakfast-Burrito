class TreeNode:
	def __init__(self, val):
		self.val = val
		self.right, self.left = None, None

class Solution:
	def levelOrderBottom(self, root):
		result = []
		this_level = [root]

		if root is None:
			return result

		while this_level:
			result_temp = []
			next_level = []
			for node in this_level:
				if node.left:
					next_level.append(node.left)
				if node.right:
					next_level.append(node.right)
			for node in this_level:
				result_temp.append(node.val)
			this_level = next_level
			result.append(result_temp)
		return result[::-1]



