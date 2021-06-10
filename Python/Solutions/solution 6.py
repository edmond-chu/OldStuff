# Change this file's name to "solution.py" before submitting.

# Implement a function to check whether a given linked list contains a cycle.
# Return true if it has a cycle and return false if it does not have a cycle.

# Note that the function will be called on the head of the linked list.
# A Node has `.val` and `.next` properties.


class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
#This algorithm traverses the array once, and uses a set to track the
#nodes visited. Using a while loop to traverse the linked list, it
#every node is checked in the set if it has been visited before. If it has,
#it returns true. Once a list is fully traversed without having a compared element
#in the set, it returnns false. This algorithm is O(n), and uses O(1) auxiliary space
def hasCycle(head: Node) -> bool:
    stor = set() #Create a set to store nodes visited
    curr = head
    while (curr): #while the node is not null, uses the while loop to traverse list
        if (curr in stor): #if the element is in the set, returns true because
                            #a cycle is present
            return True
        stor.add(curr) #adds unvisited nodes to set and moves down the list
        curr = curr.next
    return False
    #return false when it a cycle is not found
