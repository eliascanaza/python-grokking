from Node import Node

class Utilities:
    def isSimilar(self, first: Node, second: Node):
        if not first and not second:
            return True
        
        if first and second and first.value == second.value:
            return self.isSimilar(first.left, second.left) and self.isSimilar(first.right, second.right)
        
        return False