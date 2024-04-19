array = [2,4,6,7,9,10]

target = 9


def linearsearch(array,target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1



result = linearsearch(array,target)

print(f"element found at the index {result}")

