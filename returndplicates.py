def find_duplicates(arr):
    n = len(arr)
    duplicates = []
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                duplicates.append(arr[j])
    return duplicates

arr = [2, 3, 3, 6, 2, 9]
print(find_duplicates(arr))



