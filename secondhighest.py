def largestsecond(num):
    if len(num) < 2:
        return None
    highest, second_highest = num[0], num[1]
    for i in num:
        if i > highest:
            second_highest = highest
            highest = i
        elif i > second_highest and i < highest:
            second_highest = i

    return second_highest

num = [3,5,7,9,8,21]

result = largestsecond(num)

print(f"second largest number is: {result}")


