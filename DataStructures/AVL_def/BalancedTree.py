
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
    
    def setBalanced(self,node):
        node.balanced=self.height(node.rightChild-self.height(node.leftChild))
        
    def height(self,node):
        
        if Node==None:
            return -1
        else:
            return 1+max(self.height(node.leftChild),self.height(node.rightChild))
    
    
        
        