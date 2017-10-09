# Single linked-list contructor
class Node(object):
	def __init__(self, data = None, next_node = None):
		self.data = data
		self.next = next

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_next(self, new_next):
		self.next = new_next 

# Single linked list operations
class Single_Linked_List(object):
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def insert(self, data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node

	def size(self):
		current = self.head 
		count = 0 
		while current:
			count += 1
			current = current.get_next()
		return count

	def search(self, data):
		current = self.head
		found = False
		while current != None and not found:
			if current.get_data() == data:
				found = True 
			else:
				current = current.get_next()
		return found 

	def  delete(self, data):
		if self.head is None:
			return False
		else:
			current = self.head
			previous = None
			found = False

			while not found:
				if current.get_data() == data:
					found = True 
				else:
					previous = current 
					current = current.get_next()

			if previous == None:
				self.head = current.get_next()
			else:
				previous.set_next(current.get_next())

# TEST_CASE:
mylist = Single_Linked_List()

mylist.insert(31)
mylist.insert(77)
mylist.insert(87)
mylist.insert(3)
mylist.insert(24)

print("Original size: " + str(mylist.size()))
print("Search for 77: " + str(mylist.search(77)))

mylist.delete(24)

print("Size after removing one element: " + str(mylist.size()))

