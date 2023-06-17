# some gibberish value will be given as string we have to check if this is a palindrome or not..

# s=input("enter the string")
# s=str(s) 
# r=s[::-1]

# print(r)      

# nums=input("enter the list")   
# n=len(nums)
        
# for i in range(0,n-1):
#             count=0
#             for j in range (i+1,n):
#                 if nums[i]==nums[j]:
#                     count=count+1
                  
        
# if (count>(n/2)):
#     print (nums[i])
        
        # n=set(nums)
        
        # for i in n:
        #     if nums.count(i)>len(nums)/2:
#         #         return i
# nums=input("enter a list")

# s=[[0]*nums.count(0)+[1]*nums.count(1)+[2]*nums.count(2)]
# r=
# print(s)

# class Solution:
#     def defangIPaddr(self, a: str) -> str:
#         k=list(a.split('.'))
#         k.join('[.]')
# #         return k
# temp=0
# a=[1,2,3,4]

# a[2]=temp
# print(temp)

class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        res = [''] * len(s)
        for i in range(len(s)):
            res[indices[i]] = s[i]
        return ''.join(i for i in res)