#################### Code starts here ####################
import os #to get the address of present working directory
import re #to validate email address
CurrentPath = os.getcwd() #current path of working directory
filepath = CurrentPath + '/Emply_details.txt' #path of the data file

#################### Functions to validate details ####################
def isValid_email(email):
    # 1) Begins with alphanumeric data incluing - and _
    # 2) Then contains @
    # 3) Then contains alphanumeric data
    # 4) Then contains .
    # 5) Then contains alphanumeric data of size 1 to 3
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(pat,email):
        return True
    return False

def isValid_mobile(mobile):
    # 1) Begins with 0 or 91
    # 2) Then contains 6,7 or 8 or 9.
    # 3) Then contains 9 digits
    Pattern = re.compile("(0|91)?[6-9][0-9]{9}")
    return Pattern.match(mobile)

#################### Menu functions ####################
def add():
    name = input("Enter the employee name: ")   #taking name input
    emply_no = input("Enter the employee number: ") #taking employee number input
    mobile = input("Enter employee mobile number: ")    #taking employee mobile number input
    while not isValid_mobile(mobile):   #checking if mobile is valid
        print("Invalid mobile number")
        mobile = input("Enter the mobile number again: ")
    email = input("Enter employee email address: ") #taking employee email address input
    while not isValid_email(email): #checking if email is valid
        print("Invalid email")
        email = input("Enter the email address again: ")
    #Adding data to file
    file = open(filepath,'a')
    file.write(emply_no+"\t")
    file.write(name+"\t")
    file.write(mobile+"\t")
    file.write(email)
    print("Employee data successfully added!")
    file.close()

def update():
    try:
        employ_no = input("Enter the employee number: ")    #taking employee number input
        file = open(filepath, 'r') #Opening file in read mode
        all = file.readlines() #storing all lines of the file
        file.close()
        file = open(filepath, 'w')  #opening file in write mode
        found = False
        for data in all:
            d = data.split("\t")
            if d[0] != employ_no:       #if other employee data add to file
                file.writelines(data)
            else:
                found = True
                op = int(input("What do you want to change:\n1.Name 2.Mobile 3.Email\t: "))
                if op == 1:
                    d[1] = input("Enter new Name: ")
                elif op == 2:
                    d[2] = input("Enter new mobile number: ")
                elif op == 3:
                    d[3] = input("Enter new email: ")
                else:
                    print("Invalid option")
                file.writelines(d[0]+"\t"+d[1]+"\t"+d[2]+"\t"+d[3]) #updating data in the file
        if found == True:
            print("Data is updated!")
        else:
            print("Data not found in the list!")
        file.close()
    except:     #if file is not found
        print("File doesn't have any data!")

def delete():
    try:
        employ_no = input("Enter the employee number: ")    #taking employee number input
        file = open(filepath, 'r') #Opening file in read mode
        all = file.readlines() # storing all lines of the file
        file.close()
        file = open(filepath, 'w')  #opening file in write mode
        deleted = "No data found for the above number"
        for data in all:
            d = data.split("\t")
            if d[0] != employ_no:       #if other employee data add to file
                file.writelines(data)
            else:                       #if found, not adding in to file
                deleted = data
        if deleted == "No data found for the above number":
            print(deleted)
        else:
            print("Data deleted is",deleted)
        file.close()
    except: #if file is not found
        print("File doesn't have any data")

def search():
    try:
        employ_no = input("Enter the employee number: ")    #taking employee number input
        file = open(filepath, 'r') #Opening file in read mode
        all = file.readlines() # storing all lines of the file
        file.close()
        emply_data = "No data found for the above number"
        for data in all:
            d = data.split("\t")
            if d[0] == employ_no:   #if data is found
                emply_data = data
        if emply_data == "No data found for the above number":
            print(emply_data)
        else:
            print("Data found is",emply_data)
    except: #if file is not found
        print("File doesn't have any data")

def display():
    try:
        print("The data in the file is: ")
        file = open(filepath, 'r') #Opening file in read mode
        all = file.readlines() # storing all lines of the file
        file.close()
        for data in all:
            print(data)
    except: #if file is not found
        print("File doesn't have any data")


#################### Main code starts here ####################
print("Welcome to the Employee Details Portal!")
while(True):
    print("Menu:")
    print("1. Add a new employee")
    print("2. Update an employee's details")
    print("3. Delete an employee's details")
    print("4. Search the details of an employee")
    print("5. Display details of all the employees")
    print("6. Exit menu")
    t = int(input("Select any option: "))
    if t == 1:
        add()
    elif t == 2:
        update()
    elif t == 3:
        delete()
    elif t == 4:
        search()
    elif t == 5:
        display()
    elif t == 6:
        break
    else:
        print("Choose valid option!")
print("Thank you, Have a nice day!")