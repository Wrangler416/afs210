class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)
    
    
class Queue: 
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []
    
    def peek(self):
        return self.items[0]


myQueue = Queue()
myStack = Stack()

s = "racecar"  

def isPalindrome(s):
 for i in s:
    myStack.push(i)
            
 reversed = ""
 while not myStack.isEmpty():
     reversed = reversed + myStack.pop()
            
 if s == reversed:
        print("true")
 else: 
        print("false")



str = "hello"

def isPalindromes(str):
    for i in str:
        myQueue.enqueue(i)
    back = ""
    while not myQueue.isEmpty():
        back = back + myQueue.dequeue()
    
    if str == back:
        print("true")
    else:
        print("false")



