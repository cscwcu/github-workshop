import ast

# Implementing Bubble Sort for alphanumeric sorting
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def process_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    for line in lines:
        # Convert the string representation of the list into a Python list
        arr = ast.literal_eval(line.strip())
        # Sort the list using bubble sort
        sorted_arr = bubble_sort(arr)
        # Print the sorted array
        print(sorted_arr)

process_file('test.txt')
