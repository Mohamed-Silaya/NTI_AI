# q7
def collect_user_data():
    name = input("Enter your name: ")
    while not name or name.isdigit():
        email = input("Enter your email: ")
        print("Name:", name)
        print("Email:", email)