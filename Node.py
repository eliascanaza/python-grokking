class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Operation:
    def getMiddle(self, node = Node):
        slow = node
        faster = node
        
        while faster and faster.next:
            slow = slow.next
            faster = faster.next.next

        return slow.data

node = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)



node3.next = node4
node2.next = node3
node1.next = node2
#node.next = node1



ope = Operation()
print(ope.getMiddle(node))