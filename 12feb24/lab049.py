#factorial
#n = 5
#5*4*3*2*1
number = int(input("Factorial of number:"))
if number <0 :
    print("Factorial is not possible")
elif number==0:
    print("1")
else:
    fact = 1
    for i in range(1,number+1):
        fact*=i
    print(fact)