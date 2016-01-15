import math
import random

# define a Neural network in NEAT
class NEAT:
    def __init__(self, nIns, nOuts):
        self.n_inputs = nIns                        # number of inputs
        self.n_outputs = nOuts                      # number of outputs
        self.h_mark = 0                             # historical marking
        self.nodes = self.initNodes(nIns, nOuts)    # init nodes
        self.conns = self.initConns(nIns, nOuts)    # init connections

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




    def update(self, inputs):



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
        self.conntd = True              # false if disabled
        self.h_mark = h_mark            # historical marking
        self.n_from = n_from            # connected from (index)
        self.n_to = n_to                # connected to (index)
        self.weight = random.random()   # weight of the connection

if __name__ == "__main__":
    neat = NEAT(4, 2)
    print neat
