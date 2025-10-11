from SlidingWindowPattern import SlidingWindow

slidingWindow = SlidingWindow()
case1 = [4,2,3,1,5,7,6,8]
case2 = [2,3]
print("Greatest Sum: ", slidingWindow.fixed(case1, 3))
print(slidingWindow.fixed(case2, 3))

print("All sum window: ",slidingWindow.allWindow(case1, 4))
