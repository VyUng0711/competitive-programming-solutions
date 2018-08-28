# http://codeforces.com/problemset/problem/242/B
def big_segment(left,right):
    low = min(left)
    up = max(right)
    for i in range(len(left)):
        if left[i]==low and right[i]==up:
            return i+1
    return -1
            
n=int(input())
l=[]
r=[]
for i in range(n):
    s=[int(x) for x in input().split()]
    l.append(s[0])
    r.append(s[1])
print (big_segment(l,r))