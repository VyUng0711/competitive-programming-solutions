# http://codeforces.com/problemset/problem/673/A
def watch_tv(minutes):
    i=0
    minutes += [200]
    while i <len(minutes) - 1:
        if i==0 and minutes[i]>15:
            count=15
            break
        if minutes[i+1]-minutes[i]>15:
            count=minutes[i]+15
            if minutes[i]>=75:
                count=90
            break
        i+=1
    print (count)
n=int(input())
m=[int(x) for x in input().split()]
watch_tv(m)