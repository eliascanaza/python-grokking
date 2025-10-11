class SlidingWindow:
    def fixed(self, arr, k):
        #sum the first window elements, then store as best
        best = windowSum = sum(arr[:k])

        #loop to add the new element and substract the initial element of the window
        for i in range(k, len(arr)):
            windowSum += arr[i] - arr[i - k]

            #getting the maximum sum
            best = max(best, windowSum)

        return best
    
    def allWindow(self, arr, k):
        res = []

        #first sum window elements
        windowSum = sum(arr[:k])
        res.append(windowSum)

        #iterate adding and removing elements for the window
        for i in range(k, len(arr)):
            windowSum += arr[i] - arr[i - k]
            res.append(windowSum)

        return res

    def longest_subarray(self, arr, k):
        left, sum = 0, 0
        longest_subarray = 0

        #iterate all elements
        for right in range(len(arr)):
            sum += arr[right]

            #if does not meet the condition
            while sum > k:
                sum -= arr[left]
                left += 1

            #getting the longest sub array
            longest_subarray = max (longest_subarray, right - left + 1)

        return longest_subarray