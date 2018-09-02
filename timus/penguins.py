# http://acm.timus.ru/problem.aspx?num=1585
# Use dictionary
n = int(input())
count_dict = {}
for i in range(n):
  p = input()
  count_dict[p] = count_dict.get(p, 0) + 1
sorted_count = sorted(count_dict.items(), key=lambda x: x[1])
print(sorted_count[-1][0])

# Use binary search tree
class Node:
  def __init__(self, key, value):
    self.key = key
    self.count = value
    self.left = None
    self.right = None

def insertNode(root, key):
  if root == None:
    return Node(key, 1)
  if root.key == key:
    root.count += 1
    return root
  else:
    if key < root.key:
      root.left = insertNode(root.left, key)
    elif key > root.key:
      root.right = insertNode(root.right, key)
    return root

def get_max(root, max_node_so_far = Node(None, float('-inf'))):
  if root == None:
    return max_node_so_far
  if root.count > max_node_so_far.count:
    max_node_so_far = root
  max_node_so_far = get_max(root.left, max_node_so_far)
  max_node_so_far = get_max(root.right, max_node_so_far)
  return max_node_so_far


def searchNode(root, key):
"""
This function is used to search for a key.
"""
  if root == None:
    return 1
  if root.key == key:
    return root.count
  if root.key < key:
    return searchNode(root.right, key)
  return searchNode(root.left, key)

def modifyNode(root, key, new_value):
"""
This function is used to modify the value given a key.
"""
  if root == None:
    return
  if root.key == key:
    root.value = new_value
    return
  if root.key < key:
    modifyNode(root.right, key, new_value)
    return
  modifyNode(root.left, key, new_value)


n = int(input())
root = None
for i in range(n):
  p = input()
  root = insertNode(root, p)
print(get_max(root).key)
