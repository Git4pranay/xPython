n=int(input())
a=1
for i in range(n+1):
    for j in range(a,a+i):
        print(j,end=' ')
    a=i+a
    print()