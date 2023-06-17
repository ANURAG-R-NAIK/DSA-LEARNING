# # TO FIND IF A LEAP YEAR

# year=int(input("Enter The Year"))

# if (year % 4  ==  0):
#     print("its a leap year")
# else: 
#     print("not a leap year")    

#################################

# # SUM OF TWO NUMBERS
# a=int(input("enter first number"))
# b=int(input("enter second number"))

# print(a+b)

#############################################
# # MULTIPLICATION TABLE
# a=int(input("enter the number"))
# n=int(input("enter the no. of terms"))
# i=1

# while i<n:
#     print( a,' * ', i ,' = ' ,end="" )
#     print(i*a)
#     i+=1

###################################################
 # TO FIND HCF OF TWO NUMBERS
# x=int(input("enter the first number"))
# y=int(input("enter the second number"))
# i=0
# if x>y :
#     smaller = y   # FIRST WE DEFINE WHICH AMONG IS SMALLER BECAUSE THEN WE RUN LOOP TILL THERE
# else:
#     smaller = x
# d=[]
# for i in range(1,smaller+1):
#     if((x % i ==0) and (y % i ==0)): # HERE WE CHECK IF IT DIVIDES BOTH AND KEEP UPDATING HCF
#             hcf = i
         
# print(hcf)            


################################################
# # TO FIND THE LCM OF TWO NUMBERS
# x=int(input("enter the first number"))
# y=int(input("enter the second number"))

# if x > y:
#        greater = x  #DECIDENG WHICH AMONG THEM IS GREATER
# else:
#        greater = y

# while(True):
#        if((greater % x == 0) and (greater % y == 0)):  # HERE WE ARE INCREASING GREATER AMONG BY ONE EACH TIME AND THEN 
#            lcm = greater                    #SEEING IF IT DIVIDES BOTH THE NUMBERS . IF YES THEN WE ARE BREAKING THE LOOP
#            break
#        greater += 1  #INCREMENTING THE LOOP

# print(lcm)       #RETURNING THE VALUE

###########################################################

#Keep taking numbers as inputs till the user enters ‘x’, after that print sum of all.
    
# h=[]

# for i in input():
#     if i == 'x':
       
#         break
#     h.append(int(i))
# print(sum(h))

##################################################################
#Write a program to print whether a number is even or odd, also take input from the user.

# a=int(input('enter the number'))

# if a % 2==0:
#     print('even')
    
# else:
#     print('odd')   

#####################################################

#Take name as input and print a greeting message for that particular name.

# a=input('enter the name')

# print("hello", a, "how are u")

#######################################################

#Write a program to input principal, time, and rate (P, T, R) from the user and find Simple Interest.

# p=int(input())
# t=int(input())
# r=int(input())

# print ((p*t*r)/100)
#######################################################
#Take in two numbers and an operator (+, -, *, /) and calculate the value. (Use if conditions)


# x=int(input())
# y=int(input())
# p=int(input())

# if p==1:
#     print(x+y)
# elif p==2:
#     print(x-y)
# elif p==3:
#     print(x*y)
# else:
#     print(x/y)

##############################################

#To calculate Fibonacci Series up to n numbers
# n1,n2 =0,1 # INITIALISE THE FIRST TWO TERMS OF THE SERIES
# i=0 #POINTER
# n=int(input("range")) #ENTER THE RANGE

# while i < n:
#        print(n1)  #EACH TIME IT IS PRINTING N1 VALUE 
#        nth = n1 + n2 #ADDING AND THEN UPDATING THE VALUES
#        # update values
#        n1 = n2
#        n2 = nth
#        i += 1
###################################################

#To find out whether the given String is Palindrome or not

# x=list(input('enter'))

# s= x[::-1]  #REVERSE THE LIST OF THE INPUT STRING

# i=0

# while i<len(x)-1:  #COMPARE EACH ELEMENT AND CHECK FOR EQUALITY
#     if x[i]==s[i]:
#         i+=1
#     else:
#         print("not",end="") 
#         i+=1   
# print('palindrome')

######################################################
#To find Armstrong Number between two given number

x=int(input("enter"))
sum=0 #INITIALISE SUM POINTER
temp=x #HERE WE ARE TAKING A TEMP VALUE SO IN FUTURE WELL AMKE CHANGES ON THE COPY
while temp>0 :
    m = temp % 10  #THIS GIVES US THE ONES DIGIT TERM
    sum = sum  + m**3  #APPLY THE FORMULLA
    temp = temp//10 #TAKE THE QUOTIENT AND REPEAT THE PROCESS
    
if x==sum:
    print('Armstrong Number')
    
else:
    print('not')    


