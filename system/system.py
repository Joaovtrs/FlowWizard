from .node import Node
from .pipe import Pipe


class System:
    def __init__(self):
        self.nodes = []
        self.pipes = []

        self.n_node = 0
        self.n_pipe = 0

    def __str__(self):
        response = f'System:\n\nNode count: {len(self.nodes)}\n'

        for node in self.nodes:
            response += node.statitics() + '\n'

        response += '\n'

        response += f'Pipe count: {len(self.pipes)}\n'

        for pipe in self.pipes:
            response += pipe.statitics() + '\n'

        return response

    def __repr__(self):
        return self.__str__()

    def connections(self):
        response = f'System:\n\nNode count: {len(self.nodes)}\n'

        for node in self.nodes:
            response += str(node) + ': ' + str(node.pipes) + '\n'

        response += '\n'

        response += f'Pipe count: {len(self.pipes)}\n'

        for pipe in self.pipes:
            response += str(pipe) + ': ' + str(pipe.nodes) + '\n'

        return response

    def add_node(self):
        self.n_node += 1
        self.nodes.append(Node(self.n_node))

    def add_pipe(self):
        self.n_pipe += 1
        self.pipes.append(Pipe(self.n_pipe))

    def get_node(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
        return None

    def get_pipe(self, name):
        for pipe in self.pipes:
            if pipe.name == name:
                return pipe
        return None
