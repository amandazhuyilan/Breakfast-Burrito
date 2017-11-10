def next_step(current, tower):
	steps_arr = []
	for i in range(tower[current]):
		steps_arr = 





def is_hoppable(tower):
	current = 0
	while True:
		if current >= len(tower):
			return True 
		if tower[current] == 0:
			return False
		current = next_step(current, tower)


