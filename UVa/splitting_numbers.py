# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3084
# ~ O(log 2 (n)()
while True:
  n = int(input())
  if n == 0:
    break
  a = 0
  b = 0
  c = 1 #index of bits that are 1
  i = 0 #all index
  while n > 0:
    # if current bit is 1
    if n & 1:
      # if c's not divided by 2:
      if c & 1:
        a |= (1 << i) #turn the bit at i on
      # if c's divided by 2
      else:
        b |= (1 << i) #turn the bit at i on
      c += 1

      # c ^= 1
    n = n >> 1
    i += 1
  print(a, b)
  
