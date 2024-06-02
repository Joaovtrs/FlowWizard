def liso(diameter, flow):
    return (8.69 * 10 ** 6) * (flow ** 1.75) * (diameter ** (-4.75)) / 9.80638


def rugoso(diameter, flow):
    return (20.2 * 10 ** 6) * (flow ** 1.88) * (diameter ** (-4.88)) / 9.80638


class Pipe:
    def __init__(self, name):
        self.name = name
        self.flow = 0.0
        self.nodes = [None, None]

    def __str__(self):
        return f'Pipe {self.name}: {self.flow} l/s'
