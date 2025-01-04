# Masai_project
Basic Demonstration of a banking system
Description:
This project simulates a basic banking system that allows users to create accounts, log in, perform transactions (deposits and withdrawals), and maintain a record of accounts and transactions using file handling in Python. It is a command-line-based program suitable for learning purposes.

Features:
Main Menu:

Create a new account.
Login to an existing account.
Exit the application.
Account Management:

Accounts are saved in the accounts.txt file.
Each account includes:
Name
Initial deposit
Account number (auto-generated)
Password
Transactions:

Deposit money.
Withdraw money.
Transactions are logged in the transactions.txt file with:
Account number
Transaction type (Deposit or Withdrawal)
Amount
Date
Data Persistence:

All data is stored in plain text files (accounts.txt and transactions.txt) for future use.
File Structure:
accounts.txt: Stores account details.
Format: Name, Balance, AccountNumber, Password
transactions.txt: Logs transactions.
Format: AccountNumber, TransactionType, Amount, Date
Prerequisites:
Python 3.x
Basic understanding of Python file handling and control flow.
How to Run:
Clone or download this project to your local machine.
Open a terminal and navigate to the project folder.
Run the script using:
bash
Copy code
python <filename>.py
Follow the prompts displayed on the screen.
How It Works:
1. Main Menu:
Choose from:
1 to create a new account.
2 to log in and access the sub-menu.
3 to exit the application.
2. Sub-Menu:
Once logged in:
1 to deposit money.
2 to withdraw money.
3 to exit to the main menu.
3. Account Creation:
Input your name, initial deposit, and password.
An account number is auto-generated and displayed.
The account details are saved in accounts.txt.
4. Login:
Enter your account number and password.
Upon successful login, access the sub-menu for transactions.
5. Transactions:
Perform deposits and withdrawals.
All transactions are recorded in transactions.txt.
Functions Overview:
mainmenu(): Displays the main menu.
subMenu(): Displays the sub-menu after login.
accsave(): Saves account information to accounts.txt.
Transsave(): Logs transaction details in transactions.txt.
generate_account_number(): Generates a unique account number.
main(): Main function to drive the program.
