# inserts into the buffer queue
def buffer_write(data, loop_buffer):
	print("write:", data) 
	global new
	global old

	if new < len(loop_buffer):
		loop_buffer[new] = data
		new += 1

	elif new == len(loop_buffer):
		loop_buffer[0] = data
		old += 1
	print(loop_buffer)


# reads the oldest element and remove the entry from the queue without shrinking the size of the queue
def buffer_read(loop_buffer):
	if len(loop_buffer) == 0:
		return None

# we retrive the oldest element by putting the r
	result = loop_buffer.pop(old)
	loop_buffer.append(None)

	global new 
	new -= 1
	return(result)


old = 0
new = 0

# Setting up buffer1 with size variable and doing a read/write 

size = 4
buffer1 = [None]* (size) # Initializing buffer1 

buffer_write(1, buffer1)
buffer_write(2, buffer1)
buffer_write(3, buffer1)
print("read:" ,buffer_read(buffer1))
buffer_write(4, buffer1)
buffer_write(5, buffer1)
buffer_write(6, buffer1)
