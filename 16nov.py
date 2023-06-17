# swapping two numbers using addition and sun..
# a=int(input("enter 1st"))
# b=int(input("enter 2nd"))

# a=a+b
# b=a-b
# a=a-b
# print(a,b)
##############
#using mult. and div.

# a=int(input("enter 1st"))
# b=int(input("enter 2nd"))

# a=a*b
# b=a/b
# a=a/b
# print(a,b)

########################
#GIVE THE NUMBER OF ITEMS TO BE SWAPPED AND THEN SWAP THE TWO NUMBERS ENTERED

# r=int(input('enter range'))
# i=0
# while i< r:
#         a=int(input('enter first number'))
#         b=int(input('enter second number'))
#         a,b = b,a
#         print(a,b)
#         i+=1

###############################################

#BINARY SEARCH (IT IS APPLICABLE TO SORTED ARRAYS ONLY)

# x=input('enter the list')
# a=int(input('enter the number to be found'))


# n=len(x)

# low=0
# high=n-1

# while low<=high:
#     mid=(low+high)/2
    
#     if(x[mid]<a):
#         low= mid +1
        
#     elif (x[mid]>a):
#         high= mid-1
        
#     else:
#         print(x[mid])    

####################################

# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:

# -1: Your guess is higher than the number I picked (i.e. num > pick).
# # 1: Your guess is lower than the number I picked (i.e. num < pick).
# # 0: your guess is equal to the number I picked (i.e. num == pick).
# # Return the number that I picked.

# class Solution:
#     def guessNumber(self, n: int) -> int:
#         s = 1
#         e = n+1
#         while s+1<e:
#             mid = (s+e)//2
#             if guess(mid)>=0:
#                 s = mid
#             else:
#                 e = mid
#         return s

#########################################################################

# #INCREASING TRIANGLE
# a=int(input('enter the rows'))


# i=1

# while i<a+1:
#     print (i*'*')
#     i+=1

#############################################################3

#DECREASING TRIANGLE

# a=int(input('enter the range'))



# while a>0:
#      print (a*'*')
#      a = a - 1

#####################################################

#INCREASING TRIANGLE WITH NUMBERS

# n=int(input('enter the range'))
# i=1
# for i in range(n):
#     for  j in range(i+1):
#         print(j+1,end="")
#     print()    

##############################

n=int(input('enter the range'))
i=1
for i in range(n):
    for j in range (i+1):
        j * print(j+1)        
    print()    