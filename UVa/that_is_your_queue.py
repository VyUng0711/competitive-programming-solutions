import queue
def health_care(p,commands):
  patients=queue.Queue()
  
  if p >= len(commands):
    for i in range(1,len(commands)+1):
      patients.put(i)
  else:
    for i in range(1,p+1):
      patients.put(i)
  #result=[]
  for c in commands:
    if c[0] == "N":
      if p > len(commands):
        print (patients.queue[0])
        #result.append(patients.queue[0])
        patients.get()
      else:
        print (patients.queue[0])
        #result.append(patients.queue[0])
        patients.put(patients.queue[0])
        patients.get()
    else:
      second_queue=queue.Queue()
      c[1] = int(c[1])
      second_queue.put(c[1])
      for j in range(patients.qsize()):
        if patients.queue[j]!=c[1]:
          second_queue.put(patients.queue[j])
      patients=second_queue
  #return (result)


cont=True
index=1
while cont:
  p, c = [int(x) for x in input().split()]
  if p == 0 and c == 0:
    cont=False
    break 
  this_input=[]
  for i in range(c):
    x = input().split(' ')
    this_input.append(x)
  print ("Case %s:" % index)
  index+=1
  health_care(p,this_input)
  