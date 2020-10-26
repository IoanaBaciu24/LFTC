class PIF:
    def __init__(self):
        self.data = []

    def add(self, name: str, index: int):
        self.data.append([name, index])

    def __str__(self):
        return str(self.data)