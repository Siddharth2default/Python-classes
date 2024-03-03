# *args and **kargs

def f1(a=1,b=1,c=1):
    return a+b+c
f1()
f1(1)
f1(1,2)
f1(1,2,3)
f1(a=10,b=20,c=30)
#*args
#def sum(a,b,c,d):
#    return a+b+c+d
#r = sum(1,2,3,4)
#print(r)
def args_sum(*args):
    for i in args:
        print(i)
args_sum(1)
args_sum(3)
args_sum(5)
args_sum(1,2,3,4)