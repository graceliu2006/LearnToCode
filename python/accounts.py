import datetime, pytz


class Account:
    """ simple account class with balance """
    
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        # self.init_bal=balance
        self._transaction_list = []
        self._transaction_list.append((Account._current_time(), balance))
        print("Account created for " + self._name)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))

        else:
            print("the amount must be greater than zero and less than your account balance")
        self.show_balance()


    def show_balance(self):
        print("Balance is ${}".format(self._balance))

    def show_transactions(self):
        amount = self._transaction_list[0][1]
        print("   Account created with balance of ${}".format(amount))
        # first_transaction = True
        for date, amount in self._transaction_list:
            # if first_transaction == True:
            #     tran_type="New Account"
            #     print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))
            #     first_transaction=False
            # else:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == "__main__":
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
 
    tim.withdraw(500)

    tim.withdraw(2000)

    tim.show_transactions()

    steph = Account("Steph", 800)
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()



