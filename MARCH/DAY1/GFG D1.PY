###Given an integer array arr of size n, you need to sum the elements of arr

# def sumElement(arr,n):
#     sum = 0
#     for i in arr:
#         sum += i
#     return sum

## gfg pattern problem
N = 5
for x in range(N,0,-1):
            #space
            for y in range(N-x):
                print(" ",end="")
            #star
            for z in range(x):
                print("*",end="")
            
            print()