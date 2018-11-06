n = int(input())
tasks = list(map(int, input().split()))
mapping = [(tasks[i], i + 1) for i in range(len(tasks))]


s = sorted(mapping, key= lambda x: x[0])
count = 1

for i in range(len(s) - 1):
  if s[i][0] == s[i + 1][0]:
    count += 1
    
if count >= 3:
  print("YES")
  for k in range(len(s)):
    print(s[k][1], end=' ')

  c = 1
  for j in range(len(s) - 1):
    if s[j][0] == s[j + 1][0]:
      c += 1
      s[j], s[j + 1] = s[j + 1], s[j]
      print()
      for h in range(len(s)):
        print(s[h][1], end=' ')

      s[j], s[j + 1] = s[j + 1], s[j]
      
    if c == 3:
      break

if count < 3:
  print("NO")
