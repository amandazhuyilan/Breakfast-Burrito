# Determines if the single linked list has a loop in it.
# Uses Floyd's hare-and-turtle algorithm, make a fast pointer that travels in two nodes at a time, 
# and a slow pointer that travels one node at a time. 
# If there exists a loop in the linked-list, fast and slow will meet.

def hasLoop(self, root):
	if root is None:
		return False
	else: 
		fast = root.next
		slow = root
		if slow.data == fast.data:
			return True 
		elif slow is not None and fast is not None and fast.next is not None:
			slow = slow.next 
			fast = fast.next.next

			
