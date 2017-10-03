# Single linked-list
class Single_Linked_List_Node(object):
	def __init__(self, data = None, next_node = None):
		self.data = data
		self.next_node = next_node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		self.next_node = new_next 

class Single_Linked_List(object):
	def __init__(object):
		self.head = head

	def insert(self, data):
		new_node = Single_Linked_List_Node(data)
		new_node.set_next(self.head)
		self.head = new_node

	def size(self):
		cuurent 

class Double_Linked_List_Node(object):
	def __init__(self, data = None, next_node = None, previous_node = None):
		self.data = data
		self.next_node = next_node 
		self.previous node = previous_node 

	def get_data(self):
		return self.data = data

	def get_next(self):
		return self.next_node 

	def set_next(self, new_next):
		self.next_node = new_next
