class XYZ:
    def f1(self):
        try:
            a = int(input("Enter num1:\n"))
        except Exception as e:
            print("Enter int value of a only!!!>",e)
        else:
            print(a)
        finally:
            print("ANyhow printed")

obj1 = XYZ()
obj1.f1()