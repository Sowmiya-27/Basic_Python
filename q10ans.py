size = int(input("Enter the size of arrays: "))
arr1 = list(map(int, input("Enter the values of Array 1: ").split()))   
arr2 = list(map(int, input("Enter the values of Array 2: ").split()))  
temp = arr1  
arr1 = arr2  
arr2 = temp  
print("Arrays after swapping:")
print("Array1:", *arr1)
print("Array2:", *arr2)


