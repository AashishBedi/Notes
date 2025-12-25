class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class CDLL:
    def __init__(self):
        self.last = None   # reference to last node

    def is_empty(self):
        return self.last is None

    def insert_at_start(self, data):
        new_node = Node(data)

        if self.is_empty():
            new_node.next = new_node
            new_node.prev = new_node
            self.last = new_node
        else:
            first = self.last.next
            new_node.next = first
            new_node.prev = self.last
            first.prev = new_node
            self.last.next = new_node

    def insert_at_last(self, data):
        new_node = Node(data)

        if self.is_empty():
            new_node.next = new_node
            new_node.prev = new_node
            self.last = new_node
        else:
            first = self.last.next
            new_node.next = first
            new_node.prev = self.last
            first.prev = new_node
            self.last.next = new_node
            self.last = new_node

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
    
    def insert_before(self, target, data):
        if self.is_empty():
            print("List is empty")
            return

        curr = self.last.next  # first node
        while True:
            if curr.data == target:
                new_node = Node(data)
                new_node.next = curr
                new_node.prev = curr.prev
                curr.prev.next = new_node
                curr.prev = new_node
                return
            curr = curr.next
            if curr == self.last.next:
                break

        print("Element not found")

    def insert_after(self, target, data):
        node = self.search(target)
        if node is None:
            print("Element not found")
            return

        new_node = Node(data)
        new_node.next = node.next
        new_node.prev = node
        node.next.prev = new_node
        node.next = new_node

        if node == self.last:
            self.last = new_node

    def print_list(self):
        if self.is_empty():
            print("List is empty")
            return

        temp = self.last.next
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.next
            if temp == self.last.next:
                break
        print("(circular)")

    def delete_first(self):
        if self.is_empty():
            return

        if self.last.next == self.last:
            self.last = None
        else:
            first = self.last.next
            self.last.next = first.next
            first.next.prev = self.last

    def delete_last(self):
        if self.is_empty():
            return

        if self.last.next == self.last:
            self.last = None
        else:
            prev_node = self.last.prev
            prev_node.next = self.last.next
            self.last.next.prev = prev_node
            self.last = prev_node

    def delete_item(self, value):
        if self.is_empty():
            return

        curr = self.last.next
        while True:
            if curr.data == value:
                if curr == self.last and curr.next == self.last:
                    self.last = None
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    if curr == self.last:
                        self.last = curr.prev
                return
            curr = curr.next
            if curr == self.last.next:
                break
        print("Element not found")
    
    def delete_before(self, value):
        if self.is_empty() or self.last.next == self.last:
            print("Operation not possible")
            return

        curr = self.last.next
        while True:
            if curr.data == value:
                node_to_delete = curr.prev

                # If node to delete is the only node
                if node_to_delete == curr:
                    self.last = None
                else:
                    node_to_delete.prev.next = curr
                    curr.prev = node_to_delete.prev

                    if node_to_delete == self.last:
                        self.last = node_to_delete.prev
                return

            curr = curr.next
            if curr == self.last.next:
                break

        print("Element not found")
        
    def delete_after(self, value):
        if self.is_empty() or self.last.next == self.last:
            print("Operation not possible")
            return

        curr = self.last.next
        while True:
            if curr.data == value:
                node_to_delete = curr.next

                # If only one node
                if node_to_delete == curr:
                    self.last = None
                else:
                    curr.next = node_to_delete.next
                    node_to_delete.next.prev = curr

                    if node_to_delete == self.last:
                        self.last = curr
                return

            curr = curr.next
            if curr == self.last.next:
                break

        print("Element not found")


cdll = CDLL()

cdll.insert_at_start(10)
cdll.insert_at_last(20)
cdll.insert_at_last(30)
cdll.insert_after(20, 25)

cdll.print_list()

cdll.delete_first()
cdll.delete_last()
cdll.delete_item(25)

cdll.print_list()