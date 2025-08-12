from Node import Node

class Utilities:
    def isSimilar(self, first: Node, second: Node):
        if not first and not second:
            return True
        
        if first and second and first.value == second.value:
            return self.isSimilar(first.left, second.left) and self.isSimilar(first.right, second.right)
        
        return False
    
    def revertNode(self, root):
        if not root:
            return root
        
        self.revertNode(root.left)
        self.revertNode(root.right)

        root.right, root.left = root.left, root.right

        return root
    
    def level_order_traverse (self, root: Node):
        result = []

        if not root:
            return result
        
        queue = []
        queue.append(root)

        while queue:
            current = queue.pop(0)
            result.append(current.value)

            if current.left:
                queue.append(current.left)
            
            if current.right:
                queue.append(current.right)
            
        return result