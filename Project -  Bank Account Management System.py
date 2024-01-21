import csv
def account_creation():
    with open('Account.csv',mode='a') as csvfile:
        mywriter = csv.writer (csvfile, delimiter=',')
        print("Welcome to our bank !!!")
        account_holder=input("Enter your name:")
        email_id=input("Enter your email address:")
        password=input("Enter your password:")
        balance=int(input("Enter your balance:"))
        details=[account_holder, email_id, password, balance]
        mywriter.writerow(details)
        print("Data Saved.....")
def account_balance():
    with open('Account.csv',mode='r') as csvfile:
        myreader = csv.reader (csvfile, delimiter=',')
        account_holder=input("Enter your name:")
        for row in myreader:
            if len(row)!=0:
                if (row[0])==account_holder:
                    print("Your Bank Account details:")
                    print ("NAME :", row[0])
                    print ("Email-ID:", row[1])
                    print ("Balance:",row[3])
                    break
def deposits():
    with open('Account.csv',mode='r') as csvfile:
        myreader = csv.reader (csvfile, delimiter=',')
        account_holder=input("Enter your name:")
        deposit_amount=int(input("Enter Deposit Amount:"))
        rows = list(myreader)
        for row in rows:
            if len(row) !=0:
                if (row[0])==account_holder:
                    updated_balance = int(row[3]) + deposit_amount
                    row[3] = str(updated_balance)

                    with open('Account.csv', mode='w', newline='') as csvfile_write:
                        mywriter = csv.writer(csvfile_write, delimiter=',')
                        mywriter.writerows(rows)
                    print("Your Bank Account details:")
                    print ("NAME :", row[0])
                    print ("Email-ID:", row[1])
                    print ("Deposited amount:",deposit_amount)
                    print ("Balance:",updated_balance)
        
def withdrawal():
    with open('Account.csv',mode='r') as csvfile:
        myreader = csv.reader (csvfile, delimiter=',')
        account_holder=input("Enter your name:")
        withdrawal_amount=int(input("Enter Withdrawal Amount:"))
        rows = list(myreader)
        for row in rows:
            if len(row)!=0:
                if (row[0])==account_holder:
                    if int(row[3]) < withdrawal_amount:
                        print("Insufficient balance for withdrawal.")
                        break

                    updated_balance = int(row[3]) - withdrawal_amount
                    row[3] = str(updated_balance)

                    with open('Account.csv', mode='w', newline='') as csvfile_write:
                        mywriter = csv.writer(csvfile_write, delimiter=',')
                        mywriter.writerows(rows)
                    print("Your Bank Account details:")
                    print ("NAME :", row[0])
                    print ("Email-ID:", row[1])
                    print ("Withdrawing amount:",withdrawal_amount)
                    print ("Balance:",updated_balance)

while True:
    print("1. Sign up")
    print("2. Balance")
    print("3. Place a deposit")
    print("4. Withdrawal Money")
    print("5. Exit")
    choices=int(input("Enter your choice(s):"))
    if choices ==1:
        account_creation()
    elif choices ==2:
        account_balance()
    elif choices ==3:
        deposits()
    elif choices ==4:
        withdrawal()
    elif choices ==5:
        print("Thank you for being the part of our community")
        break
    else:
        print("Wrong choice made....Please select a choice between 1 and 5")
