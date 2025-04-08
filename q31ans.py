import re
def str(st):    
    pattern = r'ab+'    
    if re.search(pattern,st):
        return "Match found!"
    else:
        return "No match found."
st = input("Enter a string: ")
print(str(st))
