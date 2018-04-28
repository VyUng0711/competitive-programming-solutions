def hard_work(str1,str2,str3,student_str):
  str1=delete_signs(str1)
  str2=delete_signs(str2)
  str3=delete_signs(str3)
  str1=str1.lower()
  str2=str2.lower()
  str3=str3.lower()
  accepted_strs=[str1+str2+str3, str1+str3+str2, str2+str1+str3,
                str2+str3+str1, str3+str1+str2, str3+str2+str1]
  student_str=delete_signs(student_str)
  student_str=student_str.lower()
  if student_str in accepted_strs:
    print('ACC')
  else:
    print('WA')

    
      
def delete_signs(str):
  str=str.replace('_','')
  str=str.replace(';','')
  str=str.replace('-','')
  return str

str1=input()
str2=input()
str3=input()
num=int(input())
for i in range(num):
  this_str=input()
  hard_work(str1,str2,str3,this_str)