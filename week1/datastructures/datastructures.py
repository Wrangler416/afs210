# Data type one is a TUPLE

Data1 = (7, False, "Apple", True, 7, 98.6)

#Data1 - Count the number of items
print(len(Data1))

#Data1 - Find the value of the third item stored in the data set
print(Data1[3])

#Data1 - Count the number of times 7 appears
print(Data1.count(7))


# Data type 2 is a SET

Data2 = {"July", 4, 8, "Tango", 4.3, "Bingo"}

#Data2 - Remove a random element from the data set
randomItem = Data2.pop()
print(Data2)

#Data2 - Add "Alpha" to the data set
Data2.add("Alpha")
print(Data2)

#Data2 - Print data set
print(Data2)


#Data 3 is a LIST

Data3 = ["A", 7, -1, 3.14, True, 7]

#Data3 - Print the data set in reverse order
Data3.reverse()
print(Data3)

#Data3 - Change the second value in the data set to ‘B’
Data3[1] = "B"
print(Data3)

#Data3 - Remove the last item and print the data set
Data3.remove(7)
print(Data3)


#Data type 4 is a DICTIONARY

Data4 =  {
    "name": "Joe",  
    "age": 26,  
    "active": True,  
    "hourly_wage": 14.75}

#Data4 - Change "active" to False

Data4.update({"active": False})
print(Data4)

#Data4 - Add "address" with a value of "123 West Main Street"
Data4.update({"address": "123 West Main Street"})
print(Data4)

#Data4 - Print the weekly salary for Joe if he worked a full 40 hour week.
salary = Data4["hourly_wage"] * 40 
print(salary)

#Data4 - Print the data set
keys = Data4.keys()
for key in keys: 
    print('"%s" : "%s" ' % (key, Data4.get(key)), end=",")




#In a Set, items are unordered, unindexed and do not allow duplicate values.

#Unordered means that the items in a set do not have a defined order.

#This means that items in a Set can appear in a different order every time you use them, and cannot be referenced by an index or key.

#Sets cannot have two items with the same value.

#A Set is created by placing a sequence of values separted by a comma inside curly brackets {}


#Tuple items are ordered, unchangeable, and allow duplicate values.

#Tuple items are indexed with the first item having an index of [0], the second item has an index of [1] etc.

#The Tuple is unmutable (ie: unchangeable), meaning that we can not change, add, and remove items in a tuple after it has been created.

#A Tuple may contain multiple different DataTypes include integers, strings, floats, booleans, lists and objects

#Tuples are created by placing a sequence of values separated by a comma inside round brackets ()



#Dictionaries are used to store data in key:value pairs where the keys must be unique.

#A dictionary is a collection which is ordered, as of Python version 3.7, changeable (mutable) and does not allow duplicate key values.

#Storing a value using a key that is already in use, results in the old value being replaced with the new value.

#A Dictionary is created by placing a sequence of keys:values pairs, separted by a comma, inside curly brackets {}

#If you are familiar with Javascript, the notation of key:value pairs should be familiar to you as they are similar to JSON data format.