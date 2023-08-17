# LINKED LISTS

#  creating a node in LL
# class node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        
# node1 = node(7)
# print(node1.data)
# print(node1.next)

# # creating a class of singly LL

# class singly:
#     def __init__(self):
#         self.head = None
        
# # ############################# traversal through singly LL
class node:
    def __init__(self, data):
        self.data = data
        self.next = None        
class sll:
    def __init__(self):
        self.head = None
        
    def traversal(self):
        if self.head is None:
            print('singly linked list is empty')
            
        else:
            a = self.head
            while a is not None:
                print(a.data, end = " ")
                a = a.next  
                
    def insert_at_begi(self,data):
        print()
        nb = node(data)
        nb.next = self.head
        self.head = nb        
    def inser_at_end(self, data):
        print()
        ne = node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne 
        
    def insert_at_specified(self, posi, data):
        print()
        self.data = data
        np = node(data)
        a = self.head
        for i in range(1, posi - 1):
            a = a.next
        np.next = a.next
        a.next = np
        
    def deletion_at_begi(self):
        print()
        a = self.head
        self.head = a.next
        a.next = None
        
    def deletion_at_end(self):
        print()
        prev = self.head
        a = prev.next
        
        while a.next is not None:
            a = a.next
            prev = prev.next
        prev.next = None
        
    def deletion_at_speci(self, posi):
        print()
        prev = self.head
        a = prev.next
        for i in range(1, posi - 1):
            a = a.next
            prev = prev.next
        prev.next = a.next
        



            
n1 = node(5)
ann = sll()
ann.head = n1
n2 = node(10)
n1.next = n2
n3 = node(15)
n2.next = n3
n4 = node(20)
n3.next = n4
ann.traversal()
ann.insert_at_begi(2)
ann.traversal()
ann.inser_at_end(25)
ann.traversal()
ann.insert_at_specified(3,22)
ann.traversal()
ann.deletion_at_begi()
ann.traversal()
ann.deletion_at_end()
ann.traversal()
ann.deletion_at_speci(3)
ann.traversal()