
from AVL_def.Node import Node

class Balancedtree(object):
    
    def __init__(self):
        self.rootNode=None
    
    def insert(self,data):
        
        parentNode=self.rootNode
        
        if self.rootNode is None:
            parentNode=Node(data, None)
            self.rootNode=parentNode
        else:
            parentNode=self.rootNode.insert(data, self.rootNode)
            
        self.rebalanceTree(parentNode)
    
    def rebalanceTree(self,parentNode):
        self.setBalanced(parentNode)
        
        if parentNode.balanced<-1:
            if self.height(parentNode.leftChild.leftChild)>=self.height(parentNode.leftChild.rightChild):
                parentNode=self.rotateRight(parentNode)
            else:
                parentNode=self.rotateLeftRight(parentNode)
        elif parentNode.balanced>1:
            if self.height(parentNode.rightChild.rightChild)>=self.height(parentNode.rightChild.leftChild):
                parentNode=self.rotateLeft(parentNode)
            else:
                parentNode=self.rotateRightLeft(parentNode)
        if parentNode.parentNode is not None:
            self.rebalanceTree(parentNode.parentNode)
        else:
            self.rootNode=parentNode
                
    
    def setBalanced(self,node):
        node.balanced=(self.height(node.rightChild)-self.height(node.leftChild))
        
    def height(self,node):
        
        if node==None:
            return -1
        else:
            return 1+max(self.height(node.leftChild),self.height(node.rightChild))
    
    # Rotations     
    
    def rotateLeftRight(self,node):
        print 'Left-Right Rotation'
        node.leftChild=self.rotateLeft(node.leftChild)
        return self.rotateRight(node)
    
    def rotateRightLeft(self,node):
        print 'Right-Left Rotation'
        node.rightChild=self.rotateRight(node.rightChild)
        return self.rotateLeft(node)

    def rotateLeft(self,node):
        print 'Left Rotation'
        
        temp=node.rightChild
        temp.parentNode=node.parentNode
        
        node.rightChild=temp.leftChild
        
        if node.rightChild is not None:
            node.rightChild.paretnNode=node
        
        temp.leftChild=node
        node.parentNode=temp
        
        if temp.parentNode is not None:
            if temp.parentNode.rightChild==node:
                temp.parentNode.rightChild=temp
            else:
                temp.parentNode.rightChild=temp
        
        self.setBalanced(temp)
        self.setBalanced(node)
        
        return temp
    
    
    def rotateRight(self,node):
        print 'Right Rotation'
        
        temp=node.leftChild
        temp.parentNode=node.parentNode
        
        node.leftChild=temp.rightChild
        
        if node.leftChild is not None:
            node.leftChild.parentNode=node
        
        temp.rightChild=node
        node.parentNode=temp
        
        if temp.parentNode is not None:
            if temp.parentNode.rightChild==node:
                temp.parentNode.rightChild=temp
            else:
                temp.parentNode.leftChild=temp
        
        self.setBalanced(temp)
        self.setBalanced(node)
        
        return temp
        
    

    
        
        