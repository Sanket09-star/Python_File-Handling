import datetime


def issue_book():
    d = datetime.date.today()
    bn = input("Enter a Book number : ")
    sr = input("Enter Student enrollment number : ")
    file = open("D:\\Sanket\\Python Saves\\File Handling\\libfiles\\ all_issue_books.txt", "a")
    file.write(bn+","+sr+","+str(d)+","+"NA"+"\n")
    print("Book Successfully issued.")
    file.close()


def return_book():
    book_found = False
    d = datetime.date.today()
    user_input = input("Enter Book Number to Return : ")
    file = open("D:\\Sanket\\Python Saves\\File Handling\\libfiles\\ all_issue_books.txt", "r")
    all_issues = file.readlines()
    i = 0
    while i < len(all_issues):
        onedata_ls = all_issues[i].split(",")
        if onedata_ls[0] == user_input and onedata_ls[3] == "NA\n":
            onedata_ls[3] = str(d) + "\n"
            new_data = ",".join(onedata_ls)
            all_issues[i] = new_data
            book_found = True
            break
        i = i + 1
    file.close()

    if book_found == True:
        file = open("D:\\Sanket\\Python Saves\\File Handling\\libfiles\\ all_issue_books.txt", "w")
        file.writelines(all_issues)
        file.close()
        print("Book Returned..!")
    if book_found == False:
        print("Invalid Book Number.")




def add_new_book():
    while True:
        bt = input("\nEnter Book title : ")
        bp = input("Enter Book publication : ")
        bn = input("Enter Book number : ")
        file = open("D:\\Sanket\\Python Saves\\File Handling\\libfiles\\ all_books.txt", "a")
        file.write(bt + "," + bp + "," + bn + "\n")
        c = input("\nDo you want to add another book (Y or N) : ")
        if c == "N":
            file.close()
            print("!!Data successfully saved!!")
            break
        elif c == "Y":
            continue
        else:
            file.close()
            print("\nInvalid choice!!")
            break


def add_new_student():
    while True:
        sa = input("\nEnter Student Name : ")
        se = input("Enter Student Enrollment  : ")
        smn = input("Enter Student Mobile Number : ")
        sm = input("Enter Student E-mail : ")
        file = open("D:\\Sanket\\Python Saves\\File Handling\\libfiles\\ all_students.txt", "a")
        file.write(sa + "," + se + "," + smn + ","+sm+"\n")
        c = input("\nDo you want to add another Student (Y or N) : ")
        if c == "N":
            file.close()
            print("!!Data successfully saved!!")
            break
        elif c == "Y":
            continue
        else:
            file.close()
            print("\nInvalid choice!!")
            break


def book_history():
    book_found = False
    user_input = input("Enter Book Number  : ")
    file = open("D:\\Sanket\\Python Saves\\File Handling\\libfiles\\ all_issue_books.txt", "r")
    all_issues = file.readlines()
    i = 0
    while i < len(all_issues):
        onedata_ls = all_issues[i].split(",")
        if onedata_ls[0] == user_input and onedata_ls[3] == "NA\n":
            print(all_issues[i])
            book_found = True
            break
        i = i + 1
    file.close()
    if book_found == False:
        print("Invalid Book Number.")


def student_history():
    book_found =False
    user_input = input("Enter Enrollment Number : ")
    file = open("D:\\Sanket\\Python Saves\\File Handling\\libfiles\\ all_issue_books.txt", "r")
    all_issues = file.readlines()
    i = 0
    while i < len(all_issues):
        onedata_ls = all_issues[i].split(",")
        if onedata_ls[1] == user_input:
            print(all_issues[i])
            book_found = True
            break
        i = i + 1
    file.close()
    if book_found == False:
        print("Invalid Enrollment Number.")


def search_book():
    print("Select an option")
    print("1 - Search By Book Number\n2 - Search By Book Title\n3 - Search By Publication")
    ch2 = int(input("Provide Your Choice : "))
    if ch2 == 1:
        file = open("D:\\Sanket\\Python Saves\\File Handling\\libfiles\\ all_books.txt", "r")
        user_input = input("Enter Book Number : ")
        rea = file.readline()
        while True:
            rea = rea.removesuffix("\n")
            ls = rea.split(",")
            if user_input == ls[2]:
                print(rea)
                file.close()
                break
            rea = file.read()
        file.close()
    elif ch2 == 2:
        file = open("D:\\Sanket\\Python Saves\\File Handling\\libfiles\\ all_books.txt", "r")
        user_input = input("Enter Book Title : ")
        rea = file.readline()
        while True:
            rea = rea.removesuffix("\n")
            ls = rea.split(",")
            if user_input == ls[0]:
                print(rea)
                file.close()
                break
            rea = file.read()
        file.close()
    elif ch2 == 3:
        file = open("D:\\Sanket\\Python Saves\\File Handling\\libfiles\\ all_books.txt", "r")
        user_input = input("Enter Book Publication : ")
        rea = file.readline()
        while True:
            rea = rea.removesuffix("\n")
            ls = rea.split(",")
            if user_input == ls[1]:
                print(rea)
                file.close()
                break
            rea = file.read()
        file.close()
    else:
        print("Invalid Choice")


def search_student():
    print("Select an option")
    print("1 - Search By Enrollment Number\n2 - Search By Mobile Number\n3 - Search By Email Address")
    ch3 = int(input("Provide Your Choice : "))
    if ch3 == 1:
        file = open("D:\\Sanket\\Python Saves\\File Handling\\libfiles\\ all_students.txt", "r")
        user_input = input("Enter Enrollment Number : ")
        rea = file.readline()
        while True:
            rea = rea.removesuffix("\n")
            ls = rea.split(",")
            if user_input == ls[1]:
                print(rea)
                file.close()
                break
            rea = file.read()
        file.close()
    elif ch3 == 2:
        file = open("D:\\Sanket\\Python Saves\\File Handling\\libfiles\\ all_students.txt", "r")
        user_input = input("Enter Mobile Number : ")
        rea = file.readline()
        while True:
            rea = rea.removesuffix("\n")
            ls = rea.split(",")
            if user_input == ls[2]:
                print(rea)
                file.close()
                break
            rea = file.read()
        file.close()
    elif ch3 == 3:
        file = open("D:\\Sanket\\Python Saves\\File Handling\\libfiles\\ all_students.txt", "r")
        user_input = input("Enter E-mail Address : ")
        rea = file.readline()
        while True:
            rea = rea.removesuffix("\n")
            ls = rea.split(",")
            if user_input == ls[3]:
                print(rea)
                file.close()
                break
            rea = file.read()
        file.close()
    else:
        print("Invalid Choice")


def not_returned_books():
    file = open("D:\\Sanket\\Python Saves\\File Handling\\libfiles\\ all_issue_books.txt", "r")
    all_issues = file.readlines()
    i = 0
    while i < len(all_issues):
        onedata_ls = all_issues[i].split(",")
        if onedata_ls[3] == "NA\n":
            print(all_issues[i])
        i = i + 1
    file.close()



while True:
    print("\n1:Issue Book\n2:Return Book\n3:Add new Book\n4:Add new Student\n5:Book History\n6:Student History")
    print("7:Search Book\n8:Search Student\n9:Not Returned Books\n0:Exit\n")
    ch = int(input("Enter Your choice : "))
    if ch == 1:
        issue_book()
    elif ch == 2:
        return_book()
    elif ch == 3:
        add_new_book()
    elif ch == 4:
        add_new_student()
    elif ch == 5:
        book_history()
    elif ch == 6:
        student_history()
    elif ch == 7:
        search_book()
    elif ch == 8:
        search_student()
    elif ch == 9:
        not_returned_books()
    elif ch == 0:
        exit(0)
    else:
        print("Invalid choice,Try again!!!!")
