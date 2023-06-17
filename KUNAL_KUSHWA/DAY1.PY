##############    Flow of Program - Flowcharts & Pseudocode   ###############3

# salary= int(input('enter the salary'))

# if salary>10000:
#     salary+=2000
# else :
#     salary+=1000
    
# print(salary)

################TO FIND IF GIVEN A NO. IS PRIME OR NOT#############

# number = int(input('enter the no.'))
 
# if number % 2 ==0:
#     print("not prime")

# else:
#     for i in range (2,number):
#         if number % i == 0:
#             print("not prime")
        
#     else:
#         print("prime")    

####     IN THIS PROGRAM WE NEED NOT SEE AFTER THE NUMBER HAS COMPLETED CHECKING TILL THE SQUARE ROOT OF THE NNUMBER
    ###  SO THE COMPLEXITY CAN BE  REDUCED TO HALF OF THE PRESENT
    
number = int(input('enter the no.'))
 
if number % 2 ==0:
    print("not prime")

else:
    i=2
    k=i*i
    while k<= number:
        if number % i == 0:   ## NOW COMPLEXITY IS REDUCED TO SQUARE ROOT OD=F THE PRESENT
            print("not prime")
        k += 1
    else:
        print("prime") 