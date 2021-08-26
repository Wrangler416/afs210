class Stack:
    def __init__(self):
        self.items = []
 
    def isEmpty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
 
 
s = Stack()
text = "racecar"
 
for char in text:
    s.push(char)
 
str2 = ''
while not s.isEmpty():
    str2 = str2 + s.pop()
 
if text == str2:
    print("true")
else:
    print("false")

def isPalindrome():
    