class SharedMemory:
    def __init__(self):
        self.data = []

    def store(self, item):
        self.data.append(item)

    def recent(self, k=10):
        return self.data[-k:]

    def resource_trend(self, k=5):
        if len(self.data) < 2:
            return 0.0
        recent = self.data[-k:]
        if len(recent) < 2:
            return 0.0
        resources = [t["world"]["resource"] for t in recent]
        return resources[-1] - resources[0]
