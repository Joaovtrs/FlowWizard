class Node:
    def __init__(self, name, n_connections=3):
        self.name = name
        self.elevation = 0.0
        self.pressure = 0.0
        self.n_connections = n_connections
        self.pipes = [None for _ in range(n_connections)]
        self.equivalent_length = [
            [0 for _ in range(n_connections)]
            for _ in range(n_connections)
        ]

    def __str__(self):
        return f'Node {self.name}'

    def __repr__(self):
        return self.__str__()

    def statitics(self):
        return self.__str__() + f': {self.elevation} m, {self.pressure} m.c.a.'

    def connect_pipe(self, pipe, side):
        if side >= self.n_connections:
            return

        if not pipe.connect_node(self):
            return

        if self.pipes[side] is not None:
            self.disconnect_pipe(side)

        self.pipes[side] = pipe

    def disconnect_pipe(self, side):
        if self.pipes[side] is not None:
            self.pipes[side].disconnect_node(self)
