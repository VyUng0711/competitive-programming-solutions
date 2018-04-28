def balls_game(balls,x):
  counts=[]
  for b in range(len(balls)):
    copy=balls.copy()
    copy.insert(b,x)
    this_count=0
    while True: 
      i = 0
      j = 0
      while i < len(copy):
        j = i
        while j < len(copy) and copy[i] == copy[j]:
          j += 1
        if j - i > 2:
          break
        i = j
      if i == len(copy): # cannot find any
        break
      del copy[i:j]
      this_count+=(j-i)
    counts.append(this_count)
  return max(max(counts)-1,0) 

n,k,x=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
print (balls_game(b,x))