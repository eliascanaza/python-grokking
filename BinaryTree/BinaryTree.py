from TreeNodeObject import TreeNode

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insertArray(self, arr):
        if not arr:
            return

        if not self.root:
            self.root = TreeNode(arr[0])

        queue = []
        queue.append(self.root)

        i = 1

        while queue and i < len(arr):
            current = queue.pop(0)

            if i < len(arr):
                current.left = TreeNode(arr[i])
                queue.append(current.left)
                i += 1

            if i < len(arr):
                current.right = TreeNode(arr[i])
                queue.append(current.right)
                i += 1
        
    def get_root(self):
        return self.root