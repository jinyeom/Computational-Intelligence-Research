import random
import math

# evolutionary algorithm constants
P_WEIGHT = 7 # weight precision = 1 / 128

# neural network constants
BIAS = -1
RESPONSE = 1

class NNetwork:
    def __init__(self, nIns, nHLs, nHLNs, nOuts):
        self.l_data = self.getLayerData(nHLs, nHLNs, nOuts)
        self.n_weights = nHLNs * (nIns + nHLNs * nHLs + nOuts) + nOuts
        self.weights = [random.random() for _ in range(self.n_weights)]

    # create list of number of neurons in each layer
    def getLayerData(self, nHLs, nHLNs, nOuts):
        layerData = []
        for _ in range(nHLs):
            layerData.append(nHLNs)
        layerData.append(nOuts)
        return layerData

    # get weights
    def getWeights(self):
        return self.weights

    # set weights
    def setWeights(self, weights):
        self.weights = weights

    # get n_weights
    def getNumWeights(self):
        return self.n_weights

    # recursively update the neural network
    def update(self, inputs, counter=0, l_counter=0):
        if l_counter == len(self.l_data):
            return inputs
        else:
            outputs = []
            for _ in range(self.l_data[l_counter]):
                netInput = 0.0
                for val in inputs:
                    netInput += self.weights[counter] * val
                    counter += 1
                netInput += self.weights[counter] * BIAS
                counter += 1
                outputs.append(self.sigmoid(netInput, RESPONSE))
            return self.update(outputs, counter, l_counter + 1)

    # sigmoid function
    def sigmoid(self, netInput, response):
        return 1.0 / (1.0 + math.exp(-netInput / response))

# for testing
def test():
    nnet = NNetwork(2, 3, 3, 1)
    inputs = [5, 4]
    print "LAYER DATA: " + str(nnet.l_data)
    print "NUM WEIGHTS: " + str(nnet.n_weights)
    print "WEIGHTS: ",
    print nnet.weights
    print "OUTPUT: " + str(nnet.update(inputs))
