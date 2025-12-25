class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.last = None
    
    def is_empty(self):
        return self.last is None
    
    def insert_at_start(self, data):
        n = Node(data)
        if self.is_empty():
            self.last = n
            n.next = n
        else:
            n.next = self.last.next
            self.last.next = n
    
    def insert_at_last(self, data):
        n = Node(data)
        if self.is_empty():
            self.last = n
            n.next = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n
    
    def search(self, value):
        if self.is_empty():
            return None
        temp = self.last.next
        while True:
            if temp.data == value:
                return temp
            temp = temp.next
            if temp == self.last.next:
                break
        return None
    
    def insert_after(self, target, data):
        node = self.search(target)
        if node is None:
            print("Element not found")
            return

        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node

        if node == self.last:
            self.last = new_node
    
    def print_list(self):
        if self.is_empty():
            print("List is empty")
            return
        temp = self.last.next
        while True:
            print(temp.data, end = " ")
            temp = temp.next
            if temp == self.last.next:
                break
        print()
    
    def delete_first(self):
        if self.is_empty():
            return
        if self.last.next == self.last:
            self.last = None
        else:
            self.last.next = self.last.next.next
    
    def delete_last(self):
        if self.is_empty():
            return
        if self.last.next == self.last:
            self.last = None
            return
        else:
            temp = self.last.next
            while temp.next != self.last:
                temp = temp.next
            temp.next = self.last.next
            self.last = temp

    def delete_item(self, value):
        if self.is_empty():
            return
        prev = self.last
        curr = self.last.next
        while True:
            if curr.data == value:
                if curr == self.last:
                    self.delete_last()
                elif curr == self.last.next:
                    self.delete_first()
                else:
                    prev.next = curr.next
                return
            prev = curr
            curr = curr.next
            if curr == self.last.next:
                break
        print("Element not found")
    
    def delete_after(self, target):
        # If list is empty
        if self.is_empty():
            print("List is empty")
            return

        curr = self.last.next  # first node

        while True:
            if curr.data == target:
                node_to_delete = curr.next

                # Case: only one node
                if curr == curr.next:
                    self.last = None

                # Case: deleting last node
                elif node_to_delete == self.last:
                    curr.next = self.last.next
                    self.last = curr

                # Normal case
                else:
                    curr.next = node_to_delete.next

                return

            curr = curr.next
            if curr == self.last.next:
                break

        print("Element not found")


cll = CLL()

cll.insert_at_start(10)
cll.insert_at_last(20)
cll.insert_at_last(30)
cll.insert_after(20, 25)

cll.print_list()        # 10 20 25 30

cll.delete_first()
cll.delete_last()
cll.delete_item(25)