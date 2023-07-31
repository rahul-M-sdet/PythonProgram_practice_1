input_str=input("Enter the string: ")
count=0
list1=['a','e','i','o','u','A','E','I','O','U']
for char in input_str:
    if char in list1:
        count=count+1
print("The number of vowels in string is", count)