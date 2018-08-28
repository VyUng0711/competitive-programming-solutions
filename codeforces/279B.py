# http://codeforces.com/problemset/problem/279/B
def books(t,books):
  i = 0
  j = 0
  ds = [0] # if books[i] > t for each i -> ds == [] --> max([]) = runtime error
  sum = 0
  while i<len(books) and j<len(books):
    # sum=books[i]
    if sum + books[j] > t:
      sum-=books[i]
      i+=1
    else:
      sum+=books[j]
      j+=1
      ds.append(j-i)
    
  return (max(ds))
n, t=[int(x) for x in input().split()]
b = [int(x) for x in input().split()]
print (books(t,b))