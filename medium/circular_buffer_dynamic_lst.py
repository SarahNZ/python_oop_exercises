'''
See requirements: https://launchschool.com/exercises/699c68e4?track=python
'''

class CircularBuffer():

    def __init__(self, size):
        self._size = size
        self._buffer = []

    def get(self):
        if not self._buffer:    # instead of self._buffer == []
            return None
        else:
            return self._remove_oldest_object()
        
    def _remove_oldest_object(self):
        return self._buffer.pop(0)
    
    def _add_new_object(self, obj):
        self._buffer.append(obj)
        
    def put(self, obj):
        if len(self._buffer) < self._size:
            self._add_new_object(obj)
        else:
            self._remove_oldest_object()
            self._add_new_object(obj)

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