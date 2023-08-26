# 1. Execute the given function.
# def differenceofSum(n.m)

# The function takes two integrals m and n as arguments. You are required to obtain the total of all integers ranging between 1 to n (both inclusive) which are not divisible by m. You must also return the distinction between the sum of integers not divisible by m with the sum of integers divisible by m.


# def differenceofSum(n,m):
#     no = 0
#     yes = 0
#     for i in range(1, n+1):
#         if i % m == 0:
#             yes += i
#         else:
#             no += i
#     return max(no,yes) - min(no,yes)

# print(differenceofSum(10,3))

#---------------------------

# 2. Execute the given function.
# def LargeSmallSum(arr)

# The function takes an integral arr which is of the size or length of its arguments. Return the sum of the second smallest element at odd position ‘arr’ and the second largest element at the even position.
        
        
def LargeSmallSum(arr):
    k = sorted(arr)
    s = 0
    odd = []
    even = []
    for i in range(0,len(arr),2):
        odd.append(arr[i])
    for i in range(1,len(arr),2):
        even.append(arr[i])
    
    for i in range(len(k) - 1,0,-1):
        if k[i] in even and k[i] != max(arr):
            s += k[i]
    for i in range(len(k)) and k[i]!=min(arr):
        if k[i] in odd:
            s += k[i]
    print(s)
        
    
    
LargeSmallSum([3,2,1,7,5,4])
    