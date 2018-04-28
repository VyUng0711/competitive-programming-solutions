def check_arrays(A,B,k,m):
    if A[k-1]<B[len(B)-m]:
        return "YES"
    else:
        return "NO"
nA, nB = [int(x) for x in input().split()]
k, m = [int(x) for x in input().split()]
aA = [int(x) for x in input().split()]
aB = [int(x) for x in input().split()]
print (check_arrays(aA,aB,k,m))