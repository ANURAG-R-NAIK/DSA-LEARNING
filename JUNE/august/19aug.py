#  BINARY SEARCH USING RECURSION

# def search_recursion(seq, target, s, e):
    
#     if s > e:
#         return -1
    
#     m = (s + e) // 2
    
#     if seq[m] == target:
#         return m
    
#     elif seq[m] < target:
#         return search_recursion(seq, target, m+1, e)
    
#     else:
#         return search_recursion(seq, target, s, m-1)
    
# seq = [1,2,3,4,5,6]
# print(search_recursion(seq, 4, 0, 5))

# def rec_print(n):
#     if n < 1:
#         return
#     print(n)
#     rec_print(n-1)
# rec_print(4)
# print()

# def rec_printrev(n):
#     if n < 1:
#         return
#     rec_printrev(n-1)
#     print(n)
# rec_printrev(4)

# FACTORIAL OF A NUMBER

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fact(n-1)

# p = 3
# print(fact(p))

# SUM OF DIGITS OF A GIVEN NUMBER


# def sum(n):
#     if n == 0: return 0
#     return sum(n // 10) + (n%10)

# print(sum(132))

# FUNCTION TO REVERSE DIGITS OF A NUMBER

# num = 1234
# reversed_num = 0

# while num != 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10
    
# print(reversed_num)

# TO COUNT THE NUMBER OF ZEROS

# c = 0
# def count(n):
#     return helper(n,c)

# def helper(n,c):
#     if n == 0:
#         return c
    
#     else:
#         rem = n % 10
#         if rem == 0:
#             return helper(n//10, c+1)
#         else:
#             return helper(n//10,c)    
        
# print(count(12002000022))

# TO FIND IF ARRAY IS SORTED USING RECURSION
# def sorted(arr, index):
    
#     if index == len(arr) - 1:
#         return True
    
#     return ((arr[index] < arr[index +1]) and sorted(arr,index+1))

# arr  = [1,2,3,4,5]
# print(sorted(arr, 0))

# LINEAR SEARCH USING RECURSION

# def search(arr,target,index):
#     if index == len(arr) - 1:
#         return False
#     else:
#         return arr[index] == target or search(arr,target,index+1)

# arr = [1,2,3,4,5]
# print(search(arr,8,0))    
 


