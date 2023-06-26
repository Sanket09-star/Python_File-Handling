while True:
    print("1 - Administration Log in\n2 - User Log in\n3 - Create Account\n0 - Exit")
    ch = int(input("Enter Your Choice : "))
    if ch == 3:
        print("1 - Administration\n2 - User")
        ch1 = int(input("Enter Your Account Choice : "))
        if ch1 == 1:
            file = open("adminaccount.txt", "a")
            name = input("Enter Your Name : ")
            id = input("Create id : ")
            pas = input("Create password : ")
            mob = input("Enter Your Mobile Number : ")
            hotel = input("Enter Your Hotel Name : ")
            file.write(id + "," + pas + "," + name + "," + mob + "," + hotel + "\n")
            print("Account created....")
            file.close()
        elif ch1 == 2:
            file = open("useraccount.txt", "a")
            name = input("Enter Your Name : ")
            id = input("Create id : ")
            pas = input("Create password : ")
            mob = input("Enter Your Mobile Number : ")
            file.write(id + "," + pas + "," + name + "," + mob + "\n")
            print("Account created....")
            file.close()
        else:
            print("Invalid choice..")

    elif ch == 1:
        idd = input("Enter Your ID  : ")
        pas1 = input("Enter Your Password : ")
        file = open("adminaccount.txt", "r")
        alll = file.readlines()
        i = 0
        while i <= len(alll):
            data = alll[i].split(",")
            if data[0] == idd and data[1] == pas1:
                print("Yes")
            else:
                print("No")
            i = i + 1
        file.close()

    elif ch == 2:
        id1 = input("Enter Your ID  : ")
        pas1 = input("Enter Your Password : ")
        file = open("useraccount.txt", "r")
        all = file.readlines()
        i = 0
        while i <= len(all):
            data = all[i].split(",")
            if data[0] == id1 and data[1] == pas1:
                print("Yes")
                break
            else:
                print("No")
            i = i + 1
        file.close()
    elif ch == 0:
        break
    else:
        print("Invalid Input..")



