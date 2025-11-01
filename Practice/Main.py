from Util import Utilities

util = Utilities()

lst = [1,2,3,4,5,6,6]

print(lst)
print("Contain Duplicates: ",util.containsDuplicate(lst))

print()

str1 = "elias"
str2 = "saile"

print(str1, str2)
print("Valid Anagram: ",util.isAnagram(str1, str2))

print()

lst = [5,5]
k = 10
print("Find two sum: ", util.twoSum(lst, k))

print()

strs = ["act","pots","tops","cat","stop","hat"]
print("Group anagrams: ", util.groupAnagrams(strs))

print()

lst = [-1,0,1,2,-1,-4]
print("3 Sum list: ", lst)
print("3 sum: ", util.threeSum(lst))

lst = [0,0,0,0]
print("3 Sum list: ", lst)
print("3 sum: ", util.threeSum(lst))

lst = [-2,0,1,1,2]
print("3 Sum list: ", lst)
print("3 sum: ", util.threeSum(lst))
