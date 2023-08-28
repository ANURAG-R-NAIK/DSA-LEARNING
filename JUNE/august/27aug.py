# from typing import *

# def alternateNumbers(a : List[int]) -> List[int]:
#     # Write your code here.
#     f = []
#     n = []
#     p = []
#     for i in a:
#         if i > 0:
#             p.append(i)
#         else:
#             n.append(i)
#     l = len(min(p,n))
#     i = 0
#     print(p)
#     print(n)
#     while l > 0:
#         f.append(p[i])
#         f.append(n[i])
#         i += 1
#         l -= 1
#     f.extend(max(p,n)[l:])

#     return f
# nums = [int(i) for i in input().split()]
# print(alternateNumbers(nums))

    
    
from typing import *

def superiorElements(a : List[int]) -> List[int]:
    # Write your code here.
    k = []
    n = len(a)


    k.append(a[-1])

    for i in range(n):
        print(max(a[i:]))
        print(a[i])
        print('---')
        if max(a[i:]) <= a[i]:
            # print(max(a[i:]))
            k.append(a[i])
    return sorted(k)

a = [int(i) for i in input().split()]

print(superiorElements(a))
