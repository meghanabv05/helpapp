num1 = [1,2,3]
num2 = [4,2]
num3 = [1,4]

print(list( set(num1)&set(num2) | set(num1)&set(num3) | set(num2)&set(num3)))