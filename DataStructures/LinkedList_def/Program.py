from LinkedList_def.LinkedList import LinkedList;



LList=LinkedList()

#Insert Elements at the start (FATS)

LList.insertStart(1)
LList.insertStart(2)
LList.insertStart(3)
LList.insertStart(5)

#Insert Elements at the end (SLOW)
LList.insertEnd(8)
LList.insertEnd(13)
LList.insertEnd(21)
LList.insertEnd(34)
LList.insertEnd(55)
LList.insertEnd(89)
print("----------------------------------------------------------------------")

#Print what is in our list
LList.traverseList()
print("----------------------------------------------------------------------")
#Remove first element (FATS)
LList.remove(55)
LList.traverseList()

