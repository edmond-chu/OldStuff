
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



#This program removes the elements in the range of min and max within a BST
#It runs in O(n) time, where n is the number of nodes, and is O(1) complexity
def removeOutsideRange(root, Min, Max):
    if root == None:
        return None
    #operates on the left subtree and the right subtree of the root
    root.left = removeOutsideRange(root.left,Min, Max)
    root.right = removeOutsideRange(root.right, Min, Max)
    #Next, since the root hasn't been operated on, returns the left or righttree
    #depending on the root value
    if root.val < Min:
        righttree = root.right
        return righttree
    if root.val > Max:
        lefttree= root.left
        return lefttree
    return root
