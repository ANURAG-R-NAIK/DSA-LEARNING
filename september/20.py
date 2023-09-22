def find(nums):
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        print(d)
        for i,j in d.items():
            print(j)
            if j > 1:
                return True
        return False

nums = [2,14,18,22,22]
print(find(nums))