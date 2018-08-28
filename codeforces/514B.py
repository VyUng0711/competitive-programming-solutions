# http://codeforces.com/problemset/problem/514/B
n, x0, y0 = map(int, input().split())
points = []
for i in range(n):
  x, y = map(int, input().split())
  points.append((x, y))
slopes = set()
for i in range(n):
  if (points[i][0] - x0) == 0:
    slopes.add(None)
  else:
    s = (points[i][1] - y0) / (points[i][0] - x0)
    slopes.add(s)
print(len(slopes))