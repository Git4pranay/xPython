s='a\nb\tc'
print(s)
s1='a\00b\00c'
print(s1)
print(len(s1))
b='\001\002\x03'
print(b)
e=r"c:\ny\tode"       # we use r means everthing is a string
print(e)
for c in myjob:
	print(c,end='*')



