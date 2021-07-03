def find_path(graph, start, end, path = []):
	path = path + [start]
	if start == end:
		return path 
	if start not in graph:
		return None
	for node in graph[start]:
		if node not in path:
			newpath = find_path(graph, node, end, path)
			if newpath:
				return newpath
	return None

def find_all_paths(graph, start, end, path = []):
	path = path + [start]
	if start == end:
		return [path]
	if start not in graph:
		return None

	paths = []
	for node in graph[start]:
		if node not in path:
			newpaths = find_all_paths(graph, node, end, path)
			for newpath in newpaths:
				paths.append(newpath)
	return paths

def find_shortest_path(graph, start, end, path = []):
	path = path + [start]
	if start == end:
		return path
	if start not in graph:
		return None
	shortest = None
	for node in graph[start]:
		if node not in path:
			newpath = find_shortest_path(graph, node, end, path)
			if newpath:
				if not shortest or len(shortest) > len(newpath):
					shortest = newpath
	return shortest
	
graph = {
	'A' : ['B', 'C'],
	'B' : ['A','C','D'],
	'C' : ['A','B','D','E'],
	'D' : ['B','C'],
	'E' : ['C','F'],
	'F' : ['E']
}

print("Find a path: ", find_path(graph, 'A', 'F',[]))
print("Find all paths: ", find_all_paths(graph, 'A','F',[]))
print("Find shortest path: ", find_shortest_path(graph, 'A','D',[]))