class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)
    
    def isPalindrome(s):
        return s == s[::-1]

    s = "racecar"
    num1 = isPalindrome(s)
    if num1:
        print("true")
    else:
        print("false")

class Queue: 
    def _init_(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self, item):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []
    
    def peek(self):
        return self.items[0]

   
myStack = Stack()

myStack.push("e")
myStack.push("stuff")
print(myStack.pop())
print(myStack.size())
print(myStack.peek())

