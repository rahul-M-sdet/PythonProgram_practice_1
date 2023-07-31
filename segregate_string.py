def segregate_char_num_special(string):
    chars=[]
    nums=[]
    specials=[]
    for i in string:
        if i.isalpha():
            chars.append(i)
        elif i.isdigit():
            nums.append(i) 
        else:
            specials.append(i)

    return chars,nums,specials


input_str="!@#123wer"

char_list,nums_list,special_list= segregate_char_num_special(input_str)

print("char in the list is :",''.join(char_list))
print("nums in the list: ",''.join(nums_list))
print("special_char in the list: ",''.join(special_list))