s= int(input("Enter the size of an array:"))  
a= list(map(int, input("Enter the values of an array:").split()))
temp = a[:]
for i in range(s):
    for j in range(i + 1,s):
        if temp[i] < temp[j]:
            temp[i], temp[j] = temp[j], temp[i]
print("Sorted array:")
print(*temp, sep=", ")  

