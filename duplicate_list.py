my_list=[1,2,3,4,5,2,3,6]
uni=[]
dup=[]
for ele in my_list:
    if ele not in uni:
        uni.append(ele)
    elif ele not in dup:
        dup.append(ele)
print(uni)
print(dup)