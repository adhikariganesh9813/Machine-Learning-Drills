# create graph using hast table

graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# create another hash table to store cost of nodes (time taken to reach each node from start)

infinity = math.inf
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# another hash table for parents

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# track nodes ( because each node is only processed once)

processed = set()

