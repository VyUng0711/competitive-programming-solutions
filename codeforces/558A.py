def lala_land(l):
  #s=sorted(l,key=lambda x: x[0])
  count_negatives=0
  count_positives=0
  negatives=[]
  positives=[]
  for i in range(len(l)):
    if l[i][0]<0:
      count_negatives+=1
      negatives.append(l[i])
      
    else:
      count_positives+=1
      positives.append(l[i])
  sorted_neg=sorted(negatives,key=lambda x: x[0],reverse=True)
  sorted_pos=sorted(positives,key=lambda x: x[0])
  neg_values=[]
  pos_values=[]
  for i in range(len(sorted_neg)):
    neg_values.append(sorted_neg[i][1])
  for j in range(len(sorted_pos)):
    pos_values.append(sorted_pos[j][1])
    
  if count_positives==count_negatives:
    result=sum(neg_values)+sum(pos_values)
  elif count_positives > count_negatives:
    sum_pos=0
    for p in range(0,count_negatives+1):
      sum_pos+=pos_values[p]
    result=sum(neg_values)+sum_pos
  else:
    sum_neg=0
    for n in range(0,count_positives+1):
      sum_neg+=neg_values[n]
    result=sum(pos_values)+sum_neg
  print (result)
  

n=int(input())
l=[]
for i in range(n):
  l.append([int(x) for x in input().split()])
lala_land(l)