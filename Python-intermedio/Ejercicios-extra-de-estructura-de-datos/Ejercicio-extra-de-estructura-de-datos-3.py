class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current = self.head

        while current:
            if current.value == data:

                if current == self.head and current == self.tail:
                    self.head = self.tail = None

                elif current == self.head:
                    self.head = current.next
                    self.head.prev = None
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                return

            current = current.next


    def print_forward(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


    def print_backward(self):
        current = self.tail
        while current:
            print(current.value, end=" -> ")
            current = current.prev
        print("None")
