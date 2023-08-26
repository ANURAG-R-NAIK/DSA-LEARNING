# n = input()

# k = str(n)
# l = len(k)
# sum = 0
# if l == 1:
#     print('true')
# else:
#     for i in range(l):
#         # print(i)
#         sum += (int(k[i]) ** l)
#         print(sum)

#     if sum == n:
#         print('true')
#     else:
#         print('false')

def sumOfAllDivisors(n: int) -> int:
    sum = 0
    for i in range(1,n+1):
        sum += helper(i)
        print(helper(i))
    
    return sum

    
    
    
def helper(n: int) -> int:
    cnt = 0
    for i in range(1,n+1):
        if n % i == 0:
            cnt += i
            # print(cnt)
    return cnt

print(sumOfAllDivisors(5))