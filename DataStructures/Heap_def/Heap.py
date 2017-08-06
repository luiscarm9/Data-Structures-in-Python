from unittest import result
class Heap(object):
    
    HEAP_SIZE=20
    
    def __init__(self):
        self.heap=[0]*Heap.HEAP_SIZE 
        self.currentposition=-1
    
    
    def insert(self,item):        
        if self.isFull():
            print 'WARNING: Heap is full'
            return
        
        self.currentposition=self.currentposition+1
        self.heap[self.currentposition]=item
        self.fixUp(self.currentposition)
    
    def isFull(self):
        if self.currentposition==Heap.HEAP_SIZE:
            return True
        else:
            return False
    
    def fixUp(self,index):        
        parentIndex=int((index-1)/2)
        
        while parentIndex>=0 and self.heap[parentIndex]<self.heap[index]:
            temp=self.heap[index]
            self.heap[index]=self.heap[parentIndex]
            self.heap[parentIndex]=temp
            index=parentIndex
            parentIndex=int((index-1)/2)
            
            
    def fixDown(self,index,upindex):        
        if upindex<0:
            upindex=self.currentposition
        
        while index<=upindex:
            leftChild=2*index+1
            rightChild=2*index+2
            
            if leftChild<=upindex:
                childSwap=None
                
                if rightChild>upindex:
                    childSwap=leftChild
                else:
                    if self.heap[leftChild]>self.heap[rightChild]:
                        childSwap=leftChild
                    else:
                        childSwap=rightChild
                
                if self.heap[index]<self.heap[childSwap]:
                    temp=self.heap[index]
                    self.heap[index]=self.heap[childSwap]
                    self.heap[childSwap]=temp
                else:
                    break
                
                index=childSwap
            
            else:
                break       
                
            
    def getMax(self):
        result=self.heap[0]
        self.currentposition=self.currentposition-1
        self.heap[0]=self.heap[self.currentposition]
        del self.heap[self.currentposition+1]
        self.fixDown(0,-1)       
        return result
                    
    
    def heapSort(self):        
        for i in range(0,self.currentposition+1):
            temp=self.heap[0]
            print("%d"%temp)
            self.heap[0]=self.heap[self.currentposition-i]
            self.heap[self.currentposition-i]=temp
            self.fixDown(0, self.currentposition-i-1)
            
    