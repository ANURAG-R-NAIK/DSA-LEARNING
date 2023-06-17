#Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

#We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

#You must solve this problem without using the library's sort function.

nums=input('enter the list')
i=0
start=0
end=len(nums)-1

while i<=end: 
    if nums[i]==2:
         a[i], a[end] = a[end], a[i]
    elif  nums[i]==1:
            i+=1
    elif nums[i]==0:
            a[start], a[i] = a[i], a[start]
            i+=1  
            start+=1  
print(nums)           