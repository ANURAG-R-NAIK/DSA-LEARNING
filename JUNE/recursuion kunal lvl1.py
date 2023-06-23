# n = 5

# def pr(n):
#     if n == 0:
#         return #this break the resursion loop   
#     print(n) #prints the value and then calls the next reduced value
#     pr(n - 1)
# pr(n)

# #-----------------
# n = 5

# def pr(n):
#     if n == 0:
#         return #this break the resursion loop   
#     pr(n - 1) # here the last recusrion loop will first calculate for 1 and print it and then move further as follows.
#     print(n)
# pr(n)
#--------------------------
# FACTORIAL OF A NUMBER

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else :
#         return  n * fact(n-1) 

# print(fact(5))

#-------------------------------
# SUM OF DIGITS OF A NUMBER

# w/o recursion
# n = 1342
# k = str(n)
# count = 0
# for i in range(len(k)):
#     count += int(k[i])
# print(count)

#-----

def sum(n):
    if n == 0:
        return 0
    return (n%10) + sum(n//10)     
#here n%10 gives the last digit of the number here that is 2
# then n gets updated to n//10 that is 134, Gin keep repeating the procedure till we add all the numbers

print(sum(1342))