class HashItem: 
    def __init__(self, key, value): 
            self.key = key 
            self.value = value 

class HashTable:
    def __init__(self):
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.count = 0

    def hashFunction(self,key):
        keystr = str(key)
        hashval = 0
        for ch in keystr:
            hashval += ord(ch)
        return (hashval* len(keystr)) % self.size
    
    def rehashFunction(self,key):
        keystr = str(key)
        hashval = 0
        counter = 0
        for ch in keystr:
            counter += 1
            hashval += ord(ch)*counter
        return (hashval* len(keystr)) % self.size
# Insert your secondary hashing function code

    def perfectHash(self, key, size):

    # Insert your hashing function code

     

     def put(self,key,data):
        item = HashItem(key, data)
        h = self.hashFunction(key)
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                break
            h = (h+1) % self.size

            if self.slots[h] is None:
                self.count += 1
                self.slots[h] = item

        # Insert your code here to store key and data 
    def get(self,key):
        h = self.hashFunction(key)
        
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                return self.slots[h].value
            h = (h+1) % self.size

            return None
        # Insert your code here to get data by key

    def __getitem__ (self,key):
        return self.get(key)

    def __setitem__ (self,key,data):
        self.put(key,data)


H = HashTable()
#H[69] = 'A'
#H[66] = 'B'
#H[80] = 'C'
#H[35] = 'D'
#H[18] = 'E'
#H[52] = 'F'
#H[89] = 'G'
#H[70] = 'H'
#H[12] = 'I'

print(H.hashFunction("John Smith"))
print(H.hashFunction("George Washington"))
print(H.hashFunction("Jane Doe"))
print(H.hashFunction("Alexander Hamilton"))


print(H.hashFunction(5))


# Store remaining input data

# print the slot values

# print the data values

# print the value for key 52

