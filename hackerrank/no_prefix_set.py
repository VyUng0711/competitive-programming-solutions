# https://www.hackerrank.com/challenges/no-prefix-set/problem
class Node:
  def __init__(self):
    self.countWord = 0
    self.child = dict()

def add_word(root, word):
  tmp = root
  is_prefix = True
  for ch in word:
    if ch not in tmp.child:
      tmp.child[ch] = Node()
      is_prefix = False
    tmp = tmp.child[ch]
    if tmp.countWord == 1:
      return True
  tmp.countWord += 1
  return is_prefix

n = int(input())
root = Node()
result = True
first = None
for i in range(n):
  word = input()
  if add_word(root, word):
    first = word
    result = False
    break
if result:
  print("GOOD SET")
else:
  print("BAD SET")
  print(first)
