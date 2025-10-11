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

