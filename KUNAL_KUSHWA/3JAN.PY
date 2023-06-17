#### STORE A COLLECTION OF DIFFERENT ROLL NUMBERS #########
boss = list(range(0,15))

print (boss)

############# Input a year and find whether it is a leap year or not. ############

year = int(input('enter the year'))
print(year)
if year % 4 ==0 :
    print('leap year')
    
else:
    print('not a leap year')

########## Take two numbers and print the sum of both. #######

num1 = int(input('enter the numbers'))
num2 = int(input('enter the numbers'))

print(num1+num2)

######### Take a number as input and print the multiplication table for it. ###########

mul = int(input('enter the number'))
len = int(input('enter the length'))
for i in range(1,len+1):
    print(mul,'*',i ,'=',mul*i)


######### Take 2 numbers as inputs and find their HCF and LCM ##########

num1 = int(input('enter the first number'))
num2 = int(input('enter the second number'))

k = min(num1,num2)
l = max(num1,num2)

if l % k == 0:
    print('hcf is ',k)
    
else:
    for i in range(1,k+1):
      if (num1 % i ==0 ) and (num2 % i == 0):
          hcf = i
    print('hscf is',hcf)    

########### LCM #############

num1 = int(input('enter the first number'))
num2 = int(input('enter the second number')) 

k = min(num1,num2)


for i in range(2,k+1):
      if (num1 % i ==0 ) and (num2 % i == 0):
          print('lcm is',i)
          break
             
########### Keep taking numbers as inputs till the user enters ‘x’, after that print sum of all#######
sum = 0
while(input('enter') != 'x'):
    sum = sum+int(input('enter'))
    if ValueError:
        print(sum)########## didnot complete ##########