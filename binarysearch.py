def binarysearch(array,target):
    low, high = 0, len(array)-1

    while low <= high:
        mid = (low+high)//2
        mid_element = array[mid]
        if mid_element == target:
            return mid
        elif mid_element < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


array = [2,4,6,7,9,10]

target = 2

result = binarysearch(array,target)

print(f"element found at the index {result}")
