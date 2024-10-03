def liso(diameter, flow):
    return (8.69 * 10**6) * (flow**1.75) * (diameter ** (-4.75)) / 9.80638


def rugoso(diameter, flow):
    return (20.2 * 10**6) * (flow**1.88) * (diameter ** (-4.88)) / 9.80638


class Pipe:
    def __init__(self, name):
        self.name = name
        self.flow = 0.0
        self.nodes = [None, None]
        self.pressure_loss = 0.0

    def __str__(self):
        return f'Pipe {self.name}'

    def __repr__(self):
        return self.__str__()

    def statitics(self):
        return self.__str__() + f': {self.flow} l/s'

    def connect_node(self, node, side):
        if side in [1, 2]:
            self.nodes[side - 1] = node

    def disconnect_node(self, node):
        if node in self.nodes:
            pos = self.nodes.index(node)
            self.nodes[pos] = None

    def clear_conections(self):
        for node in self.nodes:
            if node is not None:
                node.disconnect_pipe(self)
        self.nodes = [None, None]
