from BS import BinarySearchPattern

bs = BinarySearchPattern()
list1 = [1,2,3,4,5,6,7,8]
target1 = 6

list2 = [1,2,3,4,5,7,8]
target2 = 61

print("Binary Search:")
print(list1, "target: ", target1)
print("Index: ",bs.findElement(list1, target1))
print()
print(list2, "target: ", target2)
print("Index: ",bs.findElement(list2, target2))

