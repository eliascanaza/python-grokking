from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        bot, top = 0, rows - 1
        row = 0

        if target > matrix[rows-1][cols-1] or target < matrix[0][0]:
            return False

        while bot <= top:
            row = (bot + top) // 2

            if target > matrix[row][-1]:
                bot = row + 1
            elif target < matrix[row][0]:
                top = row - 1
            else: break
        
        bot, top = 0, cols - 1

        while bot <= top:
            mid = (bot + top) // 2

            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                bot = mid + 1
            else:
                top = mid - 1
        
        return False
        