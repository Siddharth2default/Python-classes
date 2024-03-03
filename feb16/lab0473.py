#filter
#filter the items from list based on logic
#return less no of items
#number =[1,2,3,4,5,6]
#even = filter(lambda x:x%2==0,number)
#print(list(even))
number = [1,2,3,4,5,6]
def even(num):
    return num%2==0

even_lambda = lambda num:num%2==0
print(list(filter(even_lambda,number)))