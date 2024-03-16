a = int(input("Enter a number :"))

try :
    a = int(input("Enter a no. :"))
    print(a)
except ZeroDivisionError as e:
    print(e)
except ValueError as k:
    print(k)
except Exception as i:
    print(i)
else:
    print(f"The number:{a}")

finally:
    print("BYe")
