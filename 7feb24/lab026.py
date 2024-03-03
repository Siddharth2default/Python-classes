#assignment operator
name = "Pramod"
#it will store the value of variable literal to identifier
#unary operator
age = 95
bal = -887
print(age,bal)
is_married = True
#not - unary used for booleans mainly
print(not is_married)
#is operatot - identity operator
a = 5
b = False
c = 5
print(a is b)
print(a is c) #True
my_list =[1,2,3]
my_list2 = [1,2,3]
print(my_list is my_list2) #ordered
my_set = {4,5,6}
my_set2 = {4,5,6} # unordered (even is set2 is{6,5,4} has same set of contents it setill reflect false as order donot matter here
print(my_set is my_set2)