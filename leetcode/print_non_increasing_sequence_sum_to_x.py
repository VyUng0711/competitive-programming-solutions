# https://www.geeksforgeeks.org/print-all-non-increasing-sequences-of-sum-equal-to-a-given-number/

# Method 1:

def non_increasing_sequence(x, chosen, sum_so_far):
    if sum_so_far == x:
        for a in chosen:
            print(a, end=' ')
        print()
    else:
        num = 1
        while num <= x - sum_so_far and (len(chosen) == 0 or num <= chosen[-1]):
            chosen.append(num)
            non_increasing_sequence(x, chosen, sum_so_far + num)
            chosen.pop()
            num += 1

non_increasing_sequence(5, [], 0)

# Method 2:

def print_a(a, n):
    for i in range(0, n):
        print(a[i], end = " ")
    print()

def non_increasing_sequence(x, chosen, sum_so_far, curr_indx):
    # print('non_increasing_sequence({}, {})'.format(x, sum_so_far))
    # print('chosen', chosen)
    if sum_so_far == x:
        print_a(chosen, curr_indx)
        return
    else:
        num = 1
        while num <= x - sum_so_far and (curr_indx == 0 or num <= chosen[curr_indx - 1]):
            chosen[curr_indx] = num
            non_increasing_sequence(x, chosen, sum_so_far + num, curr_indx + 1)
            num += 1

def generate(x):
    res = [None] * x
    non_increasing_sequence(x, res, 0, 0)

generate(5)

