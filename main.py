# Banking system
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("The details are: ")
        print("Name: ", self.name)
        print("age: ", self.age)
        print("gender: ", self.gender)


class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance+self.amount
        print("Account balancehas been updated: ", self.balance)

    def withdrow(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Balance. Your balane is: ", self.balance)
        else:
            self.balance = self.balance-self.amount
            print("Your current balance after withdrawal is: ", self.balance)

    def show_balance(self):
        print("You current balance is: ", self.balance)


# neaz = Bank("Ali Neaz", 24, "Male")
# # neaz.deposit(10000)
# # neaz.withdrow(1000)
# # neaz.withdrow(5000)
# neaz.show_balance()
if __name__ == "__main__":
    neaz = Bank("Neaz Ali", 22, "Male")
    while True:
        print("*********Wellcome to the central bank of 420.**********")
        print("Please Select what do you want to do..")
        print("1 For User Details")
        print("2 For Deposite")
        print("3 For withdrow money")
        print("4 show current balance")
        print("5 to quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            neaz.show_details()
        elif choice == 2:
            amount = int(input("Enter the amount you want to deposite: "))
            neaz.deposit(amount)
        elif choice == 3:
            amount = int(input("Enter the amount you want to withdraw:"))
            neaz.withdrow(amount)
        elif choice == 4:
            neaz.show_balance()
        elif choice == 5:
            print("Thank for using our banking system.")
            print("Please combe back later.")
            break
