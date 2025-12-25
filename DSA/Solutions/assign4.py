class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DLL:
    def __init__(self):
        self.start = None
        
    def is_empty(self):
        return self.start is None
    
    def insert_first(self, data):
        n = Node(data)
        if self.is_empty():
            self.start = n
        else:
            n.next = self.start
            self.start.prev = n
            self.start = n
    
    def insert_last(self, data):
        n = Node(data)
        if self.is_empty():
            self.start = n
            return
        else:
            temp = self.start
            while temp.next:
                temp = temp.next
            temp.next = n
            n.prev = temp
    
    def search(self, value):
        temp = self.start
        while temp:
            if temp.data == value:
                return temp
            temp = temp.next
        return None
    
    def insert_before(self, target, data):
        node = self.search(target)
        if node is None:
            print("Target not found")
            return

        # If target is first node
        if node.prev is None:
            self.insert_first(data)
            return

        n = Node(data)
        n.prev = node.prev
        n.next = node

        node.prev.next = n
        node.prev = n
    
    def insert_after(self, target, data):
        node = self.search(target)
        if node is None:
            print("Target not found")
            return
        
        n = Node(data)
        n.next = node.next
        n.prev = node
        
        if node.next:
            node.next.prev = n
        node.next = n
    
    def print_list(self):
        temp = self.start
        while temp:
            print(temp.data, end = " <-> ")
            temp = temp.next
        print("None")
    
    def delete_first(self):
        if self.is_empty():
            print("List is empty")
            return
        
        if self.start.next is None:
            self.start = None
        else:
            self.start = self.start.next
            self.start.prev = None
    
    def delete_last(self):
        if self.is_empty():
            print("List is empty")
            return
        
        temp = self.start
        if temp.next is None:
            self.start = None
            return
        while temp.next:
            temp = temp.next
        temp.prev.next = None
    
    def delete_item(self, value):
        temp = self.start
        while temp:
            if temp.data == value:
                # If first node
                if temp.prev is None:
                    self.start = temp.next
                    if self.start:
                        self.start.prev = None
                else:
                    temp.prev.next = temp.next
                    if temp.next:
                        temp.next.prev = temp.prev
                return
            temp = temp.next
        print("Item not found")
        
    def delete_before(self, target):
        node = self.search(target)
        if node is None:
            print("Target not found")
            return

        if node.prev is None:
            print("No node exists before the target")
            return

        # If node before target is the first node
        if node.prev.prev is None:
            self.start = node
            node.prev = None
        else:
            node.prev.prev.next = node
            node.prev = node.prev.prev
    
    def delete_after(self, target):
        node = self.search(target)
        if node is None:
            print("Target not found")
            return

        if node.next is None:
            print("No node exists after the target")
            return

        temp = node.next
        node.next = temp.next

        if temp.next:
            temp.next.prev = node


dll = DLL()
dll.insert_first(10)
dll.insert_last(20)
dll.insert_last(30)
dll.insert_after(20, 25)

dll.print_list()

dll.delete_item(25)
dll.delete_first()
dll.delete_last()

dll.print_list()
