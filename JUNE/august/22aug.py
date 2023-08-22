
# s = input('enter')
# from collections import Counter
# def isIsogram(s):
#         k = Counter(s)
#         print(k)
#         for i, j in k.items():
#             if j > 1:
#                 return 0
#         return 1
    
# print(isIsogram(s))

# OOPS STARTED FRIM HERE

# class dog:
#     attr1 = "mammal"
#     attr2 = "dog"
    
#     def fun(self):
#         print("I'm a", self.attr1)
#         print("I'm a", self.attr2)  
        
# roger = dog()

# print(roger.attr1)
# roger.fun()
#-------------------------

# class person:
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def __str__(self):
#         return f"hello my name is {self.name} and my age is {self.age}"
    
# p = person('anurag', 21)
# print(p)
#----------------
 
# class dog:
    
#     animal = 'dog'
    
#     def __init__(self, breed, color):
#         self.breed = breed
#         self.color = color
        
# roger = dog('pug', 'brown')
# buzo = dog('bulldog', 'black')

# print(roger.animal)
# print(roger.breed)
# print(roger.color)


# print(buzo.animal)
# print(buzo.breed)
# print(buzo.color)

#------------------------

# RECURSION VIDEO KEYPAD NUMBER QUESTION
# TAKEN 2 STRING AS PROCESSED AND UNPROCESSED AND THEN WE KEEP  HAVING CHOICES FROM UP AND PUT IN P
# FIRST IF WE GET LEN(UP) == 0 THAT MEANS WE HAVE COMPLETED THE RECURSION CALL AND NEED TO PRINT THE VALUES
# WE CHECK FROM THE VALUES LIKE 1 - A,B,C  AND 2 - D,E,F HERE WE TAKE THE FIRST LETTER A TAKE ITS ASCII VALUE AND THEN WE ADD THE FOLLOWING DIGIT AND AFTER CONVERT BACK TO GET THE ALPHABET WE NEED
# RANGE IS LIKE FIRST 3 ALPHABETS HAVE 0 - 3 AND NEXT 3 - 5 THIS RANGE IS ((digit - 1) * 3, digit * 3))
# FOR ALL COMBINATIONS FROM THIS WE GET THE CHOICES OF THE POSSIBLE COMBINATIONS USING FOR LOOP  AND THEN ADD TO THE PROCESSED LIST
# AND THEN REMOVE FROM THE UNPROCESSED LIST
# def pad(p, up):
#     if len(up) == 0: 
#         print(p)
#         return 
    
#     digit = int(up[0])
    
#     for i in range((digit - 1) * 3, digit * 3):
#         ch = chr(ord('a') + i)      
        
#         pad(p + ch, up[1:])   
        
# pad("", "12")
  
  
# HERE WE TRY TO RETURN THE ANSWER IN THE ARRAY FORMAT      
def padarray(p, up):
    if len(up) == 0:    
        return p 
    
    digit = int(up[0])
    
    lst = []
    
    for i in range((digit - 1) * 3, digit * 3):
        ch = chr(ord('a') + i)      
        
        lst.append(padarray(p + ch, up[1:]))
        
    return lst  
    
print(padarray("", "12"))