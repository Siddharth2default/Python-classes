#prob - find max between 3 no's
num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))
num3 = int(input("Enter num3"))
#max_num = max(num1,num2,num3)
#print(max_num)
if((num1>num2)and(num1>num3)):
    print(f"{num1}is max")
elif num2>num1 and num2>num3:
    print(f"{num2} is largest")
else:
    print("max is",num3)