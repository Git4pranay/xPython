m,n=map(int,input().split())
def border(m,c):
    k=0
    r=c
    l1=[m[k][i] for i in range(k,c)]
    l2=[m[i][c-1] for i in range(k+1,r-k)]
    l3=[m[r-1][i] for i in range(k+1,c-1-k)][::-1]
    l4=[m[i][k] for i in range(k,r)][::-1]
    for i in l1+l2+l3+l4:
        if i%2!=0:
            return 0
    return 1
count=0
l=[ list(map(int,input().split())) for i in range(m)]
p=0
for j in range(m-n+1):
 sub=[]
 for i in l:
    sub.append(i[j:j+n])
 subm=[ border(sub[i:i+n],n) for i in range(len(sub)-n+1) ]
 if 1 in subm:
    count+=1
 print(subm)
print(count)