# def fun1(n):
#     print(n)
#     return fun2(n-1)

# def fun2(n):
#     print(n)
#     return fun3(n-1)

# def fun3(n):
#     print(n)
    
# fun1(10)

# FIBONACCI NUMBER

def fib(n):
    if n < 2:
        return(n)
    return(fib(n-1) + fib(n-2))
print(fib(6))
