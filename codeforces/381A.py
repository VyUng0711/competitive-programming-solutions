# http://codeforces.com/problemset/problem/381/A
def sereja_and_dima(cards):
  s=0
  d=0
  turn=0
  i=0
  j=len(cards)-1
  while j>=i:
    if turn == 0:
      if cards[i]<cards[j]:
        s+=cards[j]
        j-=1
      else:
        s+=cards[i]
        i+=1
      turn = 1
    else:
      if cards[i]<cards[j]:
        d+=cards[j]
        j-=1
      else:
        d+=cards[i]
        i+=1
      turn = 0
  print (s, d)

n=int(input())
c=[int(x) for x in input().split()]
sereja_and_dima(c)