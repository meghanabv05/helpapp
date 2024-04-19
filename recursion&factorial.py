"""import sys


print(sys.setrecursionlimit(2000))

i = 0

def recursion():
    global i
    i += 1
    print("hello, i")

    recursion()


recursion() """


def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)


result = fact(5)
print(result)



def fact_with_loop(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
result = fact(5)
print(result)






