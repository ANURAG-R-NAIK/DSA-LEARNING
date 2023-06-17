# # QUESTION 2 OF KUNAL PATTERN
# i = 0
# while i<6 :
#     print("*"*i)
#     i+=1

# # QUESTION 3 OF KUNAL PATTERN
# i = 5
# while i>0:
#     print("*"*i)
#     i-=1

# #QUESTION 4 OF KUNAL PATTERN
# n = 7
# for i in range (1,n):
#     for j in range (1,i):
#         print(j,end="")
#     print()

# # QUESTION 5 OF KUNAL PATTERN

n = int(10)
p = n//2

for i in range(0,p+1):
    print("* "*i)
i = p
while i>0:
    print("*"*i)
    i-=1



# QUESTION 13 OF KUNAL PATTERN
# i = 3
# j = 0
# print(" "*(i+2),"*")
# while i>0:
#     print(" "*i,"*"," "*j," "*j,"*",)
#     i-=1
#     j+=1
# print(" ","*"*(i+j))

# # coding ninjas problem

# n = 7
# while n>0:
#     for i in range(1,n+1):
#        print (i,end="")
#     print()
#     n-=1

## coding ninjas number pattern

n = 7
i = 1
j = 2 
while i<n:
    while j<n:
        print(j,end="")
        j+=1
    i+=1
    
    print()    