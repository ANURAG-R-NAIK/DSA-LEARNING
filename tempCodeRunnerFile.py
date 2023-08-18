def createSequence(n):

    def fine(n):
        k = str(n)
        print(k)
        for i in k:
            print(i)
            if int(i) != 2 or int(i) != 5:
                return False
        return True

        
    l = []
    for i in range(n+1):
        if fine(i):
            l.append(i)
    return l
        
x = int(input('enter'))
print(createSequence(x))

