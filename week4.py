from queue import PriorityQueue

graph = {
	'A': {'B': 5, 'C': 2},
	'B': {'D': 4},
	'C': {'B': 8, 'D': 7},
	'D': {'E': 6},
	'E': {}
}

heuristic = {
	'A': 10,
	'B': 6,
	'C': 4,
	'D': 2,
	'E': 0
}

def a_star(start, goal):
	open_set = PriorityQueue()
	open_set.put((0, start))
	came_from = {}
	g_score = {node: float('inf') for node in graph}
	g_score[start] = 0
	
	while not open_set.empty():
		current_f, current = open_set.get()
		
		if current == goal:
			path = []
			
			while current in came_from:	
				path.append(current)
				current = came_from[current]	
			path.append(start)
			return path[::-1]
		for neighbour in graph[current]:
			tentative_g = g_score[current] + graph[current][neighbour]
			if tentative_g < g_score[neighbour]:
				came_from[neighbour] = current
				g_score[neighbour] = tentative_g
				f_score = tentative_g + heuristic[neighbour]
				open_set.put((f_score, neighbour))
	return None;

start_node = 'A'
goal_node = 'E'
path = a_star(start_node, goal_node)
print(f"shortest path from {start_node} to {goal_node} : {path}")
