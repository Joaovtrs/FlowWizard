from system import System

system = System()

system.add_node(1)
system.add_node(1)
system.add_node(2)

system.add_pipe()
system.add_pipe()

print(system)

system.get_node(1).connect_pipe(system.get_pipe(1), 0)
system.get_node(3).connect_pipe(system.get_pipe(1), 0)
system.get_node(3).connect_pipe(system.get_pipe(2), 1)
system.get_node(2).connect_pipe(system.get_pipe(2), 0)

print(system.connections())

system.verify_connections()
