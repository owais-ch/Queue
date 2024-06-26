'''
Rotate Deque By K

Given a Deque deq of size N containing non-negative integers and a positive integer K, the task is to rotate elements of the deque by K places in a circular fashion. There will be two rotations which you have to implement depending on the type rotating query. Below is the description of rotating type and value of K for which you have to rotate in circular way:
Type-1. right_Rotate_Deq_ByK(): this function should rotate deque by K places in a clockwise fashion.
Type-2. left_Rotate_Deq_ByK(): this function should rotate deque by K places in an anti-clockwise fashion.

Example 1:

Input:
6
1 2 3 4 5 6
1 2

Output: 
5 6 1 2 3 4 
'''

def left_Rotate_Deq_ByK(deq,k):
    arr=[]
    
    i=0
    
    while i<k:
        arr.append(deq.popleft())
        i+=1
        
    while arr!=[]:
        deq.append(arr.pop(0))
    
    return deq
 
#Function to rotate deque by k places in clockwise direction.   
def right_Rotate_Deq_ByK(deq,k):
    length=len(deq)
    
    deq2=deque()
    
    i=0
    
    while i<k:
        deq2.append(deq.pop())
        i+=1
        
    while deq2!=deque():
        deq.appendleft(deq2.popleft())
    return deq
