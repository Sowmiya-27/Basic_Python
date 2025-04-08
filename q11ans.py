size = int(input("Enter the size of an array: "))  
arr = list(map(int, input("Enter the values of array: ").split()))  
even = 0  
for num in arr:  
    if num % 2 == 0:  
        even += 1  
print("Number of even numbers in the given array is", even)  

