#!/bin/python3




# Complete the reverseArray function below.
def reverseArray(a):
    b = []
    
    for i in range(len(a)-1, -1, -1):
        b.append(a[i])
    return b


a = [1, 2, 3, 4]
res = reverseArray(a)
print(res)
        
        
        
    

