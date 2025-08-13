from Node import Node

class Utilities:
    def isSimilar (self, first: Node, second: Node):
        if not first and not second:
            return True
        
        if first and second and first.value == second.value:
            return self.isSimilar(first.left, second.left) and self.isSimilar(first.right, second.right)
        
        return False
    
    def revertNode (self, root):
        if not root:
            return root
        
        self.revertNode(root.left)
        self.revertNode(root.right)

        root.right, root.left = root.left, root.right

        return root
    
    # Level by Level
    def level_order_traverse (self, node: Node):
        result = []

        if not node:
            return

        queue = []
        queue.append(node)

        while queue:
            currentNode = queue.pop(0)
            result.append(currentNode.value)

            if currentNode.left:
                queue.append(currentNode.left)

            if currentNode.right:
                queue.append(currentNode.right)

        return result
        
    # Left -> Root -> Right
    def in_order_traversal (self, node: Node):
        result = []
        
        if node:
            result = self.in_order_traversal(node.left)
            result.append(node.value)
            result += self.in_order_traversal(node.right)
        return result
    
    # Left -> Right -> Root
    def post_order_traversal (self, node: Node):
        result = []

        if node:
            result = self.post_order_traversal(node.left)
            result += self.post_order_traversal(node.right)
            result.append(node.value)
        return result
    
    # Root -> Left -> Right
    def pre_order_traversal (self, node: Node):
        result = []
        return result