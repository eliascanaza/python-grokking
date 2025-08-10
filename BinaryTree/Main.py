from BinaryTree import BinaryTree
from OperationNode import Utilities

arr = [5,2,5,7,1,9,6]
arr2 = [5,2,5,7,1,9,6]

bt = BinaryTree()
bt2 = BinaryTree()

util = Utilities()

bt.insertArray(arr)
bt2.insertArray(arr2)

print(util.isSimilar(bt.get_root(), bt2.get_root()))
