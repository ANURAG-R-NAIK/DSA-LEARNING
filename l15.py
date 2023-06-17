
# def fib(n):
    
#     if n<0:
#         print("incorrect input")
    
#     elif n==0:
#         return 0
    
    
#     elif n==1 or n==2:
#         return 1
#     else:
#          return fib(n-1)+fib(n-2)
    
# n=int(input("enter the no. of values"))
# print(fib(n))

def Fibonacci(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
    
print(Fibonacci(9))