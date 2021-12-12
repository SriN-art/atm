class Atm(object):
    def __init__(self, cardnumber, pin):
        self.cardnumber=cardnumber
        self.pin = pin
    def checkbalance(self):
        print('Your balance is 50,000')
    def withdrawal(self, amount):
        newAmount = 50000-amount
        print('You have withdrawn amount '+str(amount)+'. Your remaining balance is '+str(newAmount))
def main():
    cardnumber=input('Insert your card number: ')
    pinnumber=input('Insert your pin number: ')
    newUser = Atm(cardnumber, pinnumber)
    print('Choose your activity')
    print('1. Balance Enquiry  2. Withdrawal')
    activity=int(input('Enter activity number: '))
    if activity==1:
        newUser.checkbalance()
    elif activity==2:
        amount=int(input('Enter the amount: '))
        newUser.withdrawal(amount)
    else:
        print('Enter a valid number')
main()
    