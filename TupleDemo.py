# Tuples are immutable we cannot change the value.

tup1 = (10,20, "Rahul",True,1,1,1,2,2,2)
tup2 = "Rahul"
print(len(tup1))
print(tup1)
print(tup1[1])
print(tup1.count(1))  # True is bydefault as 1 thats why return 5
print(tup1.count(2))
print(tup1.index(2))
print(tup1)
print(tup1[-1])
print(tup1[-2])
print(tup1[0:4])
print(tup1[1:5])
print(tup1[-1:-4:2])
print(type(tup1))

print("********************")

l1 = list(tup1)  # converted tuple into list
print(l1)

s1 = set(tup1)          # converted tuple into set
print(s1)



