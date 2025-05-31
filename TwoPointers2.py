# for remove_nth_last_node problem
# Definition for a Linked List node
# class LinkedListNode:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

from linked_list import LinkedList
from linked_list_node import LinkedListNode

class TwoPointer:
    #
    # Check if an string is a palindrome
    # "ABA" = true, "ABBBA" = true, "abbbas" = false
    def is_palindrome(s):
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
            
        return True
    # 
    # Sum of tree is igual zero 0
    #
    def three_sum(nums):
        nums.sort()

        left = 0
        right = len(nums) - 1
        sum = 0
        result = []

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            if i > 0 and nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result

    #
    # Remove Nth Node from End of List
    #
    def remove_nth_last_node(head, n):
        left = head
        right = head
    
        for i in range(n):
            right = right.next

        if not right:
            return left.next
        
        while right.next:
            right = right.next
            left = left.next

        left.next = left.next.next

        return head
    
    #
    # Sort colors
    # 0: red, 1: white, 2: blue
    def sort_colors(colors):
        current, left = 0,0
        right = len(colors) - 1

        while current <= right:
            if colors[current] == 0:
                colors[left], colors[current] = colors[current], colors[left]

                left += 1
                current += 1
            elif colors[current] == 1:
                current += 1
            elif colors[current] == 2:
                colors[right], colors[current] = colors[current], colors[right]

                right -= 1

        return colors

    #
    # Reverse words
    #
    def reverse_words(_self, sentence):
        sentence = sentence[::-1]

        word = list(sentence)
        left = 0
        right = 0

        for right in range(len(word)):
            if word[right] == ' ':
                word = _self.revertWord(left, right - 1, word)
                left = right + 1
            else:
                right += 1

        _self.revertWord(left, right - 1, word)

        return ''.join(word)

    def revertWord(_self, left, right, word):
        tmp_left = left
        tmp_right = right

        while tmp_left < tmp_right:
            tmp = word[tmp_left]
            word[tmp_left] = word[tmp_right]
            word[tmp_right] = tmp

            tmp_left += 1
            tmp_right -= 1
        
        return word

    def valid_word_abbreviation(_self, word, abbr):
        abbr_init = 0
        word_init = 0

        while abbr_init < len(abbr):
            num = abbr[abbr_init]
            if num.isdigit():
                print(abbr[abbr_init])
                
                word_init = abbr_init + num
                
                
                    
                abbr_init += 1
            else:
                word_init += 1
                abbr_init += 1

        return True
#print(TwoPointer.is_palindrome('abababa'))
#print(TwoPointer.three_sum([-4,-2,-2,-2,0,2,2,2,4]))

#input_linked_list = LinkedList()
#input_linked_list.create_linked_list([69,8,49,106,116,112])
#list = TwoPointer.remove_nth_last_node(input_linked_list.head, 6)
#while list.next:
#    print(list.data)
#    list = list.next

#print(TwoPointer.sort_colors([1,1,0,2,0]))

twoPointer = TwoPointer()
print(twoPointer.valid_word_abbreviation("elias", "e2as"))

#print(twoPointer.reverse_words("Elias como estas"))

