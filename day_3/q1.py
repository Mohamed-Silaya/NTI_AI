import re

users = {}

def validate_phone(phone):
    pattern = r"^01[0125]\d{8}$"
    return re.match(pattern, phone)

# def validate_email(email):
#     pattern = r"^[a-z-A-Z-1:9]@"
#     return re.match(pattern, email)


############################################
def register():
    print("Registration:")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    password = input("Password: ")
    phone = input("Mobile Phone: ")

    if not validate_phone(phone):
        return  print("Invalid phone number.")
    # if not validate_email(email):
    #     return  print("Invalid  email..")
    if email in users:
        return   print("Email already registered.")


    users[email] = {
        "first_name": first_name,
        "last_name": last_name,
        "password": password,
        "phone": phone
    }
    print("Registration successful.")
######################################################
def login():
    print("Login:")
    email = input("Email: ")
    password = input("Password: ")

    if email in users:
        if users[email]["password"] == password:
            print("Login successful.")
        else:
            print("Incorrect password.")
    else:
        print("Email not found.")


#########################################################
x=0
while(x!=3):
    print("enter 1 => for register \n      2 => for login\n      3 => for out")
    x=int(input("Enter (1 or 2 or 3)"))

    if x==1:
        register()
    elif x==2:
        login()
    else:
        print("Invaled OUT")
        