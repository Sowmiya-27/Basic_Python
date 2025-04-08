class TwoDArray:
    def __init__(self, size):
        self.size = size
        self.arr = []
    def getArray(self):        
        print("Enter the array values:")
        for _ in range(self.size):
            row = list(map(int, input().split()))
            self.arr.append(row)
    def displayArray(self):       
        print("\nArray elements are:\n")
        for row in self.arr:
            print(*row)
def main():
    size = int(input("Enter the size of the array: "))
    array_obj = TwoDArray(size)  
    array_obj.getArray()         
    array_obj.displayArray()    
if __name__ == "__main__":
    main()
