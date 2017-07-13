class Node(object):
    
    def __init__(self,data,parentNode):
        self.data=data
        self.parenNode=parentNode
        self.rightChild=None
        self.leftChild=None
        self.balanced=0
    
    def insert(self,data,parentNode):
        
        if data<self.data:
            if not self.leftChild:#if it is Null
                self.leftChild=Node(data, parentNode)
            else:
                self.leftChild.insert(data, parentNode)
        else:
            if not self.rightChild:
                self.rightChild=Node(data, parentNode)
            else:
                self.rightChild.insert(data, parentNode)
                
        return parentNode
    
    def getTraverseInOrder(self) :
        
        if self.leftChild is not None:
            self.leftChild.getTraverseInOrder()
        
        print self.data
        
        if self.rightChild is not None:
            self.rightChild.getTraverseInOrder() 
    
    def getMax(self):
        if not self.rightChild:
            return self.data
        else:
            return self.rightChild.getMax()


    def getMin(self):
        if not self.leftChild:
            return self.data
        else:
            return self.leftChild.getMin()
           
        
                
                
        