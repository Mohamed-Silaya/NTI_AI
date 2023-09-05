# Q3
def sort_array():
    array = []
    for i in range(5):
     element = int(input(f"Enter element {i+1}: "))
     array.append(element)
    # Sort the array in descending order
    descending_order = sorted(array, reverse=True)
    # Sort the array in ascending order
    ascending_order = sorted(array)
    # Display the output
    print("Descending order:", descending_order)
    print("Ascending order:", ascending_order)