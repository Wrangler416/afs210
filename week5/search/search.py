def linear_search(list, term):
    list_size = len(list)
    for i in range(list_size):
	    if term == list[i]:
		    return True
	    elif list[i] > term:
		    return False
	    return False
    
myList = [11, 30, 25, 27, 9, 19, 28, 3, 21, 17]


sortedList = [3, 10, 13, 20, 45, 67, 100]


def lin_search(list, term):
    if list[0] == term:
        return True
    else:
        return lin_search(list[1:], term)

print(lin_search(sortedList, 25))



binary search only works on ordered

binary search on sorted list

when the array is 1  = base case
use Recursion 

pass in list and target number
keep calling function 

move towards base case

dividing list 

