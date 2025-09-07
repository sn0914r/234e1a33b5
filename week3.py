from collections import deque

def dfs(graph, start, visited=None):
	if visited is None:
		visited = set()
	visited.add(start)
	print(start, end=' ')
	for neighbour in graph[start]:
		if neighbour not in visited:
			dfs(graph, neighbour, visited)

def dfs_stack(graph, start):
	visited = set()
	stack = [start]
	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			print(vertex, end=" ")
			visited.add(vertex)
			stack.extend(reversed(graph[vertex]))

def bfs(graph, start):
	visited = set()
	queue = deque([start])
	while queue:
		vertex = queue.popleft()
		if vertex not in visited:
			print(vertex, end=' ')
			visited.add(vertex)
			queue.extend(graph[vertex])

graph = {
	'A': ['B', 'C'], 
	'B': ['D'], 
	'C':['E', 'F'], 
	'D': [],
	'E': [],
	'F': []
}

print("DFS Recursive: ")
dfs(graph, 'A')
print("\nDFS using stack")
dfs_stack(graph, 'A')
print("\nBFS: ")
bfs(graph, 'A')