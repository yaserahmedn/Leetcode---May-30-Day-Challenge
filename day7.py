#In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

#Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

#We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

#Return true if and only if the nodes corresponding to the values x and y are cousins.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        queue=[(root,0,-1)]
        flag=False
        x_node=None
        y_node=None
        while(len(queue)>0):
            temp=queue.pop(0)
            node,level,parent=temp[0],temp[1],temp[2]
            if node.left:
                queue.append((node.left,level+1,node.val))
            if node.right:
                queue.append((node.right,level+1,node.val))
                
            if x==node.val:
                x_node=temp
            if y==node.val:
                y_node=temp
                
            if x_node and y_node:
                if x_node[1]==y_node[1] and x_node[2]!=y_node[2]:
                    flag=True
                    break
                
        return flag
        
