n,m=[int(x) for x in input().split()]
s=[int(x) for x in input().split()]
#print (choose_book(s))

def fast_choose_book(list_of_books,m):
    counts={}
    num_options=0
    for book in list_of_books:
        if book in counts:
            counts[book]+=1
        else:
            counts[book]=1
    for i in range(1, m+1):
        for j in range(i+1,m+1):
            num_options+=counts[i]*counts[j]     
    return num_options
print (fast_choose_book(s,m))