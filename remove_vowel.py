str="Hello"
vowels="a,e,i,o,u,A,I,O,U"
without_vowels=''
for i in str:
    if i not in vowels:
        without_vowels +=i

print(without_vowels)