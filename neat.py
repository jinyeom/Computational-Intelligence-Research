import math
import random

# define a Neural network in NEAT
class NEAT:
    def __init__(self, nIns, nOuts):
        self.n_inputs = nIns                    # number of inputs
        self.n_outputs = nOuts                  # number of outputs
        self.c_node = 0                         # neuron counter
        self.c_conn = 0                         # connection counter
        self.nodes = initNodes(nIns, nOuts)     # init NEAT inputs and outputs
        self.conns = initConns(nIns, nOuts)     # init NEAT connections

    def initNodes(self, nIns, nOuts):
        nodes = []

        # append input nodes
        for i in range(nIns):
            nodes.append(Node(self.c_node))
            self.c_node += 1

        # append output nodes
        for i in range(nOuts):
            nodes.append(Node(self.c_node))
            self.c_node += 1

        return nodes

    def initConns(self):
        conn = []


# define a connection
class Connection:
    def __init__(self, h_mark, n_from, n_to):
        self.conntd = True                      # false if disabled
        self.h_mark = h_mark                    # historical marking
        self.n_from = n_from                    # connected from
        self.n_to = n_to                        # connected to
        self.weight = random.random()           # weight of the connection

# define a node
class Node:
    def __init__(self, n_num):
        self.n_num = n_num                      # node number
        self.s_inputs = 0.0                     # sum of all inputs
