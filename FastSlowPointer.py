from linked_list import LinkedList

class FastSlowPointer:
    def happyNumber(_self, number):
        sum = number
        numList = set()
        numList.add(number)

        while sum != 1:
            sum = 0
            
            while number > 0:
                digit = number % 10
                number //= 10
                sum += digit * digit
            
            if sum in numList: 
                return False
            
            numList.add(sum)
            number = sum

        return True
    
    def detect_cycle(_self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    def get_middle_node(_self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    def find_duplicate(_self, nums):
        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        print(slow,"-",fast)
        return 0

fastSlowPointer = FastSlowPointer()

#print(fastSlowPointer.happyNumber(40))

#input_linked_list = LinkedList()
#input_linked_list.create_linked_list([1,2,3,4,5,6])
#list = input_linked_list.head

#print(fastSlowPointer.get_middle_node(list))
#print(fastSlowPointer.detect_cycle(input_linked_list.head))
print(fastSlowPointer.find_duplicate([4,5,6,1,3,7,54]))


