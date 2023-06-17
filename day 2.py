# TO FIND IF THE ELEMENT HAS A COPY INSIDE THE ARRAY AND RETURN TRUE IF THERE
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        nums.sort()
        for i in range (0,len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
                i+=1