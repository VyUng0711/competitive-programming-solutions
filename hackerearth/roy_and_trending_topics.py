# https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/practice-problems/algorithm/roy-and-trending-topics-1/
import heapq

n = int(input())
topics_new = {}
changes = []
for i in range(n):
  topic_id, old_score, p, l, c, s = map(int, input().split())
  new_score = p * 50 + l * 5 + c * 10 + s * 20
  change = new_score - old_score
  topics_new[-topic_id] = new_score
  changes.append((-change, -topic_id))
#print (changes)
#print (topics)

heapq.heapify(changes)
top_scores = []
for i in range(5):
  top_scores.append(heapq.heappop(changes))

for score, i in top_scores:
  print (-i, topics_new[i])

# print (top_scores)