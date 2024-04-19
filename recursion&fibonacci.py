def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))



def fib(n):
    a = 0
    b = 1
    if n<=1:
        return n
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a+b
            a = b
            b = c
            print(c)

fib(5)