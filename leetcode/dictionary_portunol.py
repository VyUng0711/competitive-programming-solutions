#https://icpcarchive.ecs.baylor.edu/index.php?option=onlinejudge&page=show_problem&problem=3803
import queue

class Node:
  def __init__(self):
    self.countWord = 0
    self.child = dict()
    self.level = 0
    
def add_word(root, word):
  tmp = root
  for ch in word:
    if ch not in tmp.child:
      tmp.child[ch] = Node()
      tmp.child[ch].level = tmp.level + 1
    tmp = tmp.child[ch]
  tmp.countWord += 1

def get_result(root_p, count_start_suffix, total_suffix):
  q = queue.Queue()
  q.put(root_p)
  out = 0
  while not q.empty():
    top = q.get()
    for k, v in top.child.items():
      q.put(v)
      this_count = total_suffix
      for l in v.child.keys():
        if l in count_start_suffix:
          this_count -= count_start_suffix[l]
      out += this_count
  return out
      
def get_suffix_start_frequency(root_s):
  q = queue.Queue()
  q.put(root_s)
  count_start_suffix = {}
  total_suffix = 0
  while not q.empty():
    top = q.get()
    total_suffix += 1
    for k, v in top.child.items():
      # print(k, v.level)
      if v.level > 1:
         count_start_suffix[k] = count_start_suffix.get(k, 0) + 1

      q.put(v)
  return count_start_suffix, total_suffix - 1

def get_all_suffix(root):
  reversed_suffix = get_all_prefix(root)
  return [x[::-1] for x in reversed_suffix.keys()]

# t * (p * len(prefix) + s * len(suffix) + sum(len(prefix))) + len(prefix) * p * 26)
while True:
  p, s = map(int, input().split())
  if p == 0 and s == 0:
    break

  root_p = Node()
  root_s = Node()

  for i in range(p):
    add_word(root_p, input())
  for j in range(s):
    add_word(root_s, input()[::-1])
  count_start_suffix, total_suffix = get_suffix_start_frequency(root_s)
  out = get_result(root_p, count_start_suffix, total_suffix)
  print(out)
  
