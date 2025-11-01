from typing import List


class Utilities:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = set()

        for num in nums:
            if num in res:
                return True
            
            res.add(num)
        
        return False
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapS, mapT = {} ,{}

        for i in range(len(s)):
            mapS[s[i]] = 1 + mapS.get(s[i], 0)
            mapT[t[i]] = 1 + mapT.get(t[i], 0)
        
        if mapS == mapT:
            return True
        return False

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapNum = {}

        for i,v in enumerate(nums):
            if (target - v) in mapNum:
                return [i, mapNum.get(target - v)]
            mapNum[v] = i
        return []
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for item in strs:
            word = {}

            for s in item:
                word[s] = 1 + word.get(s, 0)
            
        return res
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                sum3 = num + nums[l] + nums[r]

                if sum3 < 0:
                    l += 1
                elif sum3 > 0:
                    r -= 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
        
        return res

    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            maxWater = max(area, maxWater)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxWater
    
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]

        return res
    