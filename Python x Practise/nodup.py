lo=list(map(int,input().split()))
listcount=[]
list_of_unique=[]
list_of_duplicates=[]
for i in lo:
    c=0
    for j in lo:
        if i==j:
            c=c+1
    listcount.append(c)

for i in range(len(listcount)):
    if listcount[i]==1:
        list_of_unique.append(lo[i])
    else:
        if lo[i] not in list_of_duplicates:
             list_of_duplicates.append(lo[i])



print(list_of_unique)
print(list_of_duplicates)