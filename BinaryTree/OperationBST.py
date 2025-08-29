import math
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

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed, maxSpeed = 1, max(piles)
        res = maxSpeed

        while minSpeed <= maxSpeed:
            mid = (minSpeed + maxSpeed) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)

            if hours <= h:
                res = min(hours, res)
                maxSpeed = mid - 1
            else:
                minSpeed = mid + 1
        
        return minSpeed

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        index = l

        if index == 0:
            l, r = 0, len(nums) - 1
        
        # Evaluating if this is in left side
        elif target >= nums[0] and target <= nums[index - 1]:
            l, r = 0, index - 1

        # Evaluating if this is in right side
        else:
            l, r = index, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            else: 
                r = m - 1
        return -1