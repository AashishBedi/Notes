from queue import Empty
from turtle import right


class EmptyHeapException(Exception):
    def __init__(self, msg = 'Empty Heap'):
        self.msg = msg
    def __str__(self):
        return self.msg


class Heap:
    def __init__(self):
        self.heap = []
    
    def createHeap(self, list1):
        for e in list1:
            self.insert(e)
    def insert(self, e):
        index = len(self.heap)
        parentIndex = (index-1)//2
        while index>0 and self.heap[parentIndex] < e:
            if index == len(self.heap):
                self.heap.append(self.heap[parentIndex])
            else:
                self.heap[index] = self.heap[parentIndex]
            index = parentIndex
            parentIndex = (index-1)//2
        if index == len(self.heap):
            self.heap.append(e)
        else:
            self.heap[index] = e
    
    def top(self):
        if len(self.heap) == 0:
            raise EmptyHeapException()
        return self.heap[0]
    
    def delete(self):
        if len(self.heap) == 0:
            raise EmptyHeapException()
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        temp = self.heap.pop()
        index = 0
        leftChildIndex = 2*index+1
        rightChildIndex= 2*index+2
        
        while leftChildIndex < len(self.heap):
            if rightChildIndex < len(self.heap):
                if self.heap[leftChildIndex] > self.heap[rightChildIndex]:
                    if self.heap[leftChildIndex] > temp:
                        self.heap[index] = self.heap[leftChildIndex]
                        index = leftChildIndex
                    else:
                        break
                else:
                    if self.heap[rightChildIndex] > temp:
                        self.heap[index] = self.heap[rightChildIndex]
                        index = rightChildIndex
                    else:
                        break
            else:
                if self.heap[leftChildIndex] > temp:
                    self.heap[index] = self.heap[leftChildIndex]
                    index = leftChildIndex
                else:
                    break
            leftChildIndex = 2*index+1
            rightChildIndex= 2*index+2
        self.heap[index] = temp
        return max_value
    
    def heap_sort(self):
        """
        Performs heap sort using the current heap.
        Returns a sorted list in ascending order.
        """
        if len(self.heap) == 0:
            raise EmptyHeapException()

        result = []

        # Repeatedly remove max element
        while len(self.heap) > 0:
            result.append(self.delete())

        # Since this is a max-heap, result is in descending order
        result.reverse()
        return result

if __name__ == "__main__":
    h = Heap()

    print("Creating heap from list:")
    elements = [20, 15, 30, 40, 10, 5]
    print("Input:", elements)

    h.createHeap(elements)
    print("Heap array:", h.heap)

    print("\nInserting elements:")
    h.insert(50)
    h.insert(25)
    print("Heap after insertions:", h.heap)

    print("\nTop element:", h.top())

    print("\nDeleting elements:")
    print("Deleted:", h.delete())
    print("Heap after deletion:", h.heap)

    print("\nHeap Sort Result:")
    h.createHeap([12, 7, 25, 15, 28, 3])
    sorted_list = h.heap_sort()
    print("Sorted list:", sorted_list)
