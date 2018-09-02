# http://codeforces.com/problemset/problem/518/B
s = input()
t = input()
dict_t = dict()
for letter in t:
  dict_t[letter] = dict_t.get(letter, 0) + 1
  
yay = 0
whoops = 0
remaining = []
for letter in s:
  if letter in dict_t and dict_t[letter] > 0:
    yay += 1
    dict_t[letter] -= 1
  else:
    remaining.append(letter)
for letter in remaining:
  if letter.isupper() and letter.lower() in dict_t and dict_t[letter.lower()] > 0:
    whoops += 1
    dict_t[letter.lower()] -= 1
  if letter.islower() and letter.upper() in dict_t and dict_t[letter.upper()] > 0:
    whoops += 1
    dict_t[letter.upper()] -= 1
      
print(yay, whoops)
