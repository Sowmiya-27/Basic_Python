str= [{'name': 'John', 'age': 10}, {'name': 'Doe', 'age': 20}, {'name': 'Michael', 'age': 15}]
sort_str = sorted(str, key=lambda str:str['age'])
print(sort_str)
