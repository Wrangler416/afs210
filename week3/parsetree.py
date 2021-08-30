import print_tree

class Node:
    def __init__ (self, value, left=None, right=None, parent=None):
        self.val = value
        self.left = left
        self.right = right
        self.parent = parent
        
    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
    
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
        
root = Node("")

def buildParseTree(exp):
    explist = exp.split()
    myStack = Stack()
    currentNode = root

    for expression in explist:
        print(expression)
        newNode = Node("")
   
        if expression == '(':
           currentNode.left = newNode
           myStack.push(currentNode)
           currentNode = currentNode.left
        #if current token is ( then add a new node as the left child and then descend to that child
        elif expression == ')':
            if(myStack.size() > 0):
                currentNode = myStack.pop()
        # go up to the parent of the currentNode

        elif expression in '+-*/':
            currentNode.val = (expression)
            currentNode.right = newNode
            myStack.push(currentNode)
            currentNode = currentNode.right
            # set value of the currentNode to that operator
            # create a node and make it the right child of the currentNode
            # then descend to that right child

        elif expression not in '+-*/':
            currentNode.val = eval(expression)
            currentNode.parent = myStack.pop()
            currentNode = currentNode.parent

            # expression is a number
            # set value of the currentNode to that number
            # go back up to our parent
                
                
        else:
            raise ValueError("Unknown Operator: " + expression)


# in order
def inOrder(node):
    if node:
        inOrder(node.left)
        print(node.val)
        inOrder(node.right)
      
#post order
def postOrder(node):
    if node:
        postOrder(node.left)
        postOrder(node.right)
        print(node.val)

# pre order
def preOrder(node):
    if node:
        print(node.val)
        preOrder(node.left)
        preOrder(node.right)


buildParseTree("( ( 11 * 2 ) + ( 10 - 2 ) )")
print_tree.print_tree(root)
inOrder(root)  
postOrder(root)
preOrder(root)