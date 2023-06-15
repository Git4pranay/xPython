n=int(input())
letter=65
for i in range(n+1):
     for j in range(letter,letter+i):
       char=chr(j)
       print(char,end='')
     letter=letter+i
     print()
        