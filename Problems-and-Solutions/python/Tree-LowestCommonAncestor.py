# Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

# The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.


class TreeNodes(object):
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None
class Solution():
	def LCA(self, root, node1, node2):
		if root is None:
			return None

		if node1 is root or node2 is root:
			return root

		left_node = self.LCA(node.left, node1, node2)
		right_node = self.LCA(node.right, node1, node2)

		if left_node and right_node:
			return root 
		if left_node:
			return left_node
		if right_node:
			return right_node

		return None





