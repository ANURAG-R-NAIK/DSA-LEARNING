# # 1. Execute the given function.
# # def differenceofSum(n.m)

# # The function takes two integrals m and n as arguments. You are required to obtain the total of all integers ranging between 1 to n (both inclusive) which are not divisible by m. You must also return the distinction between the sum of integers not divisible by m with the sum of integers divisible by m.


# # def differenceofSum(n,m):
# #     no = 0
# #     yes = 0
# #     for i in range(1, n+1):
# #         if i % m == 0:
# #             yes += i
# #         else:
# #             no += i
# #     return max(no,yes) - min(no,yes)

# # print(differenceofSum(10,3))

# #---------------------------

# # 2. Execute the given function.
# # def LargeSmallSum(arr)

# # The function takes an integral arr which is of the size or length of its arguments. Return the sum of the second smallest element at odd position ‘arr’ and the second largest element at the even position.
        
        
# def LargeSmallSum(arr):
#     k = sorted(arr)
#     s = 0
#     odd = []
#     even = []
#     for i in range(0,len(arr),2):
#         odd.append(arr[i])
#     for i in range(1,len(arr),2):
#         even.append(arr[i])
    
#     for i in range(len(k) - 1,0,-1):
#         if k[i] in even and k[i] != max(arr):
#             s += k[i]
#     for i in range(len(k)) and k[i]!=min(arr):
#         if k[i] in odd:
#             s += k[i]
#     print(s)
        
    
    
# LargeSmallSum([3,2,1,7,5,4])
    
#--------TELEGRAM QUESTIONS ACCENTURE-------------
# x = int(input("enter the first number"))
# y = int(input('enter second number'))

# if x < 10000 and x > -10000 and y < 10000 and y > -10000:
#     print(x+y)
# else:
#     print(-1)


# x = input('enter the number')

# lst = list(x)
# cnt = 0
# max = 0
# # print(cnt)

# l = ['p', '*']
# n = ['#']
# if x[-1] == '*' and x[-2] != '#':
#     cnt += 1
# if x[0] == '*' and x[1] != '#':
#     cnt += 1
#     # print(cnt)
# for j in range(1,len(x) - 1):
#     if x[j] == '*':
#         if x[j+1] in l and x[j-1] in l:
#             cnt += 1
#             # print(cnt, 'f')
        
#-------------------------    
# for i in range(len(lst)):
#     if lst[i] == '*':
#         cnt += 1
#     elif lst[i] == '#':
#         cnt = 0
#     else:
#         max = cnt
#         cnt = 0
# max += cnt
# print(max)
    
#-----------------------

# k = [int(i) for i in input().split()]

# s = list(set(k))

# if len(s) == 1:
#     print(s[0], -1)
# else:
#     l = sorted(s)
#     print(l[-1], l[-2])

#------------------------------

# k = [int(i) for i in input().split()]
# x = int(input('enter'))
# print(k.index(x))

#--------------------

# str = input('enter the string  -- ')
# cnt = 0

# s = str.lower()
# for i in range(len(s) - 1):
#     if s[i] == 'a' and s[i+1] == 'm':
#         cnt += 1
# print(cnt)
    
#-------------------------

# def find(x, y):
#     k = x * y
#     i = 2
#     while i*i <= k:
#         if k % (i*i) == 0:
#             return min((k // (i*i)), i*i)
            
#         i += 1
#     return (k)

# x = int(input('enter the length'))
# y = int(input('enter the breadth'))
# print(find(x, y))

#--------------------------

# x = float(input('enter the ph value'))

# if x>7:
#     print('alkaline')
# elif x<7:
#     print('acidic')
# else:
#     print('neutral')

#----------------------

# def c(x):
    
#     if x < 248:
#         return(0)
#     cnt = 0
#     for i in range(247, x):
#         m,n,o = 0,0,0
    
#         k = str(i)
#         for i in k:
#             if int(i) == 2:
#                 m+=1
#             elif int(i) == 4:
#                 n += 1
#             elif int(i) == 8:
#                 o += 1
#         if m == n == o and m > 0:
#             cnt += 1
#     return cnt

# x = int(input('enter'))
# print(c(x))

#---------------------------

# n = int(input('enter the lines'))

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j%2, end = " ")
#     print()

#--------------------------

# str = input('enter the string')
# lst = list(str)

# sp = []
# d = []
# for i in lst:
#     if i.isdigit():
#         d.append(i)
#     elif not i.isalnum():
#         sp.append(i)
        
# k = ''
# for i in range(len(min(sp, d))):
#     k += d[i]
#     k += sp[i]
#     k+= (max(sp,d)[len(min(sp,d))])
# print(k)
#-------------------------------

# x = input('enter the string')

# i = int(x[0])

# for i in range(1, len(x) - 1, 2):
#     if x[i] == 'A':
#         i = i & int(x[i+1])
#     elif x[i] == 'B':
#         i = i | int(x[i+1])
#     elif x[i] == 'C':
#         i = i ^ int(x[i+1])
        
# print(i)

#-------------------

# r = int(input('enter r'))
# unit = int(input('enter the unit'))
# arr = [int(i) for i in input().split()]

# n = len(arr)
# total = r * unit
# sum = 0

# if n == 0:
#     print(-1)
# for i in range(len(arr)):
#     sum += arr[i]
#     if sum >= total:
#         print(i+1)
#         break
#-----------------------------

# def CheckPassword(char):
#     di,cap = 0,0
#     lst = list(char)
    
#     if char[0].isdigit():
#         return 0
#     if len(lst) < 4:
#         return 0
#     for i in lst:
#         if i.isdigit():
#             di+=1
#         elif i.isalpha():
#             if i.isupper():
#                 cap += 1
#         elif i == '/' or i == ' ':
#             return 0
#     if di>=1 and cap>=1:
#         return 1
    
# k = input('enter')
# print(CheckPassword(k))

#----------------------

# def findCount(arr,length,num,diff):
#     cnt = 0
#     for i in arr:
#         if i in range(num-diff, num+diff+1):
#             print(i)
#             cnt +=1
#     return cnt

# arr = [int(i) for i in input('enter').split()]
# length = len(arr)
# num = int(input('enter the number'))
# diff = int(input('enter the diff'))

# print(findCount(arr,length, num,diff))


#------------------------------

# def differenceofSum(n, m):
#     l = []
#     d = []
#     for i in range(1, m+1):
#         if i % n == 0:
#             d.append(i)
#         else:
#             l.append(i)
#     print(d)
#     print(l)
#     return sum(l) - sum(d)

# n = int(input('enter the number'))
# m = int(input('enter the number'))
# print(differenceofSum(n ,m))

#------------------------------------

# def LargeSmallSum(arr):
#     odd = []
#     even = []
#     for i in range(0, len(arr),2):
#         odd.append(arr[i])
#     for i in range(1, len(arr), 2):
#         even.append(arr[i])
#     if 0 in odd:
#         odd.remove(0)
#     elif 0 in even:
#         even.remove(0)
#     return sorted(odd)[1] + sorted(even)[-2]
        
# arr = [int(i) for i in input('enter').split()]
# print(LargeSmallSum(arr))


#--------------------------------------

# arr = [int(i) for i in input('enter').split()]
# sum = int(input('enter the num'))

# def find(arr, sum):
#     if len(arr)<2:
#         return 0
#     k = sorted(arr)
#     for i in range(len(k) - 1):
#         if arr[i] + arr[i+1] <= sum:
#             return arr[i] * arr[i+1]
#     return -1

#-------------------------------------


# QUESTION 8 - didnot understand


#---------------------

# def MoveHyphen(str,n):
#     l = ''
#     cnt = 0
#     for i in str:
#         if i == '-':
#             cnt += 1
#         else:
#             l += i
#     return '-'*cnt + l

# str = input('enter the string')
# n = len(str)
# print(MoveHyphen(str,n))

#-----------------------


# def NumberOfCarries(num1 , num2):
#     car = 0
#     s1 = str(num1)
#     s2 = str(num2)
#     cnt = 0
    
    
#     for i in range(len(min(s1, s2)) - 1,0,-1):
#         if int(s1[i]) + int(s2[i]) + car > 9:
#             car= 1
#             cnt += 1
#         else:
#             car = 0
            
#     return cnt

# num1 = int(input('enter the num1 -- '))
# num2 = int(input('enter the num2 -- '))
# print(NumberOfCarries(num1, num2))
            
            
#---------------------------

# def ReplaceCharacter(Char,n,ch1,ch2):
#     a = ch2
#     b = ch1
#     lst = list(Char)
    
#     for i in range(len(lst)):
#         if lst[i] == a:
#             lst[i] = b
#         elif lst[i] == b:
#             lst[i] = a
#     # print(lst)
#     return "".join(lst)

# c = input('enter the string')
# ch1 = input('enter the char1')
# ch2 = input('enter the char2')
# n = len(c)
# print(ReplaceCharacter(c,n,ch1,ch2))   

#----------------------------

# def OperationChoices(c, a, b):
#     if c == 1:
#         return a+b
#     elif c == 2:
#         return a - b
#     elif c == 3:
#         return a*b
#     elif c == 4:
#         return a / b
#     else:
#         print('invalid literal')
# a = int(input('enter a'))    
# b = int(input('enter b'))  
# c = int(input('enter the num - '))
# print(OperationChoices(c,a,b))

#---------------------------------

# def MaxExponents(a,b):
#     cnt = 0
#     maxi = 0
#     for i in range(a, b+1):
#         while i % 2 == 0:
#             i = i // 2
#             cnt += 1
#         maxi = max(cnt, maxi)
#     return maxi

# a = int(input('enter a'))
# b = int(input('enter b'))
# print(MaxExponents(a,b))
        
#---------------------

# def Calculate(m, n):
#     cnt = 0
    
#     for i in range(m, n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             cnt += i
#     return cnt
# m = int(input('enter the num'))
# n = int(input('enter the num'))
# print(Calculate(m, n))

#------------------------

# n = int(input('enter the size'))
# l = []
# i = 0
# while i < n:
#     x = int(input('enter the num'))
#     l.append(x)
#     i += 1
# e = []
# o = []
# for i in range(len(l)):
#     if i % 2 == 0:
#         e.append(l[i])
#     else:
#         o.append(l[i])
# e.sort()
# o.sort()
# print(e[-2] + o[-2])

#-----------------------

# x1, y1 = 1,1
# x2, y2 = 2,4
# x3, y3 = 3,6
# f = ((x1-x2)**2 + (y1-y2)**2)**0.5
# g = ((x1-x3)**2 + (y1-y3)**2)**0.5
# k = ((x3-x2)**2 + (y3-y2)**2)**0.5
# print(f+g+k)

        
    