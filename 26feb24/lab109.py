class BankAccount:
    def __init__(self):
        self.balance = 0
        self.__priv_var = 100
    def deposit(self,amount):
        self.balance +=amount
    def _withdraw(self,amount):
        self.balance-=amount
    def __show_balance(self):
        print("Your Current balance is :",self.balance)
    def if_auth(self,flag):
        if flag:
            self.__show_balance()
        else:
            print("Not allowed")
    def bank_manager(self,amount):
        self._withdraw(amount=amount)
        print("Withdrawall done of amount",amount)
jp_chase = BankAccount()
jp_chase.deposit(1000)
jp_chase.bank_manager(499)
jp_chase.if_auth(True)
