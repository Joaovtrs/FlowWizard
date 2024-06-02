from system import System

system = System()

system.add_node()
system.add_node()
system.add_node()
system.add_node()

system.add_pipe()
system.add_pipe()
system.add_pipe()

print(system)

print(system.get_node(1).equivalent_length)
