class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.start = None
        
    def is_empty(self):
        return self.start is None
    
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.start
        self.start = new_node
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            return
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    
    def search(self, value):
        temp = self.start
        while temp:
            if temp.data == value:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self, target, data):
        node = self.search(target)
        if node is None:
            print("Element not found")
            return
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node
    
    def print_list(self):
        temp = self.start 
        if self.is_empty():
            print("List is empty")
            return
        while temp:
            print(temp.data, end = " -> ")
            temp = temp.next
        print("None")
    
    def delete_last(self):
        if self.is_empty():
            print("List is empty")
            return
        if self.start.next is None:
            self.start = None
            return
        temp = self.start
        while temp.next.next:
            temp = temp.next
        temp.next = None
    
    def delete_first(self):
        if self.is_empty():
            raise IndexError("List is empty")
        value = self.start.data
        self.start = self.start.next
        return value

    def get_first(self):
        if self.is_empty():
            raise IndexError("List is empty")
        return self.start.data

    
    def delete_item(self, value):
        if self.is_empty():
            print("List is empty")
            return
        if self.start.data == value:
            self.start = self.start.next
            return
        
        prev = self.start
        curr = self.start.next
        while curr:
            if curr.data == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
        print("Element not found")
    
    def delete_after(self, target):
        if self.is_empty():
            print("List is empty")
            return

        curr = self.start

        while curr and curr.data != target:
            curr = curr.next

        if curr is None or curr.next is None:
            print("Deletion not possible")
            return

        curr.next = curr.next.next
    
    def size(self):
        count = 0
        temp = self.start
        while temp:
            count += 1
            temp = temp.next
        return count


s = SLL()
s.insert_at_start(10)
s.insert_at_end(20)
s.insert_at_end(30)
s.insert_after(20, 25)

s.print_list()

s.delete_first()
s.delete_last()
s.delete_item(25)

s.print_list()