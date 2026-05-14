class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if self.top is None:
            raise Exception("Stack vacío")
        removed_value = self.top.value
        self.top = self.top.next
        return removed_value
    def print_stack(self):
        current = self.top
        while current:
            print(current.value)
            current = current.next
    def bubble_sort(self):
        if self.top is None:
            return

        swapped = True

        while swapped:
            swapped = False
            current = self.top
            while current.next:
                if current.value > current.next.value:
                    current.value, current.next.value = (
                        current.next.value,
                        current.value
                    )
                    swapped = True
                current = current.next
