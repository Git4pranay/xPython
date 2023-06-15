lo=[1,3,4,5,6,1,2,3,4,1,2,3]
ld=[]
for i in lo:
    if i not in ld:
        ld.append(i)
print(ld)