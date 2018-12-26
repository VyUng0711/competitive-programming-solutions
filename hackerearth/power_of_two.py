# https://www.hackerearth.com/challenge/competitive/thoughtworks-singapore-codeathon-2015/algorithm/power-of-two-4/description/
# Using bit operation:
num_test = int(input())
for t in range(num_test):
  n = int(input())
  nums = list(map(int, input().split()))
  found = False
  for i in range(31):
    start = 2 ** 32 - 1
    for j in range(len(nums)):
      if (nums[j] >> i) & 1 == 1:
          start = start & nums[j]
    if start & (start - 1) == 0:
      print("YES")
      found = True
      break
  if not found:
    print("NO")


# Operate on string:
num_test = int(input())
for t in range(num_test):
  n = int(input())
  a = list(map(int, input().split()))
  bin_a = []
  max_length = 0
  for num in a:
    bin_num = bin(num)[2:]
    bin_a.append(list(bin_num))
    max_length = max(max_length, len(bin_num))
  
  # print(bin_a)
  for i in range(len(bin_a)):
    bin_a[i] = ['0'] * (max_length - len(bin_a[i])) + bin_a[i]
  
  # print(bin_a)
  
  found = False
  for i in range(max_length):
    ao = None
    for j in range(len(bin_a)):
      if not ao and bin_a[j][i] == '1':
        ao = a[j]
        continue
      elif bin_a[j][i] == '1':
        ao = ao & a[j]

    if ao:
      if ao & (ao - 1) == 0:
        print("YES")
        found = True
        break
  if not found:
    print("NO") 




