import datetime


def check_acc():
    d = int(input("Enter Account number : "))
    file = open("bankaccount.txt", "r")
    a = file.readlines()
    i = 0
    while i < len(a):
        b = a[i].split(",")
        t = b[0].count(str(d))
        if t != 0:
            if str(d) == b[0] and b[7] != "C\n":
                file.close()
                return [0, i]
        i = i + 1


def check_pin():
    d = int(input("Enter Your PIN : "))
    file = open("bankaccount.txt", "r")
    a = file.readlines()
    i = 0
    while i < len(a):
        b = a[i].split(",")
        t = b[1].count(str(d))
        if t != 0:
            if str(d) == b[1]:
                return 0
        i = i + 1


def add_account():
    print("Accepting details of Account : ")
    acno = input("Enter Your Account Number : ")
    pin = input("Enter your initial pin : ")
    n = input("Enter Your Name : ")
    b = input("Enter Initial Balance : ")
    add = input("Enter your address : ")
    mob = input("Enter your Mobile Number : ")
    email = input("Enter Your Email :  ")
    file = open("bankaccount.txt", "a")
    file.write(acno + "," + pin + "," + n + "," + b + "," + add + "," + mob + "," + email + "," + "A" + "\n")
    file.close()

    print("Account  successfully created")


def withdraw():
    w = check_acc()
    if w[0] == 0:
        w1 = check_pin()
        if w1 == 0:
            wi = int(input("Enter amount to withdraw : "))
            file = open("bankaccount.txt", "r")
            a = file.readlines()
            ind = w[1]
            b = a[ind].split(",")
            wbal = float(b[3])
            wbal = wbal - wi
            b[3] = str(wbal)
            new = ",".join(b)
            a[ind] = new
            file.close()
            file = open("bankaccount.txt", "w")
            file.writelines(a)
            file.close()
            print("Withdraw successful")
            d = datetime.date.today()
            tran = open(b[0] + "transaction.txt", "a")
            tran.write(b[0] + "," + str(d) + "," + "withdraw - " + "," + str(wi) + "\n")
            print("New Balance is", wbal)


def pin_change():
    w = check_acc()
    if w[0] == 0:
        w1 = check_pin()
        if w1 == 0:
            b1 = int(input("Enter Your new PIN : "))
            c1 = int(input("Re-Enter your new PIN : "))
            if b1 == c1:
                print("PIN successfully changed")
                file = open("bankaccount.txt", "r")
                a = file.readlines()
                i = 0
                while i < len(a):
                    b = a[i].split(",")
                    b[1] = str(c1)
                    new = ",".join(b)
                    a[i] = new
                    file.close()
                    file = open("bankaccount.txt", "w")
                    file.writelines(a)
                    file.close()
                    break
            else:
                print("Previous PIN and New PIN doesn't Match")


def deposite():
    w = check_acc()
    if w[0] == 0:
        file = open("bankaccount.txt", "r")
        a = file.readlines()
        ind = w[1]
        b = a[ind].split(",")
        wbal = float(b[3])
        wi = float(input("Enter amount to deposite : "))
        wbal = wbal + wi
        b[3] = str(wbal)
        new = ",".join(b)
        a[ind] = new
        file.close()
        file = open("bankaccount.txt", "w")
        file.writelines(a)
        file.close()
        print("Deposite sucessfull")
        print("New Balance is", wbal)
        d = datetime.date.today()
        tran = open(b[0] + "transaction.txt", "a")
        tran.write(b[0] + "," + str(d) + "," + "deposite -" + "," + str(wi) + "\n")


def check_balance():
    a = check_acc()
    if a[0] == 0:
        b2 = check_pin()
        if b2 == 0:
            file = open("bankaccount.txt", "r")
            c = file.readlines()
            ind = a[1]
            b = c[ind].split(",")
            print("Balance : ", b[ind])
            file.close()


def check_mini():
    a = check_acc()
    if a[0] == 0:
        b2 = check_pin()
        if b2 == 0:
            ind = a[1]
            file = open("bankaccount.txt", "r")
            c = file.readlines()
            b = c[ind].split(",")
            if float(b[3]) > 2000:
                print("Account Balanced is maintained")
                print("Balance : ", b[3])
            else:
                b[3] = str(float(b[3]) - 20)
                print("Account Balance is less than  MINIMUM required Balance Fine Rs.20")
                print("Balance : ", b[3])
                new = ",".join(b)
                c[ind] = new
                file.close()
                file = open("bankaccount.txt", "w")
                file.writelines(c)
                file.close()


def addinter():
    a = check_acc()
    if a[0] == 0:
        b2 = check_pin()
        if b2 == 0:
            ind = a[1]
            file = open("bankaccount.txt", "r")
            c = file.readlines()
            b = c[ind].split(",")
            inte = (float(b[3]) / 100) * 4
            intee = float(b[3]) + inte
            print("Rs.", inte, "Credited as Interest.")
            print("New Balance is ", (float(b[3]) + intee))
            b[3] = str((float(b[3]) + intee))
            new = ",".join(b)
            c[ind] = new
            file.close()
            file = open("bankaccount.txt", "w")
            file.writelines(c)
            file.close()


def show_info():
    a = check_acc()
    if a[0] == 0:
        b2 = check_pin()
        if b2 == 0:
            file = open("bankaccount.txt", "r")
            c = file.readlines()
            i = a[1]
            b = c[i].split(",")
            print("Account Number : ", b[0])
            print("Balance : ", b[3])
            print("PIN : ", b[1])
            file.close()


def transfer_fund():
    first = check_acc()
    if first[0] == 0:
        print("Transfer to ---")
        second = check_acc()
        if second[0] == 0:
            am = float(input("Amount to Transfer : -"))
            if am >= 1000:
                b2 = check_pin()
                if b2 == 0:
                    ind1 = first[1]
                    ind = second[1]
                    file = open("bankaccount.txt", "r")
                    c = file.readlines()
                    b = c[ind1].split(",")
                    d = c[ind].split(",")
                    b[3] = str(float(b[3]) - am)
                    print("Rs.", am, "sucessfull transfer to Account", d[0])
                    file.close()
                    file = open("bankaccount.txt", "w")
                    new = ",".join(b)
                    c[ind1] = new
                    file.writelines(c)
                    file.close()
                    file = open("bankaccount.txt", "w")
                    d[3] = str(float(d[3]) + am)
                    new = ",".join(d)
                    c[ind] = new
                    file.writelines(c)
                    file.close()
                    print("New Balanace of Account no.", b[0], "Rs.", b[3])
                    print("New Balance of Account no.", d[0], "Rs.", d[3])

            else:
                print("Insufficicent Balance, Minimum Balance required for transfering funds is Rs.1000 ")


def tran_history():
    a = check_acc()
    if a[0] == 0:
        b2 = check_pin()
        if b2 == 0:
            file = open("bankaccount.txt", "r")
            c = file.readlines()
            ind = a[1]
            b = c[ind].split(",")
            tran = open(str(b[0]) + "transaction.txt", "r")
            b = tran.readlines()
            tran.close()
            b.reverse()
            count = 10
            for ele in b:
                ele.split(",")
                print(str(ele), end="")
                count = count + 1
                if count == 10:
                    break


def update_account():
    print()
    print("--------------------------------------------------------------------")
    print("Select an operation")
    print("1 - Update mobile number")
    print("2 - Update address")
    print("3 - Update email-address")
    ch1 = int(input("Provide your choice -"))
    print()
    print("----------------------------------------------------------------------")
    if ch1 == 1:
        a = check_acc()
        if a[0] == 0:
            b2 = check_pin()
            if b2 == 0:
                file = open("bankaccount.txt", "r")
                c = file.readlines()
                ind = a[1]
                b = c[ind].split(",")
                inn = input("Enter your new mobile number : ")
                b[5] = inn
                new = ",".join(b)
                c[ind] = new
                file.close()
                file = open("bankaccount.txt", "w")
                file.writelines(c)
                file.close()
    elif ch1 == 2:
        a = check_acc()
        if a[0] == 0:
            b2 = check_pin()
            if b2 == 0:
                file = open("bankaccount.txt", "r")
                c = file.readlines()
                ind = a[1]
                b = c[ind].split(",")
                inn = input("Enter your new address : ")
                b[4] = inn
                new = ",".join(b)
                c[ind] = new
                file.close()
                file = open("bankaccount.txt", "w")
                file.writelines(c)
                file.close()
    elif ch1 == 3:
        a = check_acc()
        if a[0] == 0:
            b2 = check_pin()
            if b2 == 0:
                file = open("bankaccount.txt", "r")
                c = file.readlines()
                ind = a[1]
                b = c[ind].split(",")
                inn = input("Enter your new email address : ")
                b[6] = inn
                new = ",".join(b)
                c[ind] = new
                file.close()
                file = open("bankaccount.txt", "w")
                file.writelines(c)
                file.close()
    else:
        print("Invalid choice..")


def close_account():
    a = check_acc()
    if a[0] == 0:
        b2 = check_pin()
        if b2 == 0:
            num = input("Are you sure that you want to delete your account (Y/N):")
            if num == "Y" or "y":
                file = open("bankaccount.txt", "r")
                c = file.readlines()
                ind = a[1]
                b = c[ind].split(",")
                b[7] = "C\n"
                new = ",".join(b)
                c[ind] = new
                file.close()
                file = open("bankaccount.txt", "w")
                file.writelines(c)
                file.close()


while True:
    print()
    print("--------------------------------------------------------------------")
    print("Select an operation")
    print("1 - New Account")
    print("2 - Withdrawal")
    print("3 - Deposite")
    print("4 - PIN change")
    print("5 - Check Balance")
    print("6 - Check for MINIMUM balance")
    print("7 - Add Interest")
    print("8 - Transfer Funds")
    print("9 - Show Account Information")
    print("10 - View Transaction History")
    print("11 - Update Account Info")
    print("12 - Delete Account")
    print("0 - EXIT")
    ch = int(input("Provide your choice -"))
    print()
    print("----------------------------------------------------------------------")
    if ch == 1:
        add_account()
    elif ch == 2:
        withdraw()
    elif ch == 3:
        deposite()
    elif ch == 4:
        pin_change()
    elif ch == 5:
        check_balance()
    elif ch == 6:
        check_mini()
    elif ch == 7:
        addinter()
    elif ch == 8:
        transfer_fund()
    elif ch == 9:
        show_info()
    elif ch == 10:
        tran_history()
    elif ch == 11:
        update_account()
    elif ch == 12:
        close_account()
    elif ch == 0:
        exit(0)
    else:
        print("Invalid choice.....")
