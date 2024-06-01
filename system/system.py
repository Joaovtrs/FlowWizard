from .node import Node
from .pipe import Pipe


class System:
    def __init__(self):
        self.nodes = []
        self.pipes = []

        self.n_node = 0
        self.n_pipe = 0

    def add_node(self):
        self.n_node += 1
        self.nodes.append(Node(self.n_node))

    def add_pipe(self):
        self.n_pipe += 1
        self.pipes.append(Pipe(self.n_pipe))

    def __str__(self):
        response = 'System:\n'
        response += f'Node count: {len(self.nodes)}\n'

        for node in self.nodes:
            response += str(node) + '\n'

        response += '\n'

        response += f'Pipe count: {len(self.pipes)}\n'

        for pipe in self.pipes:
            response += str(pipe) + '\n'

        return response
