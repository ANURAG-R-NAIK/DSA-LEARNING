class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()
        i=0
        while i<=len(nums)-1:
            if i==len(nums)-1:
                return nums[i]
            if nums[i]==nums[i+1]==nums[i+2] :
                i=i+3
            else:
                return nums[i]  