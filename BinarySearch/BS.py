class BinarySearchPattern:
    def findElement(self, nums, target):
        start, end = 0, len (nums) - 1

        while start <= end:
            middle = (start + end) // 2
            
            if nums[middle] == target:
                return middle
            elif target < nums[middle]:
                end = middle - 1
            else:
                start = middle + 1
        
        return -1

    def findInRotatedArray(self, nums, target):
        s, e = 0, len(nums) - 1

        while s <= e:
            m = (s + e) // 2

            if nums[m] == target:
                return m
            
            if nums[s] <= nums[m]:
                if nums[s] <= target and target < nums[m]:
                    e = m - 1
                else:
                    s = m + 1
            else:
                if nums[m] < target and target <= nums[e]:
                    s = m + 1
                else:
                    e = m - 1
        return -1