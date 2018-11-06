class Node:
  def __init__(self):
    self.countWord = 0
    self.child = dict()

def addWord(root, s):
  tmp = root
  is_prefix = True
  for ch in s:
    if ch not in tmp.child:
      tmp.child[ch] = Node()
      is_prefix = False
    
    tmp = tmp.child[ch]
    if tmp.countWord == 1:
      return True

  tmp.countWord += 1
  return is_prefix

num_tests = int(input())
for t in range(num_tests):
  n = int(input())
  r = Node()
  final = True
  for i in range(n):
    this_number = input().strip()
    
    is_prefix = addWord(r, this_number)
    # print(is_prefix)
    if is_prefix:
      final = False

  if final:
    print("YES")
  else:
    print("NO")
