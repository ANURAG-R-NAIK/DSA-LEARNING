# GCD(7,63)

# def gcd(a,b):
#     l1= []
#     l2= []
#     max = 0
#     for i in range(1,a+1):
#         if a % i ==0:
#             l1.append(i)
#     for j in range(1,b+1):
#         if b % j == 0:
#             l2.append(j)
#     for i in l1:
#         if i in l2:
#             max = i
#     return max             

# print(gcd(7,63))

# def gcd(a,b):
#     max = 0
#     for i in range(1,min(a,b)+1):
#         if (a%i) == 0 and (b%i) == 0:
#             max = i
#     return max

# print(gcd(7,63))

# def gcd(a,b):
#     i = min(a,b)
#     while i>0:
#         if a%i == 0 and b%i == 0:
#             return i
#         else:i_=1

# print(gcd(7,63))   

#euclids algorithm  

# def gcd(a,b):
#     if a>b:
#         (a,b) = (b,a)
        
#     if a%b == 0:
#         return b
#     else:
#         return gcd(a,a%b)

# print(gcd(7,63))     

## FACTORIAL OF A NUMBER


# def fact(x):
#     if x <= 0:
#         return(1)
#     else:
#         k = x * fact(x-1)
#         return(k) 
        
# print(fact(10))


## FACTORS OF A NUMBER N

# n = int(input("enter"))
# k = []
# for i in range(1,n):
#     if (n%i) == 0:
#         k.append(i)
# print(k)       
    