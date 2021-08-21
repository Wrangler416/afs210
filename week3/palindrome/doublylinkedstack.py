# Stacks and Queues


class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None 
        self.prev = None

class Stack1:
     def __init__(self):
         self.head = None

     def push(self, data):
         if self.head is None:
             self.head = Node(data)
         else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

     def pop(self):
         if self.head is None:
             return None
         elif self.head.next is None:
             temp = self.head.data
             self.head = None
             return temp
         else:
             temp = self.head.data
             self.head = self.head.next
             self.head.prev = None
             return temp
         
     def size(self):
         temp = self.head
         count = 0

         while temp is not None:
            count = count + 1
            temp = temp.next
         return count 

     def isEmpty(self):
         if self.head is None:
             return True
         else:
             return False

     def peek(self):
         return self.head.data

     def printAll(self):
         print("stack consists of:")
         temp = self.head
         while temp is not None: 
             print(temp.data, end= "->")
             temp = temp.next





myStack = Stack1()

myStack.push("e")
myStack.printAll()
