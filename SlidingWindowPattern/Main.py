from SlidingWindowPattern import SlidingWindow

slidingWindow = SlidingWindow()
case1 = [1,2,3,4,5,2,1,3]
case2 = [1,2,1,2,1,4,2,1,2]
print("Greatest Sum: ", slidingWindow.fixed(case1, 3))
print(slidingWindow.fixed(case2, 3))

print("All sum window: ",slidingWindow.allWindow(case1, 4))
print("Longest sum array: ",slidingWindow.longest_subarray(case2, 7))