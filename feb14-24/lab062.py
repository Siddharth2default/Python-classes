#factorial
#reverse string
#palindrome
def rev_string(str):
    rev_str=""
    for c in str:
        rev_str=c+rev_str
    return rev_str
og = input("enter name")
og = og.lower()
name = rev_string(og)
print(name)

if og == name:
    print("palindrome")
else:
    print("not a palindrome")
