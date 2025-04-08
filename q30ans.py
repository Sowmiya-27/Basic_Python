filename = input("Enter the filename: ")  
try:
    with open(filename, "r") as file:
        count= sum(1 for line in file)
    print(f"Number of lines in the file: {count}")
except FileNotFoundError:
    print("File not found. Please enter a valid filename.")

