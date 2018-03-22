class TreeNode():
	def __init__(self, val):
		self.val = val
		self.right, self.left = None, None

class Solution():
	def BinaryTreePath(self, root):
		result = []
		if root is None:
			return result
		self.dfs(root, result, [])
		return result

	def dfs(self, node, result, temp):
		temp.append(str(node.val))
		if node.left is None and node.right is None:
			result.append('->'.join(temp))
			temp.pop()
			return 
		if node.left:
			self.dfs(node.left, result, temp)
		if node.right:
			self.dfs(node.right, result, temp)

		temp.pop()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(5)
root.left.right = TreeNode(6)

print(Solution().BinaryTreePath(root))