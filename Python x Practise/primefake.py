y=int(input())
if y==0:
  print("zero is not")
elif y<0:
 print("no negative")
else:
 x=1
 while y>x:
  if y%(x+1)==0 :
   print(y,"not prime")
   break
  x=x+1
 else:
  if(y!=2):
   print(y,"is prime")
   

 