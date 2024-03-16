def f1():
    print("f1 is printed")
def f2():
    f1()
    print("f2 is printed")

if __name__ == '__main__':
    f2()
