def far_distance(array,n):
    index_min=array.index(1)
    index_max=array.index(n)
    distances=[index_min,index_max,n-index_min-1,n-index_max-1]
    return max(distances)
n=int(input())
a=[int(x) for x in input().split()]
print (far_distance(a,n))