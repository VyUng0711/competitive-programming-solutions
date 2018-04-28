n,m,x,y=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]

def dress(a,b,x,y):
  l = []
  j = 0
  for i in range(n):
      while j < m and b[j] <= a[i] + y:
          if a[i] - x <= b[j]:
              j += 1
              l += [(i + 1, j)]
              break
          j += 1
  print (len(l))
  for i, j in l:
      print (i, j)
dress(a,b,x,y)