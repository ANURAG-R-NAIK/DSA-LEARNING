s=int(input('enter\n'))
n=int(input('enter\n'))
m=int(input('enter\n'))
if m>n:
    print(-1)
    exit(0)
k=s//7
s = s-k
i=0
if n < s*m:
    i+=1
    n=n*i
print (i+1)    
