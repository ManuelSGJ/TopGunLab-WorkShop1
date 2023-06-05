import os

class BankAccount: 
    def __init__(self, initAccountBalance:float, owner: str, numDoc: str) -> None:
        self.accountBalance = initAccountBalance
        self.owner = owner
        self.numDoc = numDoc
        
    def depositing(self, cant) -> None:
        self.accountBalance = self.accountBalance + cant
        print(f'You havr deposited +{cant} in your account balance')
    
    def withdrawing(self, cant) -> None:
        if self.accountBalance - cant < 0:
            print('It was not possible to withdraw this amount. Please try again with another value.')
        else:
            self.accountBalance = self.accountBalance - cant

    def checkAccountBalance(self) -> None:
        print(f'Your account balance is {self.accountBalance}')

    def checkInfoAccount(self) -> None:
        print(f'''
              Name: {self.owner}
              NumDoc: {self.numDoc}
        ''')


def searchAccount(accounts, word):
    numAccount = input(f'Please the account number that you want to {word} : ')
    cont = 0
    for account in accounts:
        if account.numDoc.strip() == numAccount.strip():
            accountSelected = account
            return [accountSelected, cont, False]
        cont += 1
    
    return ['Account not found', 0, True]

def clearConsole():
    if os.name == 'posix': 
        os.system('clear')
    elif os.name == 'nt': 
        os.system('cls')

print('Welcome to the best bank around the world')

accounts = []
exit = False
while not exit:
    try: 
        clearConsole()
        option = int(input('''
            Please select a choise:
            1- Create a new account
            2- Select an account    
            3- Delete an account          
            4- exit
        '''))

        if option == 4:
            exit = True
            print('Thank you for using the best bank')
            break
        
        elif option == 1: 
            numberDoc = input('Please enter your document number: ')
            name = input('Please enter your name: ')
            initAccountBalance = float(input('Please enter your initial account balance: '))

            accounts.append(BankAccount(initAccountBalance, name, numberDoc))
            print('Account created!')
            continue
        
        elif option == 2 and len(accounts) > 0:
            search = searchAccount(accounts, 'select')
            
            if search[2]:
                print(search[0])
                continue

            accountSelected = search[0]
            exitAccount = False
            while not exitAccount:
                optionAccount = int(input('''
                    Please select a choice:
                    1- Depositing
                    2- Withdrawing   
                    3- Check the account balance         
                    4- Check the account Info
                    5- Exit the account
                '''))

                if optionAccount == 5:
                    optionAccount = True
                    break               
                if optionAccount == 1:
                    cant = float(input('Please enter an anamount that you want to deposite: '))
                    accountSelected.depositing(cant)
                if optionAccount == 2:
                    cant = float(input('Please enter an anamount that you want to withdraw: '))
                    accountSelected.withdrawing(cant)
                if optionAccount == 3:
                    accountSelected.checkAccountBalance()
                if optionAccount == 4:
                    accountSelected.checkInfoAccount()
            
            continue

        elif option == 3 and len(accounts) > 0:
            accountSelected = searchAccount(accounts, 'delete')
            if accountSelected[2]:
                print(accountSelected[0])
                continue
            del accounts[accountSelected[1]]
            print(f'Account {accountSelected[0].numDoc} has been deleted')

        else:
            print('Not account available yet')
            continue

        
    except Exception as err:
        print('Ha ocurrido un error inesperado')
        print(err)