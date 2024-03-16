class MyCustom(Exception):

    def __init__(self,message):
        self.message = message
        super().__init__(message)

bal = 100
withdraw = int(input("amt to withdraw:"))

if withdraw > bal:
    raise MyCustom("Bal is low")
print("Total after withdrwal :",bal-withdraw)