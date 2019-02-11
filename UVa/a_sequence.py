# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1871

# 


def check_a_sequence(s):
  all_sum_so_far = set()
  all_sum_so_far.add(s[0])
  is_asequence = True
  if s[0] < 1:
    is_asequence = False
  for i in range(1, len(s)):
    if s[i] in all_sum_so_far or s[i] < s[i - 1]:
      is_asequence = False
      break
    new_sums = set()
    # all_sum_so_far = {1, 3, 4}
    # s[i] = 6
    for j in all_sum_so_far:
      new_sums.add(j + s[i]) # 10 -> {7, 1, 9, 3, 10}
      # new_sums.add(j) # 3 -> {7, 1, 9, 3, 10, 4}
    new_sums.add(s[i])
    
    all_sum_so_far = all_sum_so_far.union(new_sums)
    # for k in s[:i]:
    #   new_sums.add(k + s[i])
    # print(new_sums)
    
    # print(all_sum_so_far)
  if is_asequence:
    print("This is an A-sequence.")
  else:
    print("This is not an A-sequence.")
  # print(all_sum_so_far)
  return

t = 1
while True:
  try:
    line = list(map(int, input().split()))
    s = line[1:]
    # print(s)
    print("Case #{}: ".format(t) + " ".join([str(x) for x in s]))
    check_a_sequence(s)
    t += 1
  except EOFError:
    break

######### Other solution

def check_a_sequence(s):
 # sum_s = sum(s)
  aseq = True
  dp = [0] * (1001)
  dp[0] = 1
  for i in range(len(s)):
    for j in range(1000, -1, -1):
      if dp[j] and j + s[i] <= 1000:
        dp[j + s[i]] += 1
  if s[0] < 1:
    aseq = False
  for i in range(1, len(s)):
    if s[i] <= s[i - 1]:
      aseq = False
  for i in range(len(s)):
    if dp[s[i]] > 1:
      aseq = False
  #print(dp)
  if aseq:
    print("This is not an A-sequence.")
  else:
    print("This is an A-sequence.")


