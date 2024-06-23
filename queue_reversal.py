'''
Queue Reversal (GFG)

Given a Queue Q containing N elements. The task is to reverse the Queue. Your task is to complete the function rev(), that reverses the N elements of the queue.

Example 1:

Input:
6
4 3 1 10 2 6
Output: 
6 2 10 1 3 4
Explanation: 
After reversing the given elements of the queue , the resultant queue will be 6 2 10 1 3 4.
'''

class Solution:
    #Function to reverse the queue.
    def rev(self, q):
        list1=[]
        lengthx=q.qsize()
        
        while not q.empty():
            list1.append(q.get())
            #lengthx-=1
            
        while list1!=[]:
            q.put(list1.pop())
            
        return q
