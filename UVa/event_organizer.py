# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1167
num_tests = int(input())
first_blank = input()
for t in range(num_tests):
  count_species = dict()
  sum_count = 0
  while True:
    tree = input()
    if tree == "":
      break
    count_species[tree] = count_species.get(tree, 0) + 1
    sum_count += 1
    
  for k in sorted(count_species):
    print(k, format(100*float(count_species[k]/ sum_count), '.4f'))
  if t != num_tests - 1:
    print()
