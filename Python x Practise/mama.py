a=input()
b=input()
L=[]
L1=[]
lf=[]
for i in range(len(a)):
    l=a[0:i+1]+b+a[i+1:]
    L.append(l)
for i in L:
  print(i)