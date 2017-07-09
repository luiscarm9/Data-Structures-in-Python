from BinarySerachTree_def.Node import Node

class BinaryTreeS(object):
    
    def __init__(self):
        self.rootNode=None
    
    def insert(self,data):
        if not self.rootNode:
            self.rootNode=Node(data)
        else:
            self.rootNode.insert(data)
    
    def remove(self,dataRemove):
        if self.rootNode:
            if self.rootNode.data == dataRemove:
                temp=Node(None)
                temp.leftChild=self.rootNode
                self.rootNode.remove(dataRemove,temp)
            else:
                self.rootNode.remove(dataRemove, None)
    
    def getMax(self):
        if self.rootNode:
            return self.rootNode.getMaxValue()

    def getMin(self):
        if self.rootNode:
            return self.rootNode.getMinValue()  
           
    def getTraverseInOrder(self) :     
        if self.rootNode:
            self.rootNode.getTraverseInOrder()       