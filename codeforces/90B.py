#test1=[['c','b','a'],['b','c','d'],['c','b','c']]
test1=['cba','bcd','cbc']
def african_crossword(n,m,grid):
  encrypted = ""
  for i in range(n):
    for j in range(m):
      is_encrypted=True
      for k in range(n):
        if grid[i][j]==grid[k][j] and k!=i:
          is_encrypted=False
          break
      for h in range(m):
        if grid[i][j]==grid[i][h] and h!=j:
          is_encrypted=False
          break
      if is_encrypted==True:
        encrypted+=grid[i][j]
  return (encrypted)

#print (african_crossword(3,3,test1))

n,m=map(int,input().split())
grid=[]
for i in range(n):
  grid.append(input())

print (african_crossword(n,m,grid))