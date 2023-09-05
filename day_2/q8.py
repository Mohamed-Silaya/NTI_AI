#  q8

def spl(input_string):
    string_list = input_string.split()
    print(string_list)
    print("\n")

    dict = {}

    for i in string_list:
        # Get the first character of the string
        first_char = i[0]
        print(first_char)
        print(i)
        print("\n")

        # Check if the first character already exists as a key in the dictionary
        if first_char in dict:
            # If the key exists, append the string to its corresponding value list
            dict[first_char].append(i)
        else:
            # If the key doesn't exist, create a new key-value pair with the string as the value
            dict[first_char] = [i]

    
input_string = input("Enter a list of strings: ")
spl(input_string)