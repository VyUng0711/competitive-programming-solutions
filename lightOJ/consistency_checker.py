class Node:
  def __init__(self):
    self.countWord = 0
    self.child = dict()
    
  
def add_word(root, s):
  tmp = root
  is_prefix = True
  for ch in s:
    if ch not in tmp.child:
      tmp.child[ch] = Node()
      tmp = tmp.child[ch]
      is_prefix = False
    else:
      # Check if there is already a word that is the prefix of the word we
      # want to add
      if tmp.child[ch].countWord == 1 and is_prefix:
        return True
      else:
        tmp = tmp.child[ch]
  # Check if the word we want to add is the prefix of an existing word.
#   if len(tmp.child) > 0 and is_prefix:
#     return True
  
  tmp.countWord += 1
  return is_prefix

    
num_test = int(input())
for t in range(num_test):
  n = int(input())
  root = Node()
  result = True
  words = []
  for i in range(n):
    words.append(input())
    
  for word in words:
    is_prefix = add_word(root, word)
    if is_prefix:
      result = False
      break

  if result == False:
    print("Case {}: NO".format(t + 1))
  else:
    print("Case {}: YES".format(t + 1))
