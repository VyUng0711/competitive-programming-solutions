# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=942


configs = [
  (0, 0, 0),
  (0, 0, 1),
  (0, 1, 0),
  (0, 1, 1),
  (1, 0, 0),
  (1, 0, 1),
  (1, 1, 0),
  (1, 1, 1)      
  ]
def recurse(indx):
  # global found
  # print('recurse({})'.format(indx))
  # print(temp)

  if indx == n:
    # If we already reach the last index:
    # we check if the last two in temp fit the first two in temp
    # because the first two were chosen arbitrarily in the beginning
    if temp[0] == temp[indx] and temp[1] == temp[indx + 1]:
      return True

    return False
  for i in range(8):
    if identity[i] == state[indx]:
      # If it's the first one, the neighbors don't matter so we can assign temp arbitrarily 
      if indx == 0:
        # temp[indx] = configs[i][0]
        # temp[indx + 1] = configs[i][1] -> state[indx + 1]
        # temp[indx + 2] = configs[i][2]

        temp[indx - 1] = configs[i][0]
        temp[indx] = configs[i][1]
        temp[indx + 1] = configs[i][2]
        if recurse(indx + 1):
          return True
      # If it's not the first one, then, we have to check if temp prefix fit any 
      # prefix configuration among the 8
      elif (temp[indx - 1] == configs[i][0] and temp[indx] == configs[i][1]):
        temp[indx + 1] = configs[i][2]
        if recurse(indx + 1):
          return True

  return False

      
while True:
  try:
    identity, n, state = input().split()
    identity = format(int(identity), '08b')[::-1]
    # print(state)
    # print(identity)
    n = int(n)
    temp = [0] * (n + 2)
    # found = False
    if recurse(0):
      print("REACHABLE")
    else:
      print("GARDEN OF EDEN")
  except EOFError:
    break


