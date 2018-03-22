# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# A single node tree is a BST

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	import sys

	def isValidBST(self, root):
		return self.ValidBST(root, -sys.maxint, sys.maxint)

	def ValidBST(self, node, min, max):
		if node is None:
			return True 
		if node.val >= max or node.val <= min:
			return False
		return self.ValidBST(node.left, min, node.val) and self.ValidBST(node.right, node.val, max)

