a = int(input("Enter num1:\n"))
b = int(input("Enter num2:"))

#exeception is event occurs during execution that distrupts normal execution of progrma
#handle exception
#try and except block
#try cod
#except - exceute the except code(if problem in try)

try :
    c = a / b
    print("Division is :",c)
except ZeroDivisionError as e:
    print('ZEro error>>',e)
except :
    print("ERROR Name")
print("------------------")