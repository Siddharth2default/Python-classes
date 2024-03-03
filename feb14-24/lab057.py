#functions
#no return type and no arg
def hello():
    print("hello there")

hello()

def args(name,age): #no return type with argument
    print("hi",name,age)
args('sid',24)

def default(name="john"):
    print("bye",name)
default()
default("amit")
def returnargs(a,b):
    return a+b
comb = returnargs(7,3)
comb2 = returnargs("sid","cas")
print(comb,comb2)