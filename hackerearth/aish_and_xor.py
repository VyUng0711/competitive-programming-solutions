# https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/aish-and-xor-2/

# Better complexity:

n = int(input())
a = list(map(int, input().split()))
count_ones = []
count_ones.append(0)
so_far = 0
for i in range(n):
  if a[i] == 1:
    so_far += 1
  count_ones.append(so_far)

# print(count_ones)

q = int(input())
for i in range(q):
  l, r = map(int, input().split())
  length = r - l + 1
  # print('length', length)
  num_ones = count_ones[r] - count_ones[l - 1]
  # print('num ones', num_ones)
  num_zeroes = length - num_ones
  # print('num zeroes', num_zeroes)
  if num_ones & 1 == 0:
    bit = 0
  else:
    bit = 1
  print(bit, num_zeroes) 


# Brute force
n = int(input())
a = list(map(int, input().split()))
q = int(input())
for i in range(q):
  l, r = map(int, input().split())
  target = a[l - 1: r]
  s = target[0]
  if s == 0:
    count = 1
  else:
    count = 0
  for b in target[1:]:
    if b == 0:
      count += 1
    s = s ^ b
  print(s, count)


