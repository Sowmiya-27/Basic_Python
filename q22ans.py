def getArray(size):
    arr = []
    for i in range(size):
        row = list(map(int, input().split()))
        arr.append(row)
    return arr
def addArray(arr1, arr2, size):
    result = [[arr1[i][j] + arr2[i][j]
               for j in range(size)]
                  for i in range(size)]
    return result
def displayArray(arr):
    for row in arr:
        print(*row)
def main():
    size = int(input("Enter the size of the array: "))
    print("Enter the values of array 1:")
    arr1 = getArray(size)
    print("Enter the values of array 2:")
    arr2 = getArray(size)
    result = addArray(arr1, arr2, size)
    print("\nSum of array 1 and array 2:")
    displayArray(result)
if __name__ == "__main__":
    main()
