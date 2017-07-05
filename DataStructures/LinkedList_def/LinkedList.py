from LinkedList_def.Node import Node;


class LinkedList(object):
    
    def __init__(self):
        self.head=None
        self.counter=0
    
    def traverseList(self):
        
        actualNode=self.head
        
        while actualNode is not None:
            print("%d " % actualNode.data)
            actualNode=actualNode.NextNode
    
    
    #Very fast! O(1)        
    def insertStart(self,data):
        self.counter+=1
        newNode=Node(data)
        
        if not self.head:
            self.head=newNode
        else:
            newNode.nextNode=self.head
            self.head=newNode
    
    def size(self):
        return self.counter
    
    #Very slow O(N)
    def insertEnd(self,data):
        if self.head is None:
            self.insertStart(data)
            return
        self.counter+=1
        
        newNode=Node(data)
        actualNode=self.head
        
        while actualNode.NextNode is not None:#iterate until the final node
            actualNode=actualNode.NextNode
        
        #Here we are in the final node
        actualNode.NextNode=newNode
    
    #Slow O(N) the worst case is to iterate all 
    def remove(self,data):
        
        self.counter-=1 
        
        if self.head:#not empty list
            if data==self.head.data:
                self.head=self.head.nextNode #Update the reference to the next 
            else:
                self.head.removeNode(data,self.head) #if is not the head iterate
            