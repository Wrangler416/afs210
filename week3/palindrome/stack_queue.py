class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

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

# """ def isPalindrome(word):
#     if len(word) < 2: return True
#     if word[0] != word[-1]: return False
#     return isPalindrome(word[1:-1])

#     return True """



def isPalindrome(str):
    str = myStack.push("noon")
    rev_str = myStack.pop()
    if str == rev_str:
        print(True)
    else: 
        print(False)
   
print(isPalindrome(str))  
   
   # if myStack.pop() == myQueue.dequeue():
    

      
