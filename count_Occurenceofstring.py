def count_occurences(strinA,stringB):
    return strinA.count(stringB)

stringA="qwertyuiopiopiopu"
stringB="iop"

occurences=count_occurences(stringA.lower(),stringB.lower())

print(f"'{stringB}' repeated in '{stringA}' is :{occurences} times")


# print((stringA.count(stringB)))
