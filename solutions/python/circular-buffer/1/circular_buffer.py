class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.isEmpty = True
        self.elements_count = 0
        self.list = []

    def read(self):
        if self.capacity == 0 or self.isEmpty:
            # raising a BufferEmptyException
            raise BufferEmptyException("Circular buffer is empty")
        else:
            a = self.list[0]
            self.list = self.list[1:]
            self.elements_count -= 1
            if self.elements_count == 0:
                self.isEmpty = True
            return a

    def write(self, data):
        if self.capacity == self.elements_count:
            # raising a BufferFullException
            raise BufferFullException("Circular buffer is full")
        else:
            self.isEmpty = False
            self.elements_count += 1
            self.list.append(data)

    def overwrite(self, data):
        if self.capacity > self.elements_count:
            self.write(data)
            return
            
        buffer_length = len(self.list)
        data_length = len(data)
        self.list[0:buffer_length - data_length] = self.list[data_length:buffer_length]
        self.list[buffer_length - data_length:buffer_length] = data
        
    def clear(self):
        self.elements_count = 0
        self.list = []
        self.isEmpty = True
