from BinaryTree import BinaryTree
from OperationNode import Utilities

arr = [5,2,15,7,1,9,6]
arr2 = [5,2,15,7,1,9,6]

bt = BinaryTree()
bt2 = BinaryTree()

util = Utilities()

bt.insertArray(arr)
bt2.insertArray(arr2)
print(util.level_order_traverse(util.revertNode(bt2.get_root())))
print(util.isSimilar(bt.get_root(), util.revertNode(bt2.get_root())))
