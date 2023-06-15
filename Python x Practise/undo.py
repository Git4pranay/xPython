s=input()
S=list(s)
# for i in range(S.count('^')):
a=len(S)
while(1):
 for i in range(a):
    if S[i]=='^':
        S.pop(i)
        S.pop(i-1)
        break
 print(S)
 a=len(S)
 if '^'  not in S:
    break
    
