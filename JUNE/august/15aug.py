# def bsearch(seq,k,l,r):
    
#     if (r-l) == 0:
#         return False
#     mid = (r + l) // 2
#     if k == seq[mid]:
#         return True
#     elif k > seq[mid]:
#         return bsearch(seq,k,mid+1,r)
#     else:
#         return bsearch(seq,k,l,mid)
    
# seq = [2,3,4,5,6]
# print(bsearch(seq,8,0,4))


# def linear(seq,k):
#     for i in range(len(seq)):
#         if seq[i] == k:
#             return seq.index(k)
#     return False
# seq = [1,2,3,4,5]
# print(linear(seq,5))

# def search(str,l):
#     if len(str) == 0:
#         return False
#     else:
#         for i in range(len(str)):
#             if str[i] == l:
#                 return True
#         return False
# str = "hello world"
# l = 'w'
# print(search(str,'p'))

# BINARY SEARCH

# def bsearch(seq,x):
#     start, end = 0, len(seq) - 1
    
#     while (start<=end):
#         mid = start + (end - start) // 2
        
#         if x < seq[mid]:
#             end = mid - 1
#         elif x > seq[mid]:
#             start = mid + 1
#         else:
#             return mid
#     return -1

# seq = [1,2,3,4,5,6,7]
# print(bsearch(seq, 8))
    
# BOTH ASCENDING AND DESCENDING BINARY SEARCH
    
# def increase(seq,x):
#     start, end = 0, len(seq) - 1
    
#     while (start <= end):
#         mid = (start) + (end - start) // 2
        
#         if x > seq[mid]:
#             start = mid + 1
#         elif x < seq[mid]:
#             end = mid - 1
#         else:
#             return mid
#     return -1

# def decrease(seq, x):
#     start,end = 0, len(seq) - 1
    
#     while start <= end:
#         mid = start + (end - start) // 2
        
#         if x > seq[mid]:
#             end = mid - 1
#         elif x < seq[mid]:
#             start = mid + 1
#         else:
#             return mid
#     return -1

# def search(seq, x):
#     if seq[0] > seq[-1]:
#         return decrease(seq,x)
#     else:
#         return increase(seq, x)
    
# seq = [1,2,3,4,5,6]
# seq2 = [6,5,4,3,2,1]
# x = 4

# print(search(seq,x))
# print(search(seq2,x))
    
# FINDING SQUARE ROOT OF A NUMBER

# def square(x):
#     start, end = 1, x
    
#     while start <= end:
#         mid = (start + (end - start) // 2)
        
#         if mid*mid == x:
#             return mid
#         elif mid*mid > x:
#             end = mid - 1
#         else:
#             start = mid + 1
        
#     return end

# x = 99
# print(square(x))


# def ceiling(seq,x):
#     start, end = 0, len(seq) - 1
    
#     while start <= end:
#         mid = start + (end - start) // 2
        
#         if x == seq[mid]:
#             return mid
    
#         elif x > seq[mid]:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return end

# seq = [1,3,5,7]
# x = 4
# print(ceiling(seq,x))    
    
    
# MATRIX SEARCHING

# def search(seq,x):
#     row, col = 0, len(seq) - 1
    
#     while row < len(seq) and col >= 0:
#         if seq[row][col] == x:
#             return [row,col]
#         elif seq[row][col] < x:
#             row += 1
#         else:
#             col -= 1
#     return [-1, -1]

# seq = [[1,2,3],[4,5,6],[7,8,9]]
# x = 4
# print(search(seq, x))
        
        
# arr = input('enter')
# x = int(input('enter sum'))

# i = 0
# j = 0
# summ = 0
# cnt = 0


# for i in range(len(arr)):
#     summ += arr[i]
    
#     while summ > x:
#         summ - arr[j]
#         j += 1
        
#     if summ == x:
#         cnt += 1
# return cnt
        
        
# BUBBLE SORT

# def selection(seq):
#     for start in range(len(seq)):
#         for i in range(start, len(seq)):
#             if seq[i] < seq[start]:
#                 seq[start],seq[i] = seq[i],seq[start]
                
#     return seq

# seq = [4,3,2,1]
# print(selection(seq))

# BUBBLE SORT


        