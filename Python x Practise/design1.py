N=int(input())
s=str(N)
for i in range(len(s)):
    for j in range(int(s[i])):
         a=s[s.index(s[i])+1:]
         b=a.replace('0','')
         print(b,end='')

    print()