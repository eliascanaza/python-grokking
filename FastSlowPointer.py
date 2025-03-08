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

fastSlowPointer = FastSlowPointer()

#print(fastSlowPointer.happyNumber(40))

input_linked_list = LinkedList()
input_linked_list.create_linked_list([1,2,3,4,5,6])
list = input_linked_list.head

print(fastSlowPointer.get_middle_node(list))
#print(fastSlowPointer.detect_cycle(input_linked_list.head))


