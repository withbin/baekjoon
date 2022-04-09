#fibonacci
def fibonacci(n):
    if(n<=1):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

#factorial
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
#hanoi tower
a=int(input())
def move(n,start,end):
    if n==1:
        print(start,end)
        return
    move(n-1,start,6-start-end)
    print(start, end)
    move(n-1,6-start-end,end)

print(2**a-1)
move(a,1,3)
