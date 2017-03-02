'''
Created on 28 Feb 2017

@author: ezng
'''

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if(root==None) :
            return None
        if(key==root.val) :
            if(root.left == None and root.right==None) :
                return None
            elif(root.left == None) :
                return root.right
            elif (root.right == None):
                return root.left
            else :
                newRoot = self.findSmallestLeafFromRight(root, root.right)
                newRoot.left = root.left
                newRoot.right =  root.right
                root=None
                return newRoot          
        elif (key>root.val) :
            if(root.right!=None) :
                self.removeNode(root, root.right, key)   
                return root
        elif (root.left!=None) :
            self.removeNode(root, root.left, key)   
            return root 
        else :
            return root     
     
    def removeNode(self, parent , node, key):
        if (node.val == key):
            if(node.left==None and node.right==None):
                if(parent.val>key):
                    parent.left = None
                else :
                    parent.right = None
            elif(node.left==None):
                if(parent.val>key):
                    parent.left = node.right
                else :
                    parent.right = node.right  
            elif(node.right==None) :
                if(parent.val>key):
                    parent.left = node.left
                else :
                    parent.right = node.left            
            else:
                newNode = self.findSmallestLeafFromRight(node, node.right)   
                newNode.left=node.left
                newNode.right= node.right             
                if(parent.val > key):
                    parent.left = newNode
                else :
                    parent.right =newNode     
                
                node=None             
        elif(node.val > key):
            if(node.left!=None) :
                self.removeNode(node, node.left, key)
        else : 
            self.removeNode(node, node.right, key) 
        
    def findSmallestLeafFromRight(self, parent, node):
        if(node.left==None) :
            parent.right = node.right
            return node
        else :
            return self.findSmallestLeafFromLeft(node, node.left)   
                  
    def findSmallestLeafFromLeft(self, parent, node):   
        if(node.left==None) :
            parent.left = node.right
            return node
        else :
            return self.findSmallestLeafFromLeft(node, node.left)     
        
    class TreeNode(object):
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None    
            
            