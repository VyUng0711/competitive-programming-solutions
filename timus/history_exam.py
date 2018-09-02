# http://acm.timus.ru/problem.aspx?num=1196&space=1

from sys import stdin


lines = list(map(int, stdin.read().split()))
n = lines[0]
p = set()
for i in range(1, n + 1):
  p.add(lines[i])
#print(p)
m = lines[n + 1]
s = []
for j in range(n + 2, len(lines)):
  s.append(lines[j])
#print(s)
count = 0
for year in s:
  if year in p:
    count += 1
print(count)