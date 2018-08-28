# https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/monk-and-his-friends/description/
class Node:
  def __init__(self, x):
    self.key = x
    self.left = None
    self.right = None

def insertNode(root, x):
  if root == None:
    return Node(x)
  if x < root.key:
    root.left = insertNode(root.left, x)
  elif x > root.key:
    root.right = insertNode(root.right, x)
  return root

def createTree(a, n):
  root = None
  for i in range(n):
    root = insertNode(root, a[i])
  return root

def searchNode(root, x):
  if root == None or root.key == x:
    return root
  if root.key < x:
    return searchNode(root.right, x)
  return searchNode(root.left, x)

# def size(root):
#   if root == None:
#     return 0
#   return size(root.left) + 1 + size(root.right)

num_tests = int(input())
for t in range(num_tests):
  n, m = map(int, input().split())
  students = list(map(int, input().split()))
  in_class = students[:n]
  coming = students[n:]
  tree = createTree(in_class, n)
  for c in coming:
    if searchNode(tree, c):
      print("YES")
    else:
      print("NO")
    insertNode(tree, c)
  