l=[int(input()) for i in range(10)]
c=1
print(1)
for i in range(1,10):
    if l[i]<=max(l[0:i]): print(c)
    else: c=i+2;print(i+1)
        
    
