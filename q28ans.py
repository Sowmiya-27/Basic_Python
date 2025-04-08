st=input("Enter a string: ")
fre={}
for i in st:
    if i in fre:
        fre[i] += 1
    else:
        fre[i] = 1    
print(fre)
