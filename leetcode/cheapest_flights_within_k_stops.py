# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

import queue
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = [[] * n for _ in range(n)]
        for f in flights:
            graph[f[0]].append((f[2], f[1]))
        pq = queue.PriorityQueue()
        pq.put((0, src, K + 1))
        
        visited = [False] * n
        
        while not pq.empty():
            top = pq.get()
            visited[top[1]] = True
            if dst == top[1]:
                return top[0]
            
            if top[2] > 0:
                for neighbor in graph[top[1]]:
                    if not visited[neighbor[1]]: 
                        pq.put((top[0] + neighbor[0], neighbor[1], top[2] - 1))
     
        return -1


