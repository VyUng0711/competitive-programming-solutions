class Node:
  def __init__(self, weight = 0):
    self.countWord = 0
    self.child = dict() 
    self.weight = weight 

# abc 10
# abcd 20
# abce 10
# abcef 30

# ab -> 
def add_word(root, s, w):
  tmp = root
  for ch in s:
    if ch not in tmp.child:
      tmp.child[ch] = Node(w)
    tmp = tmp.child[ch]
    tmp.weight = max(w, tmp.weight)

#       this_w = max(w, tmp.weight)
#       tmp.child[ch] = Node(this_w)
#     else:
#       tmp.child[ch].weight = max(w, tmp.child[ch].weight)
    
#     tmp = tmp.child[ch]
  
  tmp.countWord += 1
    
def find_word(root, s):
  tmp = root
  for ch in s:
    if ch not in tmp.child:
      return -1
    tmp = tmp.child[ch]
  
  
#   while len(tmp.child) > 0:
#     max_weight = -1
#     max_next = None
#     for k, v in tmp.child.items():
#       if max_weight < v.weight:
#         max_weight = v.weight
#         max_next = k
#     # print(max_weight)
#     tmp = tmp.child[max_next]
  return tmp.weight
    
    
n, q = map(int, input().split())
root = Node()
for i in range(n):
  word, weight = input().split()
  weight = int(weight)
  add_word(root, word, weight)
  # print(find_word(root, word))
  # print(root)
for j in range(q):
  target = input()
  print(find_word(root, target))
