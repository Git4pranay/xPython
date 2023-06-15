# every element in dictionary should have 'key' as well as 'value'
dic={1:'chocolate',2:'laddu','cse':2}
print(dic)
dic[1]='mama'
print(dic)
#deletion
del dic[1]
print(dic)
#remove all
dic.clear()
print(dic)
# delete the dictionary
#keys and values
dic={2:'rel',3:'bel',7:'red'}
print(dic.keys())
print(list(dic.values()))
print(list(dic.items()))
print(dic.get(2))
print(dic.get('teo',88))
#update method
d2={'t':2,'lol':4}
dic.update(d2)
print(dic)
#removing a key
print(dic.pop('lol'))
print(dic)
#nested dictionarys
rec={'name':'bob','jobs':['developers','manager'],'home':{'state':'over','zip':12}}
print(rec)
print(rec['home']['zip'])
#dict as converting to dictonary
print(dict(name='bob',age=40))
#chomprehensions in dictionarys
d={k:v for (k,v) in zip(['a','b','c'],[1,2,3])}
print(d)
d={x:x**2 for x in [1,2,3,4]}
print(d)
d={x.upper():x+'!' for x in['spam','egg','ham']}
print(d)

