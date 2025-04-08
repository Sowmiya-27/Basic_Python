lim=int(input("Enter a limit: "))  
odd=0  
for i in range(1, lim + 1):  
    if i % 2 != 0:  
        odd += i  
print("Sum of odd numbers =", odd)  

