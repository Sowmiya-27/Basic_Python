string= input("Enter a string: ")
string = string.upper()
if string == string[::-1]:
    print("Entered string is a palindrome")
else:
    print("Entered string is not a palindrome")
