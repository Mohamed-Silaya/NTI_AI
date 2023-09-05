#q9
def print_formatted(number):
    for i in range(1, number + 1):
        # Convert the number to decimal, octal, hexadecimal, and binary 
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:]
        binary = bin(i)[2:]

        # Print the formatted values
        print(f"{decimal.rjust(10)} {octal.rjust(10)} {hexadecimal.rjust(10)} {binary.rjust(10)}")


print_formatted(5)