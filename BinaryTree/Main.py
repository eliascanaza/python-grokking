from BinaryTree import BinaryTree
from OperationNode import Utilities

# Values

arr = [5,2,15,7,1,9,6,18]
arr2 = [5,2,15,7,1,9,6]

bt = BinaryTree()
bt2 = BinaryTree()

util = Utilities()

bt.insertArray(arr)
bt2.insertArray(arr2)

print("Nodes 1: ", arr)
print("Nodes 2: ", arr2)

# Order Traversal

print()
print("Level Order Traversal: ", util.level_order_traverse(bt.get_root()))
print("In Order Traversal: ", util.in_order_traversal(bt.get_root()))
print("Pre Order Traversal: ", util.pre_order_traversal(bt.get_root()))
print("Post Order Traversal: ", util.post_order_traversal(bt.get_root()))

# Operations

print()
print("Similars: ", util.isSimilar(bt.get_root(), bt2.get_root()))
print("Inverse Node 1: ", util.level_order_traverse(util.revertNode(bt.get_root())))