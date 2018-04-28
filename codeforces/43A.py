def football(num_lines,goals):
  scores={}
  for i in goals:
    if i in scores:
      scores[i]+=1
    else:
      scores[i]=1
  max_value=max(scores.values())
  for k,v in scores.items():
    if v==max_value:
      max_key=k
  return (max_key)
num_lines=int(input())
goals=[]
for i in range(num_lines):
  goals.append(input())
print(football(num_lines,goals))