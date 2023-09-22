
# class person(object):
    
#     def __init__(self, name):
#         self.name = name
        
#     def getname(self):
#         return self.name
    
#     def isemp(self):    
#         return False
    
# class emp(person):
    
#     def isemp(self):
#         return True
    
# ob1 = person("g1")
# ob2 = emp('g2')

# print(ob1.getname(), ob1.isemp())
# print(ob2.getname(), ob2.isemp())

######################################################


class person(object):
    
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def display(self):
        print(self.name)
        print(self.id)
        
    
    
class emp(person):
    
    def __init__(self, name, id, salary, post):
        self.salary = salary
        self.post = post
        
    
person.__init__(self, name, id)

a = emp('anurag', 222222, 20000000, "intern")

a.display()