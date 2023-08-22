
# PRINTITNG OATTERN
# # def pattern(r,c):
#     if r == 0:
#         return
    
#     if c < r:
#         print('*', end = " ")
#         pattern(r, c+1)
#     else:
#         print()
#         pattern(r-1, 0)

# pattern(5, 0)

# TO REMOVE A CHAR FROM A GIVEN STRING
# def string(seq, index, k):
#     if index == len(seq) - 1:
#         print(k)
#         return
#     else:
#         if seq[index]  != 'a':
#             k += seq[index]
#         string(seq, index+1,k)
        
    

# seq = 'abcdaaddbb'
# string(seq, 0, '')
# # print(seq[0])

# # SKIP AN SUBSTRING

# def skip_substring(seq):
    
#     def skip(p = '', up):
#         print(p)
#         return
    
#     ch = up[0]
    
#     if ch == 'a':
#         skip(p, up[1:])
#     else:
#         skip(p+ch, up[1:])
        
#     def skipapple(up):
#         if len(up) == 0:
#             return ""
        
        
#         if up.startswith('apple'):
#             return skipapple(up[5:])
#         else:
#             return up[0] + skipapple(up[1:])
        
# up = 'helloworldskipapple'
# skip_substring(up)
        
# TO PRINT ALL THE SUBSTRING OF A STRING

# def sub(p,up):
#     if len(up) == 0:
#         print(p)
#         return

#     ch = up[0]
#     up = up[1:]
#     sub(p + ch, up)
#     sub(p, up)
    
# sub('','abc')

# TO RETURN IN ARRAY FORMAT

# def sub(p,up):
#     if len(up) == 0:
#         newlst = []
#         newlst.append(p)
#         return newlst

#     ch = up[0]
#     up = up[1:]
#     left = []
#     right = []
#     left = sub(p + ch, up)
#     right = sub(p, up)
#     left.extend(right)
#     return left
    
# print(sub('','abc'))
    
    
# TO FIND THE SUBSETS OF AN ARRAY

# def sublists(lst):
#     n = len(lst)
#     sublists = []
     
#     for start in range(n):
#         for end in range(start + 1, n + 1):
#             sublists.append(lst[start:end])
     
#     return sublists

# print(sublists([1,2,3]))

#PERMUTATION OF THE STRING VALUES

def perm(p, up):
    if len(up) == 0:
        print(p)
        return 
    
    ch = up[0]
    # print(ch)
    
    
    for i in range(0, len(p)+1):
        f = p[0:i]
        # print(f)
        s = p[i:len(p)]
        # print(s)
        l = up[1:]
        # print(l) 
        perm(f + ch + s, l)

perm('', 'abc')

         

        
    