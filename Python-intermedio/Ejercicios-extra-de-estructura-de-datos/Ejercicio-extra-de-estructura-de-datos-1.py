class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None


    def enqueue(self, data):
        new_node = Node(data)

        if self.tail is None:  # cola vacía
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


    def dequeue(self):
        if self.head is None:
            raise Exception("Queue vacía")

        removed_value = self.head.value
        self.head = self.head.next

        if self.head is None:  # si quedó vacía
            self.tail = None

        return removed_value

    
    def print_all(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
