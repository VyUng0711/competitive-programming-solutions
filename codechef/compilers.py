def compilers(brackets):
  wrong_open = []
  wrong_close = []
  res = 0
  for i in range(len(brackets)):
    if brackets[i] == "<":
      wrong_open.append(i)
    else:
      if len(wrong_open) > 0:
        wrong_open.pop()
        if not wrong_open:
          res = i + 1
        # (()
      else:
        break
  return res

num_tests = int(input())
for t in range(num_tests):
  b = input()
  print(compilers(b))