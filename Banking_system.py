#imports
import random
from datetime import date
#global variable
choice="choice"
option="option"
accNumber="accnum"
#Main Menu/////
def mainmenu():
    global choice
    print("Welcome to the Banking System!")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")
#Sub Menu function
def subMenu():
    global option
    print("Service:")
    print("1.Deposit.")
    print("2.Withdrawals.")
    print("3.Exit")
    option=input("What service do you require:")     
#file handlings
with open("accounts.txt", "w") as file:
    file.write("Name, Balance, accountNumber, Password \n")
with open("transactions.txt", "w") as file:
    file.write("accountNumber, TransactionType, Amount, Date \n")
#Function for saving account information
def accsave(name,deposit,accNumber,password):
    with open('accounts.txt', 'a') as file:
        file.write(f"{name},{deposit},{accNumber},{password} \n")
#Function for saving the transaction information
def Transsave(accNumber,amountin,date,tracsType):
    with open('transactions.txt', 'a') as file:
        file.write(f"{accNumber},{tracsType},{amountin},{date} \n")  
#Function to generate the accnumber
def generate_account_number(length=10):
    # Ensure the account number starts with a non-zero digit
    first_digit = random.randint(1, 9)
    # Generate the remaining digits
    remaining_digits = ''.join(random.choices('0123456789', k=length-1))
    return str(first_digit) + remaining_digits
  
#choices Main menu
#Choice 1
def main():
    global accNumber
    while True:
        mainmenu()
        try:
            choice = int(input("Enter Your Choice: "))
            #choice1
            if(int(choice)==1):
                name=input("Enter your name:")
                deposit=int(input("Enter your initial deposit:"))
                password=input("Enter your password:")
                accNumber=generate_account_number()
                print(f"Your account number is: {accNumber}")
                accsave(name,deposit,accNumber,password)
                print("Account Created")
            #choice2
            if(int(choice)==2):
                accountSearch=input("Enter your account number:")
                passCheck=input("Enter your password:")
                #check if there is an account with that number
                with open("accounts.txt", "r") as f:
                    for line in f:
                        if "Name" in line:
                            continue
                        parts=line.strip().split(",")
                        if parts[2]==accountSearch and parts[3]==passCheck:
                            print("Login Success")
                            print(f"Welcom {parts[0]}")
                            subMenu()
                        else:
                            print("Account Number or Password Incorrect")
                            break
            if(int(choice)==3):
                print("Thank you for using the Banking System. Goodbye!")
                break  # Exit the program
            #choices sub menu
            #Deposit
            if(option=="1"):
                amountin=int(input("Enter the amount:"))
                dates=date.today()
                Transsave(accNumber,amountin,dates,tracsType="Deposit")
                print("Amount Credited")
            #Withdrawls 
            if(option=="2"):
                amountin=int(input("Enter the amount:"))
                dates=date.today()
                Transsave(accNumber,amountin,dates,tracsType="Withdrawl")
                print("Amount Debtied")
            #Exit
            if(option=="3"):
                break 
        except ValueError:
            print("Invalid input. Please enter a valid number.")  

# Run the program
if __name__ == "__main__":
    main()    




