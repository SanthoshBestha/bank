balance = 0
is_active = True
def show_balance():
    print(f"Your bank balance is {balance:.2f}")
def deposit():
    amount = float(input("Enter amount :"))
    if amount < 0:
        print("Invalid amount")
    else:
        return amount
def withdraw():
    debit = float(input("Enter amount to debit :"))
    if debit > balance:
        print("insufficient balance")
        return 0    
    elif debit < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return debit
def transfer():
    transfer_name = input("Enter Name of the beneficiary : ")
    acc_no=int(input("Enter the Account Number: "))
    transfer_amount=float(input("Enter amount to transfer : "))
    global balance
    if acc_no==0:
        print("Invalid Account Number")
    elif transfer_amount>balance:
        print("Insufficient Balance")
    else:
        balance = balance-transfer_amount
        print(f"Transfer Successful to {transfer_name} with amount {transfer_amount}")

def balance_clear():
    global balance
    global is_active
    balance = balance*0
    is_active = False
while is_active:
    print("*********Welcome to Bank************")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Transfer")
    print("5.Balance Clear")
    print("6.Exit")
    print("********Have a good day*************")
    choice = input("Enter your choice{1-6}: ")

    if choice == "1":
        show_balance()
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdraw()
    elif choice == "4":
        transfer()
    elif choice == "5":
        balance_clear()
    elif choice == "6":
        is_active = False
    else:
        print("Sorry,Invalid code entered")
print("thank you for banking")
