# https://www.hackerrank.com/challenges/primsmstsub/problem
# Submission on hackerrank:
import math
import os
import random
import re
import sys
import queue

# Complete the prims function below.
class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
    def __lt__(self, other):
        return self.dist <= other.dist
    
def prims(n, graph, start):
    dist = [float('inf') for i in range(n)]
    visited = [False for i in range(n)]
    pq = queue.PriorityQueue()
    pq.put(Node(start, 0))
    dist[start] = 0
    while not pq.empty():
        top = pq.get()
        u = top.id
        visited[u] = True
        for neighbor in graph[u]:
            v = neighbor.id
            w = neighbor.dist
            if not visited[v] and dist[v] > w:
                dist[v] = w
                pq.put(Node(v, w))
    return sum(dist)
                
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    graph = [[] for i in range(n)]
    for _ in range(m):
        x, y, r = map(int, input().split())
        # edges.append(list(map(int, input().rstrip().split())))
        graph[x - 1].append(Node(y - 1, r))
        graph[y - 1].append(Node(x - 1, r))
    

    start = int(input()) - 1

    result = prims(n, graph, start)

    fptr.write(str(result) + '\n')

    fptr.close()


# Test with standard input:
import queue
INF = float('inf')
class Node:
  def __init__(self, id, dist):
    self.id = id
    self.dist = dist
  def __lt__(self, other):
    return self.dist <= other.dist
  
def prim(source):
  pq = queue.PriorityQueue()
  pq.put(Node(source, 0))
  dist[source] = 0
  while not pq.empty():
    top = pq.get()
    u = top.id
    visited[u] = True
    for neighbor in graph[u]:
      v = neighbor.id
      w = neighbor.dist
      if not visited[v] and dist[v] > w:
        dist[v] = w
        pq.put(Node(v, w))
        
n, m = map(int, input().split())
graph = [[] for i in range(n)]
dist = [INF for i in range(n)]
visited = [False for i in range(n)]

for i in range(m):
  x , y, r = map(int, input().split())
  graph[x - 1].append(Node(y - 1, r))
  graph[y - 1].append(Node(x - 1, r))
  
start = int(input())
prim(start)
# print(dist)
print(sum(dist))
