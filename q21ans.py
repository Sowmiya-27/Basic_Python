size = int(input("Enter the array limit: "))
arr = list(map(int, input("Enter the values of the array: ").split()))
result =[arr[i] * arr[i + 1] for i in range(size - 1)]
print("Output:")
print(*result)
