#palindrome checker using functions

#a = input("enter string to check if palindrome or not")
def pal(a):
    return a == a[::-1]
#value = input("val:")
print(pal("hih"))

x = "racecar"
w=""
for i in x:
    w=w+i
if x==w:
    print("palindrome is true")
else:
    print("not a palindrome")