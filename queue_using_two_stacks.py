'''
Queue using two Stacks

Implement a Queue using 2 stacks s1 and s2 .
A Query Q is of 2 Types
(i) 1 x (a query of this type means  pushing 'x' into the queue)
(ii) 2   (a query of this type means to pop element from queue and print the poped element)

Note :- If there is no element return -1 as answer while popping.

Example 1:

Input:
5
1 2 1 3 2 1 4 2

Output: 
2 3
'''

#Function to push an element in queue by using 2 stacks.
def Push(x,stack1,stack2):
    stack1.append(x)

#Function to pop an element from queue by using 2 stacks.
def Pop(stack1,stack2):
    value=-1
    
    length=len(stack1)
    if length==0:
        return value
        
    while length>1:
        stack2.append(stack1.pop())
        length-=1
    
    value=stack1.pop()
    
    while stack2!=[]:
        stack1.append(stack2.pop())
    return value
        
