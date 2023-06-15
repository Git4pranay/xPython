import math
from itertools import permutations as com 
def adi(a):
    n=math.sqrt(a)
    if int(n)**2==a:
        return 1
    else:
        return 0
s=input().strip()
length=len(s);l=[];ans=[]
for i in range(0,10):
    l.append(str(i))
for i in com(l,length):
    if adi(int(''.join(i)))==1:
        ans.append(int(''.join(i)))
k=max(ans)
k1=str(k)
for i in range(length):
    print(s[i],k1[i])