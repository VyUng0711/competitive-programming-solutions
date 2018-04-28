def min_width(l,height):
    min_width=0
    for i in range(len(l)):
        if l[i] <= height:
            min_width+=1
        else:
            min_width+=2
    return min_width
n, h = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
print (min_width(a,h))