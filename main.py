from system import System
import networkx as nx
import matplotlib.pyplot as plt

system = System()

system.add_node(1)
system.add_node(2)
system.add_node(3)
system.add_node(4)

system.add_pipe()
system.add_pipe()
system.add_pipe()
system.add_pipe()

print(system)

system.get_node(1).connect_pipe(system.get_pipe(1), 0)
system.get_node(3).connect_pipe(system.get_pipe(1), 0)
system.get_node(3).connect_pipe(system.get_pipe(2), 1)
system.get_node(2).connect_pipe(system.get_pipe(2), 0)
system.get_node(3).connect_pipe(system.get_pipe(3), 2)
system.get_node(4).connect_pipe(system.get_pipe(3), 0)
system.get_node(2).connect_pipe(system.get_pipe(4), 1)
system.get_node(4).connect_pipe(system.get_pipe(4), 1)

print(system.connections())

system.verify_connections()

nx.draw_planar(system.graph(), with_labels=True)
plt.show()
