# https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/distinct-count/
class Node:
  def __init__(self, x):
    self.key = x
    self.left = None
    self.right = None
    
# a = Node(2)
# print(a.key)

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

def size(root):
  if root == None:
    return 0
  return size(root.left) + 1 + size(root.right)

num_tests = int(input())
for t in range(num_tests):
  n, x = map(int, input().split())
  a = list(map(int, input().split()))
  tree = createTree(a, n)
  count = size(tree)
  if count == x:
    print("Good")
  elif count > x:
    print("Average")
  else:
    print("Bad")

    
    
