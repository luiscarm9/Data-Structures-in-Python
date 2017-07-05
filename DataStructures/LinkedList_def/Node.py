class Node(object):
    
    def __init__(self, data):
        self.data=data;
        self.NextNode=None;
    
    def removeNode(self,data,prevNode):
        if self.data==data:
            prevNode.NextNode=self.NextNode; #Update the next node reference
            del self.data
            del self.NextNode
        else:
            if self.NextNode is not None: #Recursion until is deleted
                self.NextNode.removeNode(data,self);
        
        