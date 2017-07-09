
class Node(object):
    
    def __init__(self, data):
        self.data=data
        self.rightChild=None
        self.leftChild=None
    
    def insert(self,data):
        if data<self.data: #In binary trees left always is smaller than the value of parent Node
            if not self.leftChild:
                self.leftChild=Node(data)
            else:
                self.leftChild.insert(data)
        else: #If is bigger in binary tree always right
            if not self.rightChild:
                self.rightChild=Node(data)
            else:
                self.rightChild.insert(data)            
    
    def getMinValue(self):
        if self.leftChild is None:
            return self.leftChild
        else:
            self.leftChild.getMinValue()
            
    def getMaxValue(self):
        if self.rightChild is None:
            return self.rightChild
        else:
            self.rightChild.getMinValue()        
    
    def getTraverseInOrder(self) :
        
        if self.leftChild is not None:
            self.leftChild.getTraverseInOrder()
        
        print self.data
        
        if self.rightChild is not None:
            self.rightChild.getTraverseInOrder() 
     
    #Slow 
    def remove(self,data,parentNode):
            if data<self.data: #search the value if is smaller
                if self.leftChild is not None:
                    self.leftChild.remove(data, self)
            elif data>self.data: #search the value if bigger
                if self.rightChild is not None:
                    self.rightChild.remove(data, self)
            else:
                if self.rightChild is not None and self.leftChild is not None: #Node with 2 
                    self.data=self.rightChild.getMinValue()
                    self.rightChild.remove(self.data, self)
                elif parentNode.leftChild == self:
                    if self.leftChild is not None:
                        temp=self.leftChild
                    else:
                        temp=self.rightChild
                        
                    parentNode=self.rightChild
                
                elif parentNode.rightChild == self:
                    if self.leftChild is not None:
                        temp=self.leftChild
                    else:
                        temp=self.rightChild
                        
                    parentNode.rightChild=temp
           
            
    
            