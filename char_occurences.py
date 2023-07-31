str=input("Enter the string: ")
char=input("Enter the char to count: ")
count=0
for i in str:
    if i==char:
        count=count+1

print(f"The number of times '{char}' occured is: ",count)
