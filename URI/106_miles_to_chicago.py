INF = float('inf')
class Triad():
	def __init__(self, source, target, weight):
		self.source = source
		self.target = target
		self.weight = weight

def bellman_ford(start):
	dist[start] = 1
	for i in range(1, num_intersections):
		for j in range(num_streets*2):
			u = graph[j].source
			v = graph[j].target
			w = graph[j].weight
			if dist[u] != -INF and dist[u] * w > dist[v]:
				dist[v] = dist[u] * w


while True:
	first_line = input()
	if first_line == 0:
		break
	num_intersections, num_streets = map(int, first_line.split())
	graph = []
	dist = [-INF] * num_intersections
	for i in range(num_streets):
		a, b, p = map(int, input().split())
		graph.append(Triad(a - 1, b - 1, p/100))
		graph.append(Triad(b - 1, a - 1, p/100))
	bellman_ford(0)
	print(dist)
	print("{} percent".format(dist[-1] * 100))


