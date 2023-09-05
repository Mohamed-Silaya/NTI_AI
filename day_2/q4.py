# q4
def dic(n):
    dict = {}
    for i in range(n):
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        dict[key]= int(value)
        print(dict)

    sum_of_values = 0
    for value in dict.values():
        sum_of_values += value
    print( sum_of_values)

dic(3)