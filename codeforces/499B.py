n,m=map(int,input().split())
dict={}
for i in range(m):
  key,value=input().split()
  dict[key]=value
text=[x for x in input().split()]

def lecture(dict,text):
  result=[]
  for language1 in text:
    write_down=language1
    language2=dict[language1]
    if len(language2) < len(language1):
      write_down=language2
    print (write_down,end=' ')
lecture(dict,text)