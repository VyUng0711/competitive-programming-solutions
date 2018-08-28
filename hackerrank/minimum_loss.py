# https://www.hackerrank.com/contests/womens-codesprint-2/challenges/minimum-loss

n = int(input())
prices = list(map(int, input().split()))

# Without building binary tree

def minimumLoss(price):
  map_price_to_order = {price[i]: i for i in range(n)}
  # print(map_price_to_order)
  sorted_price = sorted(price, reverse = True)

  min_loss = float('inf')
  for i in range(n - 1):
    if map_price_to_order[sorted_price[i]] < map_price_to_order[sorted_price[i + 1]]:
      if sorted_price[i] - sorted_price[i + 1] < min_loss:
        min_loss = sorted_price[i] - sorted_price[i + 1]
  return min_loss

print(minimumLoss(prices))



# With building binary tree

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

def find_higher(root, x):
  if root == None:
    return float('inf')
  if root.key < x:
    return find_higher(root.right, x)
  return min(root.key, find_higher(root.left, x))

def minimumLossBinary(price):
  start = Node(price[0])
  root = start
  higher_so_far = price[0]
  loss_so_far = float('inf')
  for i in range(1, n):
    loss_so_far = min(loss_so_far, find_higher(root, price[i]) - price[i])
    root = insertNode(root, price[i])
  return loss_so_far

print(minimumLossBinary(prices))
