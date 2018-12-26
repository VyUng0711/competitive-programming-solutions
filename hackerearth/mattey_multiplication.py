# https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/mattey-multiplication-6/


t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    bin_m = format(m, '#010b')
    start = False
    for i in range(2, len(bin_m)):
        if bin_m[i] == '1':
            if start == True:
                print(" + ", end='')
            start = True
            print("({}<<{})".format(n, len(bin_m) - 1 - i), end='')
    print()

  
