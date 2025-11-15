from typing import List
from heapq import heapify
from collections import defaultdict


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
    
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        return nums[l]
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[amount] if dp[amount] != amount + 1 else -1

    def removeDuplicates(self, nums: List[int]) -> int:
        pass

    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        res = {}

        for num in nums:
            res[num] = res.get(num, 0) + 1
        
        lst = []
        for num, count in res.items():
            lst.append([count,num])
        
        lst.sort(reverse=True)
        
        i = 0
        final = []
        while i < k:
            final.append(lst[i][1])
            i += 1

        return final

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        map = {}
        bucket = [[] for i in range(len(nums))]
        res = []

        for num in nums:
            map[num] = map.get(num, 0) + 1
        
        
        for num, count in map.items():
            bucket[count].append(num)

        
        for index in range(len(bucket) - 1, 0, -1):
            for num in bucket[index]:
                if len(res) == k:
                    return res
                if num:
                    res.append(num)
        
        return res

    def encode(self, strs: List[str]) -> str:
        res = ''

        for word in strs:
            res += str(len(word)) + '#' + word

        return res

    def decode(self, s: str) -> List[str]:
        res = []

        num = ''
        index = 0
        while index < len(s):
            if s[index] == '#':
                    index += 1
                    lenght = int(num)
                    k = 0
                    word = ''

                    while k < lenght:
                        word += s[index]
                        index += 1
                        k += 1

                    res.append(word)
                    num = ''
            else:
                num += s[index]
                index += 1

        return res
    
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while not self.isAlpha(s[l]):
                l += 1
            while not self.isAlpha(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True

    def isAlpha(self, c):
            return (ord('a') <= ord(c) <= ord('z') or 
                    ord('A') <= ord(c) <= ord('Z') or 
                    ord('0') <= ord(c) <= ord('9'))

    def longestConsecutive(self, nums: List[int]) -> int:
        lst = set(nums)

        maxCount = 0
        for num in lst:
            if num - 1 is not lst:
                count = 1
                while num + count in lst:
                    count += 1
                maxCount = max(maxCount, count)
        
        return maxCount

    def isValid(self, s: str) -> bool:
        mapS = {")":"(","]":"[","}":"{"}
        stack = []

        for sing in s:
            if sing not in mapS:
                stack.append(sing)
            else:
                if mapS.get(sing) == stack[-1]:
                    stack.pop()
        return False if stack else True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for item in strs:
            word = [0] * 26

            for c in item:
                word[ord(c) - ord('a')] += 1

            res[tuple(word)].append(item)
        return list(res.values())
