class Bank:

    def __init__(self) :
        self.total_amount = 0
        self.name = ''

    def welcome(self):
        self.name = input("welcome to 2M Bank pls enter your name\nEnter your Name---->")
    
    def checkbalance(self):

        print(f"your current balance is now \n---->{self.total_amount}")

    def deposit(self):
        try:
            self.amount_deposit = int(input("pls enter the amount you would like to deposit in your account\n----amount---> D"))
            self.total_amount += self.amount_deposit
            self.checkbalance()
        except ValueError:
            print("Pls enter a number not a letter thank you")
    
    def widthraw(self):

        try:
            withdraw_amount = int(input("pls enter the amount you would like to widthdraw\n----amount---> D"))

            if withdraw_amount > self.total_amount:
                print("you have insufficient fund\n")
            else:
                self.total_amount -= withdraw_amount
                self.checkbalance()

        except ValueError:
            print("pls enter an number not letter")


if __name__ == "__main__":

    bank = Bank()
    bank.welcome()

    while True:
        try:
            userInput = int(input(f"Enter 1 to check your balance, Enter 2 to deposit into your account, Enter 3 to withdraw\n"))
            if userInput == 1:
                bank.checkbalance()
            elif userInput == 2:
                bank.deposit()
            elif userInput == 3:
                bank.widthraw()
            elif userInput == 0:
                print(f"Thank your for banking with us {bank.name}")
                break
        except ValueError:
            print("follow instructions above thank you ")
            




