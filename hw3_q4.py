class BankAcount():
    def __init__(self,ownername:str,money:int,acountlimit:int) -> None:
        assert money >= acountlimit , 'money could not be lower than acountlimit'
        self.owner = ownername
        self.money = money
        self.acountlimit = acountlimit

    def deposit(self,amount:int):
        assert amount > 0, "you cant deposit negetive amount"
        self.money += amount
        print('you deposit successfully')

    def withdraw(self,amount):
        assert amount > 0, "you cant deposit negetive amount"
        if (self.money - amount) <= self.acountlimit:
            print('you can not withdraw this amount')
        else:
            self.money -= amount

    def transfer(self,amount,bankacount):
        assert amount > 0, "you cant deposit negetive amount"
        if self.money - bankacount <= self.acountlimit:
            print('you can not transfer this amount')
        else:
            bankacount.money += amount
            self.money -= amount
            print('money transfered successfully')

    def canwithdraw(self,amount:int)->bool:
        if self.money - amount < self.acountlimit:
            return False
        else:
            return True


a = BankAcount('rasool', 100, 100)
print(a.deposit(200))