# https://www.geeksforgeeks.org/print-a-pattern-without-using-any-loop/

def print_pattern(n, cur, go_back):
    print(cur)
    if go_back and n == cur:
        return
    if not go_back:
        if cur - 5 > 0:
            print_pattern(n, cur - 5, False)
        else:
            print_pattern(n, cur - 5, True)
    else:
        print_pattern(n, cur + 5, True)

    

# Other method:
def print_pattern(n):
    print("print_pattern({})".format(n))
    if n == 0 or n < 0:
        print(n)
        return
    # First print decreasing order
    print(n)
    print_pattern(n - 5)
    # Then print increasing order
    print(n)


