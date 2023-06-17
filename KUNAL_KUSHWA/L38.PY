# class animals():
#     def __init__(self, name, age , color):
        
#         self.name = name
#         self.age = age
#         self.color = color
        
        
# tom = animals("Cat", 3, "Black")
# jerry = animals("Rat", 4, "Brown")

# print("tom is a {}".format(tom.name))


######## INHERITANCE ##########

def Animal():
    def __init__(self):
        print('animal is created')
        
    def name(self):
        print("animal")
        
    def do(self):
        print("runs")       
        
        
#child classs
        
class cat(Animal):
    def __init__(self):
        super().__init__()
        print(" cat is created  ")
                
    def name(self):
        print("cat") 
        
    def jumps(self):
        print("meow")        
        
        
        
k = cat()       

