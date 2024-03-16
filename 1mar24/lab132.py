#try except and finally
#multiple execption
try:
    num1 = int(input("N1:"))
    num2 = int(input("N2:"))
    c = num1/num2
except ZeroDivisionError as e:
    print("Z ERROR",e)
except ValueError as d:
    print("VAL error",d)
else:
    print(f"result :{c}")
finally :
    print("BYE1!")