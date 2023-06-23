# TO FIND IF A NUMBER IS EVEN OR ODD

# n = int(input('enter the number'))

# if n & 1 == 1:
#     print("odd")
# else:
#     print("even")

#------
# Q. ONLY ONE NUMBER APPEARS IN THE ARRAY ONCE THAN THE REST
# seq = [1, 1, 2, 2, 3, 3, 4, 4, 5]

# for i in seq:
#     if seq.count(i) == 1:
#         print(i)

#----

# d = {}
# for i in seq:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)
# for i in d:
#     if d[i] == 1:
#         print(i)

#------
# by using the xor operation on all elements of the list the individual bit remains idle rest become zero
# a = seq[0]
# for i in range(1,len(seq)):
#     a = a ^ seq[i]
# print(a)

#-----------
# Q. to find the ith bit of a given number

# for that bit we will and with 1 for that we will shift one by (i-1) bits 
# n = 39
# # 100111
# i = 3
# print(n & (1<<(i-1)))
# # 4 - 100

#----
# Q. for setting the ith bit of a number

# # for this we will or that bit with the left shifted 1
# n = 39
# # 100111
# i = 4
# n = n | (1<<(i-1))
# print(n)
# # 47 - 101111

#----
# Q. for reseting the bit of a number

# for this we will and with all ones except that bit for this we will take the complement of the previous mask
# x = 1 ^ (1 << (i - 1)) any bit ^ with one gives it complement

#----
# Q. to find the rightmost set bit

# n = 39

# k = n&(-n)

# print(k)

#-----

# Q. Magic number to the power of 5 question

# n = 3
# res = 0
# base = 5
# while n > 0:
#     lastbit = n &  1 #gives the last bit of the number
#     n = n >> 1 #right shift to get the next bit of the number
#     res += lastbit * base #base is 5 powers so multiply by the lastbit
#     base = base * 5  # doing the powersof 5 updating the base
# print(res)
    
# -----

# this gives the  number of digits required to represent the number n in the base of b
# import math
# n = 10
# b = 2

# ans = int(math.log(n) / math.log(b)) + 1
# print(ans)

#---
# Q. to find the power of a number

# base = 3
# power = 6
# res = 1

# while power>0:
#     if (power&1) == 1: #measn that is a set bit
#         res *= base # multiply with the base and multiply to result
#     base *= base #update base
#     power = power >> 1 #again right shift foe the next bit
# print(res)

#-----

# Q.count the number of set bits

# n = 10
# cnt = 0
# while n>0:
#     k = n & (-n) # gives the first et bit
#     if k>0:
#         cnt += 1 # increment cnt
#     n -= (n & (-n)) #remove that set bit
# print(cnt)


#-----
# XOR o f numbers from 0 can be given as , a be the number
''' a % 1 = 0  xor is a
 a % 1 = 1  xor is 1
 a % 1 = 2  xor is a + 1
 a % 1 = 3  xor is 0
'''
    
#------
# XOR of 2 number beteween two ranges
# xor from a to b is equal to 
# xor from 0 to b aored with with xor from 0 to a 

#----
# Q. flipping an image in leetcode question

# image = [[1,1,0],[1,0,1],[0,0,0]]

# for row in image:
#     row.reverse()
# for row in image:
#     for ele in row:
#         ele = 1
        
# print(image) # NOT COMPLETED

#-------------------------------------------------------------------------------------------------------------------
# VIDEO 2

#prime number
# k = int(input('enter the num'))

# for i in range(2, k):
#     if k % i == 0:
#         print('not prime')
#     else:
#         print('prime')

#-----
#prime number

# k = int(input('enter the number'))

# if k <= 1:
#     print(False)
    
# c = 2
# while (c * c) <= k:
#     if k %c == 0:
#         print(False)
#     c+=1

#-----

