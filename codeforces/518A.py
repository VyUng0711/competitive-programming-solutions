def vitaly_and_strings(s,t):
  new_s=""
  table='abcdefghijklmnopqrstuvwxyz'
  add_letter=''
  for i in range(len(s)-1,-1,-1):
    if s[i]!='z':
      next_index=table.find(s[i])+1
      next_letter=table[next_index]
      stop_index=i
      add_letter = next_letter + add_letter
      break
    else:
      next_letter='a'
      add_letter = next_letter + add_letter
      
  new_s=s[0:stop_index]+add_letter
  if new_s == t: 
    return 'No such string'
  else:
    return new_s

s = input()
t = input()
print (vitaly_and_strings(s,t))