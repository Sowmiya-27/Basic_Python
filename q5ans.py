tot= float(input("Enter your total mark: "))
if tot> 90:
    grade = "A"
elif tot>= 80:
    grade = "B"
elif tot>= 70:
    grade = "C"
elif tot>= 60:
    grade = "D"
elif tot>= 50:
    grade = "E"
else:
    grade = "Failed"
print("Your Grade is:",grade)
