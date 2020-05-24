#Construct Binary Search Tree from Preorder Traversal
#Solution
#Return the root node of a binary search tree that matches the given preorder traversal.

#(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

#It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

#Example 1:

#Input: [8,5,1,7,10,12]
#Output: [8,5,10,1,7,null,12]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def makeTree(root, value):
            if root:
                if root.val>value:
                    if root.left:
                        makeTree(root.left,value)
                    else:
                        root.left=TreeNode(value)
                        
                else:
                    if root.right:
                        makeTree(root.right,value)
                    else:
                        root.right=TreeNode(value)

     
        root=TreeNode(preorder[0])
        for i in range(1,len(preorder)):
            makeTree(root,preorder[i])
            
        return root
