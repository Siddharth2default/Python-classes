#lambda fn - one liner anonymous fn in python
'''
def double(salary):
    return salary*2
res=double(200000)
print(res)
'''
dres = lambda salary:salary*2
print(dres(10))
pow_of_two = lambda x:x**2
print(pow_of_two(2))
sum = lambda a,b:a+b
print(sum(6,7))
say = lambda name:print("your name",name)
say("sidd")