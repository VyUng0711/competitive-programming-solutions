# https://icpcarchive.ecs.baylor.edu/index.php?option=onlinejudge&page=show_problem&problem=5215

def recurse(indx, value, equal):
  global found
  if found:
    return
  res[indx] = value

  if indx == len(num) - 1:
    found = True
    return

  if equal:
    if count[num[indx + 1]] > 0:
      count[num[indx + 1]] -= 1
      recurse(indx + 1, num[indx + 1], True)
      count[num[indx + 1]] += 1

    for i in range(num[indx + 1] - 1, -1, -1):
      if count[i] > 0:
        count[i] -= 1
        recurse(indx + 1, i, False)
        count[i] += 1

  else:
    for i in range(9, -1, -1):
      if count[i] > 0:
        count[i] -= 1
        recurse(indx + 1, i, False)
        count[i] += 1
    


while True:
  try:
    a = input()
    num = [int(x) for x in a]
    res = [None] * 20
    count = [2] * 11
    found = False

    count[num[0]] -= 1
    recurse(0, num[0], True)
    count[num[0]] += 1

    if not found:
      for i in range(num[0] - 1, -1, -1):
        count[i] -= 1
        recurse(0, i, False)
        count[i] += 1
    
    # print(res)
    final = 0
    multiplier = 1
    for i in range(len(num) - 1, -1, -1):
      final += multiplier * res[i]
      multiplier *= 10
    print(final)
  except EOFError:
    break




