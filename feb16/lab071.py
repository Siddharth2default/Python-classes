'''
list = [1,2,3,4,5]
d_list=[]
#double each element
for i in list :
    d_list.append(i*2)

print(d_list)
'''
def sq(num):
    return num**2
#print(sq(2))
numbers =[1,2,3,4,5]
#map - takes each item from list and execute a function on it and return the same no.
op = list(map(sq,numbers))
print(op)
