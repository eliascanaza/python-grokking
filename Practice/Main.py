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

