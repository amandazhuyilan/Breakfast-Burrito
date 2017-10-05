# Binary Search tree with following operations:
# Insert, Lookup, Delete, Print, Comparing two trees, returning tree  
# elements

# example testing tree:
#						 8
#					   /   \
#					  3     10
#				     / \      \
#					1   6     14
#				       / \    /
#					  4   7  13

class node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

# Insert node with value data. Look for right location recursively.
# ex. root.insert(3)
	def insert(self,data):
		if self.data:
			if data > self.data:
				if self.right is None:
					self.right = node(data)
				else:
					self.right.insert(data)

			elif data < self.data:
				if self.left is None:
					self.left = node(data)
				else: 
					self.left.insert(data)

			elif data == self.data:
				print("Node already exists!")
		else:
			self.data = data

# Lookup node with given data, do it recursively until find it. Returns 
# node and its parent 
# ex: root.lookup 
	def lookup(self, data, parent=None):
		if data < self.data:
			if self.left is None:
				return None, None

			return self.left.lookup(data, self)

		elif data > self.data: 
			if self.right is None:
				return None, None
			else: 
				return self.right.lookup(data,self)

		else:
			return self, parent
# Removes the node in the tree. Need to consider if the removed node has 
# 0, 1 or 2 children (added in count_children function) 
# Always need to consider different scenrios when node is root
	def delete(self, data):
		def count_children(self):
			count = 0 
			if self.left:
				count += 1
			if self.right:
				count += 1
			return count 

			node, parent = self.lookup(data)
			if node: 
				if count_children == 0:
					if parent: 
						if parent.left is node: 
							parent.left = None
						else:
							parent.right = None 
						del node 
					# If the node to be removed is a root:
					else:
						self.data = None

				if count_children == 1:
					if node.left:
						n = node.left
					if node.right:
						n = node.right 
					if parent:
						if parent.left is node:
							parent.left = n
						else:
							parent.right = n

					else:
						self.left = n.left
						self.right = n.right 
						self.data = n.data

				if count_children == 2:
					parent = node 
					successor = node.right 
					while successor.left:
						parent = successor
						successor = successor.left
					node.data = successor.data
					if parent.left == successor:
						parent.left = successor.right
					else:
						parent.right = successor.right

# Use recursive to walk tree depth-first. Left subtree->Root->Right 
# subtree	
	def print_tree(self):
		if self.left:
			self.left.print_tree()
		print self.data
		if self.right:
			self.right.print_tree()

#Tests
root = node(8)
root.insert(3)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(2)
root.insert(5)
root.insert(10)
root.insert(14)
root.insert(13)


print(root.lookup(6))


