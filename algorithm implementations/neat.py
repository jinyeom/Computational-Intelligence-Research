import math
import random

# define a Neural network in NEAT
class NEAT:
    def __init__(self, n_ins, n_outs):
        self.n_inputs = n_ins                           # number of inputs
        self.n_outputs = n_outs                         # number of outputs
        self.h_mark = 0                                 # historical marking
        self.nodes = self.init_nodes(n_ins, n_outs)     # init nodes
        self.conns = self.init_conns(n_ins, n_outs)     # init connections

    # initialize nodes
    def initNodes(self, nIns, nOuts):
        nodes = []

        # append input nodes
        for i in range(nIns):
            nodes.append(0.0)

        # append output nodes
        for i in range(nOuts):
            nodes.append(0.0)

        return nodes

    # initialize connections
    def initConns(self, nIns, nOuts):
        conns = []

        # append all connections among input and output nodes
        for i in range(nIns):
            for o in range(nIns, nIns + nOuts):
                conns.append(Connection(self.h_mark, i, o))
                self.h_mark += 1

        return conns

    # structural mutation that adds a node
    def n_mutation(self):



    # structural mutation that adds a connection
    def c_mutation(self):



    # return outputs
    def update(self, inputs):
        for i, c in enumerate(self.conns):
            if c.conntd == True:
                nodes[c.n_to] += c.weight * nodes[c.n_from]

        # return a slice of nodes that contain outputs
        return nodes[self.n_inputs, self.n_inputs + self.n_outputs]


    # print NEAT instruction
    def __repr__(self):
        nodes = "NODES\n"
        for i, val in enumerate(self.nodes):
            nodes += (str(i) + " ")

        conns = "CONNECTIONS\n"
        for i, conn in enumerate(self.conns):
            conns += ("conn." + str(conn.h_mark)) + ": " +\
                str(conn.n_from) + " " + str(conn.n_to) + "\n"

        return nodes + "\n\n" + conns

    __str__ = __repr__

# define a connection
class Connection:
    def __init__(self, h_mark, n_from, n_to):
        self.conntd = True              # connected (false if disabled)
        self.h_mark = h_mark            # historical marking
        self.n_from = n_from            # connected from (index)
        self.n_to = n_to                # connected to (index)
        self.weight = random.random()   # weight of the connection

if __name__ == "__main__":
    neat = NEAT(4, 2)
    print neat
