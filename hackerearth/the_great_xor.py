# https://www.hackerrank.com/challenges/the-great-xor/problem

def theGreatXor(x):
  count = 0
  bin_x = bin(x)[2:]
  # O(len(bin_x)) = O(log(x))
  for i in range(len(bin_x) - 1, -1, -1):
    if bin_x[i] == '0':
      count += 2 ** (len(bin_x) - i - 1)
  return count

  # for a in range(1, x):
  #   if a ^ x > x:
  #     count += 1
  # return count

q = int(input())
for i in range(q):
  x = int(input())
  print(theGreatXor(x))

0 < a < x
x = 0110001001
a = 00001xxxxx -> 2 ^ 5
^ = 01101yyyyy


x = 10d =
1010b
01xx
11yy 2 ^ 2

0001
0001 2 ^ 0




