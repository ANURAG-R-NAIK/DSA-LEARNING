# def last_index(arr, x):
#     for i in range(len(arr) - 1, 0, -1):
#         if arr[i] == x:
#             print(i)
#             break
            
# arr = [1,3,2,3,4,5,6,6]
# last_index(arr, 3)
#using for loop for finding the last index of occurance

#############using recursion to find the last index

# def last_index(seq, x, index):
#     if index == 0:
#         return -1
#     if seq[index] == x:
#         return (index)
#     else:
#         return last_index(seq, x, index - 1)
    
# arr = [1,3,2,3,4,5,6,6]
# print(last_index(arr, 3, len(arr) - 1))

# -----BY PASSING A NEW LIST EVERY TIME TO FIND THE OCCURANCES

# def array(seq, x, index):
#     k = []
    
    
#     if index == len(seq):
#         return k

#     if seq[index] == x:
#         k.append(index)
        
#     m = array(seq, x, index+1)
    
#     if len(m)>0:
#         k.append(m)
    
#     return k

# arr = [1,3,2,3,4,5,6,6]
# print(array(arr, 3, 0))

#---------- PRINTING PATTERN USING RECURSION

# def pattern(r, c):
#     if r== 0:
#         return
#     if c < r:
#         print('*', end = " ")
#         pattern(r, c+1)
#     else:
#         print()
#         pattern(r-1, 0)
        
# pattern(4,0)

