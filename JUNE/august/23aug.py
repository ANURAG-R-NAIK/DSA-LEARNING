# class animal:
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def __str__(self):
#         return f" hello i am a dog named {self.name} and my age is {self.age}"
    
# roger = animal('roger', 12)
# print(roger)


# CLASS AND INSTANCE VARIABLE DIFFERENCE
# class MyClass:
#     class_var = "Class Variable"  # Class variable

#     def __init__(self, instance_var):
#         self.instance_var = instance_var  # Instance variable


# # Accessing class variable
# print(MyClass.class_var)  # Output: Class Variable

# # Creating instances and accessing instance variables
# obj1 = MyClass("Instance Variable 1")
# obj2 = MyClass("Instance Variable 2")

# print(obj1.instance_var)  # Output: Instance Variable 1
# print(obj2.instance_var)  # Output: Instance Variable 2



# CLASS AND INSTANCE VARIABLE DIFFERENCE
# class dog:
    
#     animal = "dog"
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
# roger = dog('roger', 18)
# ronnni = dog('ronnni', 18)

# print(dog.animal) # class variable
# print(roger.name) # instance variable
# print(ronnni.age)


# EXAMPLE FOR DEFAULT CONSTRUCTOR
# class anurag:
    
#     def __init__(self):
#         self.geek = "anurag"
        
#     def print(self):
#         print(self.geek)
        
# obj = anurag()

# obj.print()

# PARAMETERISED CONSTRUCTOR

# class addition:
    
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
    
#     def display(self):
#         print("sum is = ", self.cal)
        
#     def cal(self):
#         self.cal =  self.num1 + self.num2
        
# ob1 = addition(2,3)
# ob1.cal()
# ob1.display()
        
    
# # DESTRUCTOR

# class employee:
    
#     def __init__(self):
#         print('employee created')
        
#     def __del__(self):
#         print('employee deleted')
        
# ob1 = employee()
# del ob1

# # DSA
# arr = [int(i) for i in input("enter").split()]

# maxlen = 0
# sum = {}
# for i in range(len(arr)):
#     sum += arr[i]
    
#     if sum == 0:
#         maxlen = i+1
        
#     key = str(sum)
    
#     sum[key] = sum.get(key, 0) + 1
    
#     for i, j in sum.items():
#         if len(j) > 1:
#             max = v[len(v) - 1] - v[0]
#             maxlen = max(maxlen, max)
            
#     print(maxlen)