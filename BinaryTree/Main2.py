from OperationBST import Solution

sol = Solution()

matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60], [62,70,74,80]]
target1 = 80
matrix2 = [[1,3]]
target2 = 3


print("Search 2D Matrix: ", matrix1)
print("Find: ", target1, ", Result: ", sol.searchMatrix(matrix1, target1))

print("Search 2D Matrix: ", matrix2)
print("Find: ", target2, ", Result: ", sol.searchMatrix(matrix2, target2))

print("Search 2D Matrix: ", matrix2)
print("Find: ", 1000, ", Result: ", sol.searchMatrix(matrix2, 1000))