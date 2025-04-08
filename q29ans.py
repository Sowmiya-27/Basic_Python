def repch(s):
    fchar = s[0]   
    s = fchar + s[1:].replace(fchar, '$')
    return s
str1=input("Enter a string: ")
res=repch(str1)
print(f"Modified string: {res}")
