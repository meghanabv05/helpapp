dict1 = {"name":"megha", "profession":"engineer"}

print(len(dict1))






for i,j in dict1.items():
    print(i,j)


dict2 = dict1


print(dict1)

dict2 = dict1.copy()

print(dict2)


dict2["age"] = 24

print(dict2)