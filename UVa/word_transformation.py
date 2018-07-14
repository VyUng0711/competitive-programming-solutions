
import queue
from collections import defaultdict

def connected(a, b):
  if len(a) != len(b):
    return False
  count_diff = 0
  for i in range(len(a)):
    if a[i] != b[i]:
      if count_diff == 1:
        return False
      else:
        count_diff += 1
  return True

def bfs(s, t):
  for i in range(len(all_words)):
    distance[all_words[i]] = -1
  q = queue.Queue()
  q.put(s)
  distance[s] = 0
  while not q.empty():
    u = q.get()
    if u == t:
      return distance[u]
    for v in graph[u]:
      if distance[v] == -1:
        distance[v] = distance[u] + 1
        q.put(v)


num_tests = int(input())
blank = input()
for t in range(num_tests):
  all_words = []
  pairs = []
  while True:
    this_word = input()
    if this_word == "*":
      break
    else:
      all_words.append(this_word)
  while True:
    try:
        this_pair = input()
        if this_pair == "":
          break
        else:
          pairs.append(this_pair.strip().split())
    except EOFError:
      break
      
  graph = defaultdict(list)
  distance = {}
  for word_id in range(len(all_words)):
    for other_id in range(len(all_words)):
      if connected(all_words[word_id], all_words[other_id]):
        graph[all_words[word_id]].append(all_words[other_id])
  for p in pairs:
    print("{} {} {}".format(p[0], p[1], bfs(p[0], p[1])))
  if t != num_tests - 1:
    print()