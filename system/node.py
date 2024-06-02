class Node:
    def __init__(self, name):
        self.name = name
        self.elevation = 0.0
        self.pressure = 0.0

    def __str__(self):
        return f'Node {self.name}: {self.elevation} m, {self.pressure} m.c.a.'
