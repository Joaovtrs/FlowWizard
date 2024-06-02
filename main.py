from system import System

system = System()

system.add_node()
system.add_node()
system.add_node()
system.add_node()

system.add_pipe()
system.add_pipe()
system.add_pipe()

print(system.connections())

system.get_node(1).connect_pipe(system.get_pipe(1), 0)

print(system.connections())

system.get_node(1).connect_pipe(system.get_pipe(2), 0)

print(system.connections())
