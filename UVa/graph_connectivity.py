# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=400

def findSet(u):
  if parents[u] != u:
    parents[u] = findSet(parents[u])
  return parents[u]


def unionSet(u, v):
  up = findSet(u)
  vp = findSet(v)
  if up == vp:
    return
  global count
  count -= 1
  if ranks[up] > ranks[vp]:
    parents[vp] = up
  elif ranks[up] < ranks[up]:
    parents[up] = vp
  else:
    parents[up] = vp
    ranks[vp] += 1

  
# print(ord("E") - ord("A") + 1)

num_test = int(input())
blank_line = input()
for t in range(num_test):
  
  n = ord(input()) - ord("A") + 1
  parents = [i for i in range(n)]
  ranks = [0 for i in range(n)]
  
  count = n
  while True:
    try:
      pair = input()
      if pair == "":
        break
      first = ord(pair[0]) - ord("A")
      second = ord(pair[1]) - ord("A")

      unionSet(first, second)
    except EOFError:
      break
  print(count)
  if t != num_test - 1:
    print()
