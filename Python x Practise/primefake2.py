y=int(input())
if y==0:
  print("zero is not")
elif y<0:
 print("no negative")
else:
 x=y//2
 while x>1:
  if y%x==0:
   print(y,"not prime")
   break
  x=x-1
 else:
  print(y,"is prime")
   

 