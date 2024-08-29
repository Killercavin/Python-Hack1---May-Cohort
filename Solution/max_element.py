class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_maximum(self):
        if self.head is None:
            raise ValueError("The linked list is empty")

        max_value = self.head.data
        current = self.head.next

        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next

        return max_value

# Test
ll = LinkedList()
elements = [1, 0, 0]

for element in elements:
    ll.append(element)

max_value = ll.find_maximum()
print(f"The maximum element in the linked list is: {max_value}")