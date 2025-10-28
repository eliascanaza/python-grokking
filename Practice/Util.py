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

