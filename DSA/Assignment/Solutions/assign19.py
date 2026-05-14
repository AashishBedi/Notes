class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = self.rinsert(self.root, data)
    def rinsert(self, root, data):
        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = self.rinsert(root.left, data)
        elif data > root.data:
            root.right= self.rinsert(root.right, data)
        return root
    
    
    def find_min(self):
        if self.root is None:
            return None
        
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.data
    
    
    def find_max(self):
        if self.root is None:
            return None
        
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.data
    
    
    def delete(self, key):
        self.root = self.rdelete(self.root, key)
        
    def rdelete(self, root, key):
        if root is None:
            return root
        
        if key < root.data: 
            root.left = self.rdelete(root.left, key)
        elif key > root.data:
            root.right= self.rdelete(root.right, key)
        else:
            #Case 1: no child
            if root.left is None and root.right is None:
                return None
            #Case 2: One Child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            #Case 3: Two Children
            successor = self._min_node(root.right)
            root.data = successor.data
            root.right= self.rdelete(root.right, successor.data)
        return root
    
    def _min_node(self, root):
        curr = root
        while curr.left:
            curr = curr.left
        return curr
    
    def size(self, node):
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)
    
if __name__ == "__main__":
    bst = BST()

    # Insert elements
    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        bst.insert(v)

    print("BST created with elements:", values)

    # Test minimum value
    print("Minimum value in BST:", bst.find_min())   # Expected: 20

    # Test maximum value
    print("Maximum value in BST:", bst.find_max())   # Expected: 80

    # Test size
    print("Size of BST:", bst.size(bst.root))                 # Expected: 7

    # Delete a leaf node
    bst.delete(20)
    print("\nAfter deleting 20 (leaf node):")
    print("Minimum value:", bst.find_min())           # Expected: 30
    print("Size:", bst.size(bst.root))                         # Expected: 6

    # Delete a node with one child
    bst.delete(30)
    print("\nAfter deleting 30 (one child):")
    print("Minimum value:", bst.find_min())           # Expected: 40
    print("Size:", bst.size(bst.root))                         # Expected: 5

    # Delete a node with two children
    bst.delete(50)
    print("\nAfter deleting 50 (two children):")
    print("Minimum value:", bst.find_min())           # Expected: 40
    print("Maximum value:", bst.find_max())           # Expected: 80
    print("Size:", bst.size(bst.root))                         # Expected: 4
