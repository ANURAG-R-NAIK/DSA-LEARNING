#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

#Notice that the solution set must not contain duplicate triplets.
nums=list(input('enter'))
n=len(nums)

k=[]

for i in range (n-2):
            for j in range(i+1,n-1):
                for k in range (j+1,n):
                    if (nums[i] + nums[j] + nums[k] == 0)  :

                        l=[ nums[i],nums[j],nums[k] ]
                        j=k+l
                  