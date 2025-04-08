class Calculator:
    def addition(self,a, b):
        return a + b
    def subtraction(self,a,b):
        return a - b
    def multiplication(self, a, b):
        return a * b
    def division(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        else:
            return a / b
def main():
    calc = Calculator()
    
    while True:
    
        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = int(input("Enter your choice (1/2/3/4/5): "))
   
        if choice == 5:
            print("Exiting the program.")
            break
    
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
    
        if choice == 1:
            print(f"The result of addition is: {calc.addition(num1, num2)}")
        elif choice == 2:
            print(f"The result of subtraction is: {calc.subtraction(num1, num2)}")
        elif choice == 3:
            print(f"The result of multiplication is: {calc.multiplication(num1, num2)}")
        elif choice == 4:
            print(f"The result of division is: {calc.division(num1, num2)}")
        else:
            print("Invalid input! Please choose a valid operation.")

if __name__ == "__main__":
    main()
