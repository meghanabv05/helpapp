def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
                arr[i], arr[min_index] = arr[min_index], arr[i]


arr = [7,5,63,1,90,5]

selectionsort(arr)

print(arr)

