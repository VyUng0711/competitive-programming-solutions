# https://codeforces.com/problemset/problem/476/B


def get_finish_position(s):
  start = 0
  for i in s:
    if i == "+":
      start += 1
    elif i == "-":
      start -= 1
  return start

# print(get_finish_position("++-+-"))
def get_possibilities(s):
  res = []
  def recurse(cur, indx):
    if len(cur) == len(s):
      res.append(''.join(cur))
      return
    if s[indx] == "?":
      for choice in ["+", "-"]:
        cur.append(choice)
        recurse(cur, indx + 1)
        cur.pop()
    else:
      cur.append(s[indx])
      recurse(cur, indx + 1)
      cur.pop()
  recurse([], 0)
  return res


s1 = input()
s2 = input()
r1 = get_finish_position(s1)

p2 = get_possibilities(s2)
count = 0
for p in p2:
  if get_finish_position(p) == r1:
    count += 1
print(count/len(p2))



