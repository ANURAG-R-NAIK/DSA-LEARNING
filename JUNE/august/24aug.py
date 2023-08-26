def cal(r, unit, arr, n):
    
    if n == 0:
         return -1
     
    totalfood = r * unit
    foodtillnow = 0
    house = 0
    
    for house in range(n):
        foodtillnow += arr[house]
        
        if totalfood > foodtillnow:
            return house + 1
    if totalfood > foodtillnow:
        return 0
    
    
r = int(input('enter the number of rate'))
unit = int(input('enter foor unit'))
arr = [int(i) for i in input('enter array').split()]
n = len(arr)

print(cal(r, unit, n, arr))
         