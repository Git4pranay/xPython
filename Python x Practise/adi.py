n=int(input())
l=[[1]]
for i in range(2,n+1):
    k=[]
    for j in range(1,i+1):
        k.append(j)
    a=l[-1]+k
    l.append(a)
for i in l:
    print(*i)