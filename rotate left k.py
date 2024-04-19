def rotatearray(num,k):
    n = len(num)
    k = k%n

    reverse(num,0,k-1)
    reverse(num,k,n-1)
    reverse(num,0,n-1)


def reverse(num,start,end):
    while start < end:
        num[start], num[end] = num[end], num[start]
        start += 1
        end -= 1

array = [1,2,3,4,5,6,7,8,9]
steps = 3
print("before reverse:", array)
rotatearray(array,steps)
print("after reverese:", array)

