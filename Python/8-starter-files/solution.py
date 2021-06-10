
#Tree class
class TreeNode:  
    def __init__(self, data):  
        self.val = data  
        self.left = None
        self.right = None
"""
Write a function that takes a binary search tree, and two integers, Min and Max,
and returns a binary search tree with elements outside of the 
range [Min, Max] (inclusive) removed.
"""
def removeOutsideRange(root, Min, Max): 
 
