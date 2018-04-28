def night_at_the_musium(s):
  current='a'
  cur_index=0
  table='abcdefghijklmnopqrstuvwxyz'
  total=0
  for i in s:
    pos=table.find(i)
    if pos > cur_index:
      if pos - cur_index > len(table)/2:
        distance=cur_index-(pos-len(table))
      else:
        distance=pos-cur_index
    else:
      if cur_index-pos > len(table)/2:
        distance= pos-(cur_index-len(table))
      else:
        distance=cur_index-pos
    #print(distance)
    total+=distance
    cur_index=pos
  return total
x = input()
print(night_at_the_musium(x))   