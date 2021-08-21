class Node:
    # A doubly-linked node.
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        return
    
    def hasValue(self, value):
        if self.data == value:
            return True
        else:
            return False

class DoublyLinkedList:
    # A doubly-linked list.
    def __init__(self):
        # Create an empty list.
        self.tail = None
        self.head = None
        self.count = 0

    def iter(self):
        # Iterate through the list.
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

# Returns the number of elements in the list

    def size(self) -> int:
        return self.count

# Append a node
    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None
            
            self.count += 1

# Add a node at the front of the list

    def addFirst(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

# Add a node at the end of the list

    def addAtEnd(self, data):
        newNode = Node(data)
        if not self.head:
           self.head = newNode
           self.tail = newNode
        else: 
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1


    def addAtIndex(self, data, index):
        start = self.head
        for i in range(self.count):
           if(start.data == data):
            return i 
           start = start.next
        return None

        # Add a node to the list at the given index position
        # If index equals to the length of linked list, the node will be appended to the end of linked list
        # If index is greater than the length, the data will not be inserted.
        # This function does not replace the data at the index, but pushes everything else down.

# Search through the list. Return the index position if data is found, otherwise return -1       



    def indexOf(self, value):
        current = self.head
        position = 0
       
        while current is not None:
            if current.data == value:
                return position

            current = current.next
            position += 1

        return -1


    def add(self, data) -> None:
        # Append an item to the end of the list
        self.addLast(data)

    def clear(self) -> None:
        # Remove all of the items from the list
        self.head = None
        self.tail = None
        self.count = 0

    def addAtIndex(self, newElement, position):
        newNode = Node(newElement)
        if(position < 1):
            print("position needs to be greater than 1")
        elif (position == 1):

            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        else:
            temp = self.head
            for i in range(1, position-1):
                if(temp != None):
                    temp = temp.next
        if(temp !=None):
            newNode.next = temp.next
            newNode.prev = temp
            temp.next = newNode

            if(newNode.next != None):
                newNode.next.prev = newNode
        else: 
            print("previous node is null")


# Delete the node at the index-th in the linked list, if the index is valid.
        
    def deleteAtIndex(self, index):

        if (index > (self.count-1)):
            return
            
        curr = self.head
        prev = self.head

        for n in range(index):
            prev = curr
            curr = curr.next
            
        prev.next = curr.next
        curr.prev = prev
        self.count -= 1

        if (curr == self.head):
            self.head = curr.next
            curr.prev = None
        elif (curr == self.tail):
            prev.next = None
            self.tail = prev       

        return

    def delete(self, data) -> None:
# Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = prev
                self.count -= 1
                return
            prev = current
            current = current.next

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value

    def __str__(self):
        myStr = ""
        for node in self.iter():
             myStr += str(node)+ " "
        return myStr


    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


list = DoublyLinkedList()

list.append("May")
list.append("the")
list.append("force")
list.append("be")
list.append("with")
list.append("you")
list.append("!")


list.indexOf("with")


print(list)


