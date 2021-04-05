class Atm:
    def __init__(self,cardNumber,pin):
        self.cardNumber = cardNumber
        self.pin = pin

    def total_balance(self):
        print("Your balance is 500000")

    def withdrawl(self,amount):
        if amount >= 500000:
            print("Sorry! Withdrawl failed due to insufficient money")
            
        else:
            new_amount = 500000 - amount
            print("Withdrawn amount is Rupees. "+str(amount) +". Remaining balance is Rupees "+ str(new_amount))

            
        

def main():
    Card_number = input("Enter your card number-  ")
    pin_number  = input("Enter your pin- ")

    new_user =  Atm(Card_number ,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.withdrawl")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        new_user.total_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.withdrawl(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()