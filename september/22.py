# APNA COLLEGE ARRAY DSA SHEET

# Q 18 NEXT PERMUTATION

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        leng = len(nums)

        if leng <= 2:
            return nums.reverse()
            # as the next perm for the two numbers is just the rev of the numbers

        # we create a pointer to check the descending pattern

        point = leng - 2

        while point >= 0 and nums[point] >= nums[point + 1]:
            point -= 1

        if point == -1:
            return nums.reverse()
            # if the nums has the last iteration of the seq then we just return the reverse or the first element of the seq
            #321 -- 123

        for x in range(leng - 1, point, -1):
            if nums[point] < nums[x]:
                nums[point], nums[x] = nums[x], nums[point]   
                break
                # we found the end of the descending pattern and we exchange the values 

        nums[point + 1:] = reversed(nums[point + 1:])     