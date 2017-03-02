'''
Created on 2 Mar 2017

@author: ezng
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #left child and right subtree last left child can be the answer
        result = sys.maxint;
        if(root.left!=None):
            node = self.findLastRight(root.left)
            result=min(root.val - node.val, result)  
            result=min(result, self.getMinimumDifference(root.left))     
        if(root.right!=None):
            node = self.findLastLeft(root.right)
            result=min( node.val-root.val, result)
            result=min(result, self.getMinimumDifference(root.right))
        
        return result;
        
    def findLastLeft(self, node):
        if(node.left==None):
            return node;
        else :
            return self.findLastLeft(node.left)
    def findLastRight(self, node):
        if(node.right==None):
            return node;
        else :
            return self.findLastRight(node.right)    
            
    class TreeNode(object):
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None