""" sets are unordered and cannot contain duplicates use curly brackets"""



my_set = {1,2,4,5,2,4}

print(my_set)


print(len(my_set))

for i in my_set:
    print(i)




my_set.discard(1)

print(my_set)




my_set.clear()

my_set.add(6)

print(my_set)

my_set.update([6,5])

print(my_set)



print(my_set[2])






