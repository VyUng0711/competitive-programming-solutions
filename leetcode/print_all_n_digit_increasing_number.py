# https://www.geeksforgeeks.org/print-all-n-digit-strictly-increasing-numbers/

# Using backtracking:
def print_all_n_digit_strictly_increasing_number(n, cur_num):
    # print('print_all_n_digit_strictly_increasing_number({}, {})'.format(n, cur_num))
    if len(cur_num) == n:
        for i, d in enumerate(cur_num):
            if i == len(cur_num) - 1:
                print(d, end = ' ')
            else:
                print(d, end = '')

            
    else:
        for i in range(10):
            if len(cur_num) == 0 or i > cur_num[-1]:
                cur_num.append(i)
                print_all_n_digit_strictly_increasing_number(n, cur_num)
                cur_num.pop()

print_all_n_digit_strictly_increasing_number(3, [])

