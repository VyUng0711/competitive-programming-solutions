# http://codeforces.com/problemset/problem/546/A
#Complexity: O(1)
def soldier_and_bananas(k, n, w):
  cost = k*((1+w)*w//2)
  borrow = max(cost - n, 0)
  return borrow
k, n, w = map(int, input().split())
print(soldier_and_bananas(k, n, w))

#Complexity: O(n)
def soldier_and_bananas_2(k, n, w):
  cost = 0
  for i in range(1, w + 1):
    cost += i * k
  borrow = max(cost - n, 0)
  return borrow
k, n, w = map(int, input().split())
print(soldier_and_bananas(k, n, w))