def check_jacket(n,l):
    if n==1:
        if l[0]==0:
            return "NO"
        else:
            return "YES"
    check=len(l)-sum(l)
    if check!=1:
        return "NO"
    return "YES"
n = int(input())
a = [int(x) for x in input().split()]
print (check_jacket(n,a))