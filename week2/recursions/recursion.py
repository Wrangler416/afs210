def loop1():    
    odd_sum = 0    
    for i in range(20):        
        if (i % 2) == 1:            
            odd_sum += i    
        return odd_sum

#Sum the odd numbers between 1 and 20    

def recursion1(i, odd_sum):
    if i >= 20:
        return odd_sum
    elif (i % 2) == 1:
         odd_sum += i  
    return recursion1(i+1, odd_sum)

i = 0   
odd_sum = 0
print(recursion1(i, odd_sum)) 


#Sum the even numbers between 1 and 20    

def loop2():    
    i = 0    
    even_sum = 0    
    while i < 20:        
        if (i % 2) == 0:            
            even_sum += i        
    i += 1    
    return even_sum


def recursion2(i, even_sum):
    if i >= 20:
        return even_sum
    elif(i % 2) == 0:
        even_sum += i  
    return recursion2(i+1, even_sum)

i = 0
even_sum = 0   
print(recursion2(i, even_sum))


#def loop1Rec(num,odd_sum):    
    # Duplicate the loop1 function using recursion

# def loop2Rec(num,even_sum):    
    # # Duplicate the loop2 function using recursion