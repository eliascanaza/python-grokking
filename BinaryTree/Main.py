from BinaryTree import BinaryTree

arr = [4,3,-5,3,6,12]

bt = BinaryTree()
bt.insertArray(arr)
result = bt.level_order_traverse()

print(result)