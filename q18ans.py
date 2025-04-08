written = float(input("Enter the marks scored in Written Test: "))  
lab = float(input("Enter the marks scored in Lab Exams: "))  
assign = float(input("Enter the marks scored in Assignments: "))  
grade = (written * 0.70) + (lab * 0.20) + (assign * 0.10)  
print(f"Grade of the student is {grade:.1f}")  

