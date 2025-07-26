class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.head = 0  # Points to the oldest element
        self.tail = 0  # Points to the next insertion point
        self.count = 0  # Number of elements in the buffer

    def put(self, item):
        self.buffer[self.tail] = item
        if self.count == self.size:
            # Overwriting the oldest item; advance head
            self.head = (self.head + 1) % self.size
        else:
            self.count += 1
        self.tail = (self.tail + 1) % self.size

    def get(self):
        if self.count == 0:
            return None
        item = self.buffer[self.head]
        self.buffer[self.head] = None  # Optional: Clear the slot
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return item

# Examples
buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)    # True

buffer.put(5)
buffer.put(6)
buffer.put(7)

print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True