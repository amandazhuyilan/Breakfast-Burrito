# Given a binary tree, find the subtree with minimum sum. Return the root of the subtree

class Treenode(object):
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	result = None
	min_sum = 0 

	def findSubtree(self, root):
		self.dfs(root)
		return self.result 

	def DFS(self, node):
		if node is None:
			return 0
		left_node = self.DFS(node.left)
		right_node = self.DFS(node.right)

		if node.val + left_node + right_node < self.min_sum:
			self.min_sum = node.val + left_node + right_node
			self.result = node
		return node.val + left_node + right_node