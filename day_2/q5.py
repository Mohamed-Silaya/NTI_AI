#q5
def dic_seq(n):
    dict = {}
    for i in range(n):
        key = input("Enter the key: ")
        value = int(key)**2
        dict[key]= int(value)
        print(dict)

dic_seq(3)
