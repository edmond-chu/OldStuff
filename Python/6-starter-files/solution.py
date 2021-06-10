# Change this file's name to "solution.py" before submitting.

# Implement a function to check whether a given linked list contains a cycle.
# Return true if it has a cycle and return false if it does not have a cycle.

# Note that the function will be called on the head of the linked list.
# A Node has `.val` and `.next` properties.
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def hasCycle(head: Node) -> bool:
