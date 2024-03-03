#list - mutable
a=[1,2,3.4]
a[0]=21
print(a)
t =(2,3,25)
#t[0]=21 - tuple cant be assigned - type error
#tuple - immutable
print(t)
new_tup = tuple(a)
print(new_tup)
