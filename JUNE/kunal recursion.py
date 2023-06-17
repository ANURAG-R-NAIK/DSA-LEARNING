## THE FOLDER HAVING THE FILES MADE AFTER APRIL 15 HAVE ALL ERASED AS THE FOLDER GOT DELETED SOMEHOW AND RESTORING DIDNT DO ANY GOOD 
#AS I DIDNOT PUSH THE FILES I WILL RESUME FROM HERE
# IT THINK THE SEARCHING NAD SORTING PART WAS MISSED SO WILL GET THAT COVERED IN REVISION


#KUNAL RECURSION

#FIBONACCI OF A NTH NUMBER


# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)
         
# print(fib(6))

#-------------------------
# BINARY SEARCCH USING RECURSION

# seq = [1,2,3,4,5]

# s = 0
# e = len(seq) - 1
# def search(seq, n, s, e):
#     if s>e:
#         return -1
    
#     m = (e + s) // 2
    
#     if seq[m] == n:
#         return m
    
#     if n < seq[m]: 
#         # as target lies in the LHS the value lies in the first half so we need to only change the end value start remains the same        
#         return search(seq, n, s, m - 1)
    
#     return search(seq, n, m + 1, e) 
# # means it lies in the RHS of the divided seq

# print(search(seq, 3, s, e))
