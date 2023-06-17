# Q1

# class Solution:
#     def buildArray(self, nums: List[int]) -> List[int]:
#         ans = []
#         for i in range(0,len(nums)):
#             ans.append(nums[nums[i]])

#         return ans

# Q2

# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         ans = []
#         ans += (nums+nums)
#         return ans

# Q3

# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         sums = 0
#         runningSum = []
#         for i in range(0,len(nums)):
#             sums += nums[i]
#             runningSum.append(sums)
#         return runningSum

# Q4

# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         max_balue = 0
#         ind_value = 0
#         for i in range(len(accounts)):
#             ind_value = sum(accounts[i])
#             if ind_value > max_balue:
#                 max_balue = ind_value
#         return max_balue

# Q5

# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         result = []
#         for i in range(n):
#            result += [nums[i],nums[i+n]]
#         return result

# Q6

# class Solution:
#     def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
#         k = []
#         for i in candies:
#             k.append((i + extraCandies) >= max(candies))
               
#         return k

# Q7

# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         result = 0
        
#         for i in range(0,len(nums)):
#             for j in range(i+1,len(nums)):
#                 if(nums[i] == nums[j]) and (i<j):
#                     result +=1
#         return result

# Q8

# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         l=len(nums)
#         ans=[]
#         count=0
#         for i in nums:
#             for j in range(l):
#                if (nums[j]-i)<0:
#                    count+=1
#             ans.append(count)
#             count=0
#         return ans
    
# Q9

# class Solution:
#     def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]: 
#         t = []
#         for i in range(len(nums)):
#             t.insert(index[i], nums[i])
#         return t

# Q10
##ERROR
# sentence = input('enter')
# if len(sentence) > 1:
#             for i in sentence:
#                 k = (sentence.count(i) == 1 )
#             return k
#         else:
#             return "false"
##ERROR       
# # k = list(sentence)
# # l = set(k)
# # m1 = len(l)
# # m2 = len(k)
# # if (m1-m2) != 0:
# #     print('false')
# # else:
#     print('true')

#######CORRECT ONE###
# class Solution:
#     def checkIfPangram(self, sentence: str) -> bool:
#         return (len(set(sentence)) == 26)

# Q11 
# class Solution:
#     def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
#         count = 0
#         if ruleKey == 'type':
#             for i in range(len(items)):
#                 if items[i][0] == ruleValue :
#                     count += 1
#         elif ruleKey == 'color':
#             for i in range(len(items)):
#                 if items[i][1] == ruleValue :
#                     count += 1
#         elif ruleKey == 'name':
#             for i in range(len(items)):
#                 if items[i][2] == ruleValue :
#                     count += 1
#         return count


# Q12
# class Solution:
#     def largestAltitude(self, gain: List[int]) -> int:
#         k = []
#         c = 0
#         for i in gain:
#             c+=i
#             k.append(c)

#         if max(k)>=0:
#             return max(k)
#         else: return 0

# Q13
#ERROR ANS DIDNT GET
# for i in image:
#             for j in range(len(i)):
#                 if i[j] == 0:
#                     i[j] = 1
#                 else:
#                     i[j] = 0
#         return image

# Q14
