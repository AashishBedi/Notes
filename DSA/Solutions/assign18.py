class Node:
    def __init__(self, item):
        self.left = None
        self.item = item
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, item):
        self.root = self.rinsert(self.root, item)
    def rinsert(self, root, item):
        if root is None:
            return Node(item)
        elif item < root.item:
            root.left = self.rinsert(root.left, item)
        elif item > root.item:
            root.right= self.rinsert(root.right, item)
        return root
    
    def search(self, item):
        return self.rsearch(self.root, item)
    def rsearch(self, root, item):
        if root is None or root.item == item:
            return root
        if item < root.item:
            return self.rsearch(root.left, item)
        return self.rsearch(root.right, item)
    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.item, end = ' ')
            self.inorder(node.right)
    
    def preorder(self, node):
        if node:
            print(node.item, end = ' ')
            self.preorder(node.left)
            self.preorder(node.right)
    
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.item, end = ' ')

if __name__ == "__main__":
    bst = BST()

    elements = [50, 30, 70, 20, 40, 60, 80]
    for el in elements:
        bst.insert(el)

    print("Inorder Traversal:")
    bst.inorder(bst.root)

    print("\nPreorder Traversal:")
    bst.preorder(bst.root)

    print("\nPostorder Traversal:")
    bst.postorder(bst.root)

    print("\n\nSearch Result:")
    node = bst.search(90)
    if node:
        print("Item found:", node.item)
    else:
        print("Item not found")