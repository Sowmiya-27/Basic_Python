class Student:
    pass
student1 = Student()
student2 = Student()
student3 = Student()
student1.name = input("Enter name of Student 1: ")
student1.age = int(input("Enter age of Student 1: "))
student2.name = input("Enter name of Student 2: ")
student2.age = int(input("Enter age of Student 2: "))
student3.name = input("Enter name of Student 3: ")
student3.age = int(input("Enter age of Student 3: "))
print(f"\nStudent 1: Name = {student1.name}, Age = {student1.age}")
print(f"Student 2: Name = {student2.name}, Age = {student2.age}")
print(f"Student 3: Name = {student3.name}, Age = {student3.age}")
