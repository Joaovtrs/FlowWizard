def liso(diameter, flow):
    return (8.69 * 10**6) * (flow**1.75) * (diameter ** (-4.75)) / 9.80638


def rugoso(diameter, flow):
    return (20.2 * 10**6) * (flow**1.88) * (diameter ** (-4.88)) / 9.80638


class Pipe:
    def __init__(self, name):
        self.name = name
        self.flow = 0.0
        self.nodes = [None, None]

    def __str__(self):
        return f'Pipe {self.name}'

    def __repr__(self):
        return self.__str__()

    def statitics(self):
        return self.__str__() + f': {self.flow} l/s'

    def connect_node(self, node):
        if None in self.nodes:
            if self.nodes[0] is None:
                self.nodes[0] = node
            else:
                self.nodes[1] = node
            return True
        else:
            return False

    def disconnect_node(self, node):
        if self.nodes[0] == node:
            self.nodes[0] = None
        elif self.nodes[1] == node:
            self.nodes[1] = None
