input_str="Python Programming"
str=[]
for w in input_str:
    if w not in str:
        str.append(w)
    else:

        print(f"{w} repeated more then ones")
