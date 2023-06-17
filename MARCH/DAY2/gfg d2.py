#Given an array Arr of N positive integers. Your task is to find the elements whose value is 
# equal to that of its index value ( Consider 1-based indexing ).

n = int(input("enter n"))
arr = input("enter array")

k = list(arr)
for i in range(1,len(k)):
    if k[i] == n:
        print(i) 