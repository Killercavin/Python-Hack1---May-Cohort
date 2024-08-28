class QueueWithStacks:
    def __init__(self):
        self.stack1 = []  # Stack for enqueue operations
        self.stack2 = []  # Stack for dequeue operations

    def enqueue(self, item):
        # Append item(s) onto stack1
        return self.stack1.append(item)

    def dequeue(self):
        # Check if both stacks are empty
        if not self.stack1 and not self.stack2:
            raise IndexError("Invalid, Stack is empty")

        # Append items from stack1 to stack2 when stack2 is empty
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # Pop and return the top item from stack2
        return self.stack2.pop()

    # Check if the queue is empty and if both stacks are empty
    def is_empty(self):
        return not self.stack1 and not self.stack2

    def peek(self):
        # If both stacks are empty, logically the queue will be empty
        if not self.stack1 and not self.stack2:
            raise IndexError("Invalid, peek from an empty queue")

        # Empty stack2, results to appending elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # Return the top item from stack2 without popping it
        return self.stack2[-1]

# Testing
# QueueWithStacks class
q = QueueWithStacks()

# Enqueueing elements
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Dequeueing and printing elements
print(q.dequeue())
print(q.dequeue())

# Dequeue the last element
print(q.dequeue())

# Peeking at the next element
#print(q.peek())

# Check if the queue is empty
print(q.is_empty())

# I fall into some errors earlier and consulted AI on how to solve the challenge in this question