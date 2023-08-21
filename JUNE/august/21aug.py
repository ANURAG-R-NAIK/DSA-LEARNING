
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

# SKIP AN SUBSTRING

def skip_substring(seq):
    
    def skip(p = '', up):
        print(p)
        return
    
    ch = up[0]
    
    if ch == 'a':
        skip(p, up[1:])
    else:
        skip(p+ch, up[1:])
        
    def skipapple(up):
        if len(up) == 0:
            return ""
        
        
        if up.startswith('apple'):
            return skipapple(up[5:])
        else:
            return up[0] + skipapple(up[1:])
        
up = 'helloworldskipapple'
skip_substring(up)
        

    