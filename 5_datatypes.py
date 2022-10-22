a,b,c,d=("1 2 3 4").split()
print("\nList datatype operations:\n")
print("adding",a,b,c,d,"to the list")
l=[]
l.append(a)
l.append(b)
l.append(c)
l.append(d)
print("length of list",l,"is",len(l))
print("popping",l.pop(),"from the list")
print("after popping the list is",l,"and length is",len(l))
print("removing",a,"from the list")
l.remove(a)
print("after removeing the set is",l,"and length is",len(l))

print("\nSet datatype operations:\n")
print("adding",a,b,c,d,"to the set")
s=set()
s.add(a)
s.add(b)
s.add(c)
s.add(d)
print("length of the set",s,"is",len(s))
print("removing",a,"from the set")
s.remove(a)
print("after removeing the set is",s,"and length is",len(s))

print("\nTuple datatype operations:\n")
print("adding set",s,"and list",l,"to the tuple")
t=(s,l)
print("after adding tuple is",t)
print("Tupple are immputable we cannot perform any opetaions on tuple")

print("\nDictionary datatype operations:\n")
d={}
print("adding key value pair to the dictionary")
d[1]='ada'
d[2]='python'
d[3]='html'
d[4]='javascript'
print("attre adding the dictionary is",d,"and length is",len(d))
print("removing",d[1],"from dictionery")
del d[1]
print("attre detelint the dictionary is",d,"and length is",len(d))


