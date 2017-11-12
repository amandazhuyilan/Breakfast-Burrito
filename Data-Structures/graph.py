# We want to produce graphs that looks like this:
# 			vertex = [connected verticies]

# graph = { "a" = ["c"],
#			"b" = ["c","e"],
#			"c" = ["a","b","d","e"],
#			"d" = ["c"],
# 			"e" = ["b","c"],
# 			"f" = []

# }


from collections import defaultdict

class graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		# add edge v into the dictionary entry for vertex u
		self.graph[u].append(v)

	def generate_edges(self):
		edges = []

		for node in self.graph:	# each node in a graph
			for neighbour in self.graph[node]:	# each neighbour node for each single node
				edges.append((node, neighbour))
		return edges

	def  graph_BFS(self, s):
		if len(self.graph) == 0:
			return None
		visited = [False]*len(self.graph)
		queue = []

		visited[s] = True 
		queue.append(s)

		while queue:
			s = queue.pop(0)
			print(s)

			for node in self.graph[s]:
				if visited[node] == False:
					queue.append(node)
					visited[node] = True 

	def graph_DFS_helper(self, v, visited):
		visited[v] = True
		print(v)

		for node in self.graph[v]:
			if visited[node] == False:
				self.graph_DFS_helper(node, visited)

	def graph_DFS(self, s):
		visited = [False] * len(self.graph)
		self.graph_DFS_helper(s, visited)

g = graph()		

g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,2)

# prints generated graph 
#print(generate_edges(graph))

# prints the nodes in BFS format
#print("Printed in BFS format:", graph_BFS(graph, 0))

# prints the nodes in DFS format:
print("Printed in DFS format:", g.graph_DFS(2) )
