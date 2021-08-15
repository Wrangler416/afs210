def loop1():    
    odd_sum = 0    
    for i in range(20):        
        if (i % 2) == 1:            
            odd_sum += i    
    return odd_sum

#Sum the odd numbers between 1 and 20    

def recursion1(num, odd_sum = 0):
    if(num == 0):
        return 1
    if(num % 2) == 1:
        odd_sum += 1 
    else: 
        return (num * recursion1(num-1))

n = 20   
print(recursion1(n)) 




#Sum the even numbers between 1 and 20    

def loop2():    
    i = 0    
    even_sum = 0    
    while i < 20:        
        if (i % 2) == 0:            
            even_sum += i        
    i += 1    
    return even_sum


def recursion2(i = 0, even_sum = 0):
    if(i == 0):
        return 1
    if(i % 2) == 0:
        even_sum += i 
    else: 
        return (i * recursion2(i-1))

n = 20   
print(recursion2(n))











#def loop1Rec(num,odd_sum):    
    # Duplicate the loop1 function using recursion

# def loop2Rec(num,even_sum):    
    # # Duplicate the loop2 function using recursion