# import string
def camelcase(s):
  count = 1
  for i in s:
    # if i not in string.ascii_lowercase:
   	if i.isupper():
      count += 1
  return count

print(camelcase(input()))