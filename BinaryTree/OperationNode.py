from typing import Optional
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
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:
            return True
        
        def compare_tree(left: TreeNode, right: TreeNode):
            if not left and not right:
                return True
            
            if not left or not right:
                return False
            
            if not left or not right or left.value != right.value:
                return False

            return compare_tree(left.left, right.right) and compare_tree(left.right, right.left)

        return  compare_tree(root.left, root.right)
        
    def zigzag_level_order(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return
        
        queue = [root]
        result = []
        zigzag = False

        while queue:
            levels = []
            len_nodes = len(queue)

            for i in range(len_nodes):
                node = queue.pop(0)

                if zigzag:
                    levels.insert(0, node.value)
                else:
                    levels.append(node.value)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            
            zigzag = not zigzag
            result.append(levels)

        return result
