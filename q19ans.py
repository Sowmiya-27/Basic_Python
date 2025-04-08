n=float(input("Enter the annual income:"))
if(n<=250000):
 print("No income tax")
elif(n>250000 and n<=500000):
 print("Income tax=",n*0.05)
elif(n>500000 and n<=1000000):
 print("Income tax=",n*0.2)
elif(n>1000000 and n<=5000000):
 print("Income tax=",n*0.3)


