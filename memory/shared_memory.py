class SharedMemory:
    def __init__(self):
        self.data = []

    def store(self, item):
        self.data.append(item)

    def recent(self, k=10):
        return self.data[-k:]
