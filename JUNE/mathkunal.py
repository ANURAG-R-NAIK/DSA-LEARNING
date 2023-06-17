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