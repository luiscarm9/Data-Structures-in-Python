from BinarySerachTree_def.BinaryTree import BinaryTreeS

binarytree=BinaryTreeS()

#create a binary tree with fibonnaci 
binarytree.insert(0)
binarytree.insert(1)
binarytree.insert(1)
binarytree.insert(2)
binarytree.insert(3)
binarytree.insert(5)
binarytree.insert(8)
binarytree.insert(13)

binarytree.getTraverseInOrder()

print('------------------------------')

#Remove the last element
binarytree.remove(13)
binarytree.getTraverseInOrder()

print('------------------------------')
#Remove the first element different of zero
binarytree.remove(1)
binarytree.getTraverseInOrder()

print('------------------------------')
print 'Max Value:' 
print binarytree.getMax()
print 'Min Value:' 
print binarytree.getMin()