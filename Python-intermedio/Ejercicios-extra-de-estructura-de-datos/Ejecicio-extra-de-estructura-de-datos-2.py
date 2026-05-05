class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_back(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.value == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.value == data:
                current.next = current.next.next
                return
            current = current.next

    def print_all(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
