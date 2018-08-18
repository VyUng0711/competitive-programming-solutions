INF = float('inf')
class triad():
	def __init__(self, start, target, weight):
		self.start = start
		self.target = target
		self.weight = weight

def bellman_ford(start):
	dist[start] = 0
	for i in range(1, num_junctions):
		for j in range(num_roads):
			u = graph[j].start
			v = graph[j].target
			w = graph[j].weight
			if dist[u] != INF and dist[u] + w < dist[v]:
				dist[v] = dist[u] + w


num_tests = int(input())
for test in range(num_tests):
	blank = input()
	num_junctions = int(input())
	busyness_map = {}
	busyness = list(map(int, input().split()))
	num_roads = int(input())
	graph = []
	for r in range(num_roads):
		start, destination = map(int, input().split())
		start -= 1
		destination -= 1
		weight = (busyness[destination] - busyness[start])**3
		graph.append(triad(start, destination, weight))
	num_queries = int(input())
	queries = []
	for q in range(num_queries):
		this_q = int(input())
		queries.append(this_q - 1)
	dist = [INF] * num_junctions
	bellman_ford(0)
	print("Case {}".format(test + 1))
	for d in queries:
		if dist[d] < 3 or dist[d] == INF:
			print("?")
		else:
			print(dist[d])






