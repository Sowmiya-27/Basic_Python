import math
class Area:
    def circle(self, r):
        return math.pi * r* r
    def square(self, s):
        return s*s
    def rectangle(self, l, b):
        return l* b
    def triangle(self, base, h):
        return 0.5 * base * h
class MyClass(Area):
    def main(self):
        while True:
            print("\nEnter your choice:")
            print("1. Circle")
            print("2. Square")
            print("3. Rectangle")
            print("4. Triangle")
            print("5. Exit")
            choice = int(input())
            if choice == 1:
                r = float(input("Enter the radius: "))
                print(f"Area of the circle is: {self.circle(r):.2f}")

            elif choice == 2:
                s= float(input("Enter the length: "))
                print(f"Area of the square is: {self.square(s):.2f}")

            elif choice == 3:
                l= float(input("Enter the length: "))
                b= float(input("Enter the breadth: "))
                print(f"Area of the rectangle is: {self.rectangle(l,b):.2f}")

            elif choice == 4:
                base = float(input("Enter the base: "))
                h= float(input("Enter the height: "))
                print(f"Area of the triangle is: {self.triangle(base,h):.2f}")

            elif choice == 5:
                print("Exiting the program.")
                break

            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    obj = MyClass()
    obj.main()
