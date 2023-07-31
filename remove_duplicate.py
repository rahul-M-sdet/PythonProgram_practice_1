str="Hello"
result=''
for char in str:
    if char not in result:
        result=result+char
print(result)