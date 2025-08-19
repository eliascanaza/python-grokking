from TreeNodeObject import TreeNode

class Utilities:
    def isSimilar (self, first: TreeNode, second: TreeNode):
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
    def level_order_traverse (self, node: TreeNode):
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
    def in_order_traversal (self, node: TreeNode):
        result = []
        
        if node:
            result = self.in_order_traversal(node.left)
            result.append(node.value)
            result += self.in_order_traversal(node.right)
        return result
    
    # Left -> Right -> Root
    def post_order_traversal (self, node: TreeNode):
        result = []

        if node:
            result = self.post_order_traversal(node.left)
            result += self.post_order_traversal(node.right)
            result.append(node.value)
        return result
    
    # Root -> Left -> Right
    def pre_order_traversal (self, node: TreeNode):
        result = []

        if node:
            result.append(node.value)
            result += self.pre_order_traversal(node.left)
            result += self.pre_order_traversal(node.right)
        return result
    
    def sum_left_leaves(self, node: TreeNode):
        sum = 0
        return sum

    def num_levels (self, node: TreeNode):
        if node is None:
            return 1
        
        levels_left = 0
        levels_right = 0

        return max(levels_left, levels_right)

    def level_order_traversal(self, node: TreeNode):
        if not node:
            return 
        
        queue = [node]
        result = []

        while queue:
            queue_size = len(queue)
            level = []

            for i in range(queue_size):
                current_node = queue.pop(0)
                level.append(current_node.value)

                if current_node.left:
                    queue.append(current_node.left)

                if current_node.right:
                    queue.append(current_node.right)

            result.append(level)

        return result