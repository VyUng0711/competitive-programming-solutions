n = int(input())
numbers = list(map(int, input().split()))

count = 0

power_of_two = {2**x for x in range(32)}

count_number = dict()

# for number in numbers:
#   count_number[number] = count_number.get(number, 0) + 1

  
# a[j] + a[i] = 2 ^ x
# => a[i] = 2 ^ x - a[j]
  
for number in numbers:
  for s in power_of_two:
    this_freq = count_number.get(s - number, 0)
    count += this_freq
  count_number[number] = count_number.get(number, 0) + 1
  
print(count)
