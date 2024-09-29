class Node:
    def __init__(self, name):
        self.name = name
        self.elevation = 0.0
        self.pressure = 0.0
        self.pipes = []

    def __str__(self):
        return f'Node {self.name}'

    def __repr__(self):
        return self.__str__()

    def statitics(self):
        return self.__str__() + f': {self.elevation} m, {self.pressure} m.c.a.'

    def connect_pipe(self, pipe):
        if not pipe.connect_node(self):
            return

        self.pipes.append(pipe)

    def disconnect_pipe(self, pipe):
        if pipe in self.pipes:
            self.pipes.remove(pipe)

    def clear_conections(self):
        for pipe in self.pipe:
            pipe.disconnect_node(self)
        self.pipes = []
