import math
import random

# evolutionary algorithm constants
P_WEIGHT = 7 # weight precision = 1 / 128

# neural network constants
BIAS = -1
RESPONSE = 1

class NNetwork:
    def __init__(self, nIns, nHLs, nHLNs, nOuts):
        self.l_data = self.getLayerData(nHLs, nHLNs, nOuts)
        self.n_weights = nHLNs * (nIns + nHLNs * nHLs + nOuts) + nOuts
        self.dna = self.gen_DNA()
        self.weights = self.init_weights()

    # generate DNA for the neural network
    def gen_DNA(self):
        l_dna = self.n_weights * P_WEIGHT
        return [(random.random() > 0.5) for _ in range(l_dna)]

    # initialize weights based on DNA
    def init_weights(self):
        weights = []
        for i in range(self.n_weights):
            dnaSlice = self.dna[i * P_WEIGHT:(i + 1) * P_WEIGHT]
            b_sum = 0.0

            for j, bit in enumerate(dnaSlice):
                if bit == True:
                    b_sum += math.pow(2.0, P_WEIGHT - j)
            weight = b_sum / (math.pow(2.0, P_WEIGHT + 1) - 1)
            weights.append(weight)

        return weights

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

if __name__ == '__main__':
    nnet = NNetwork(2, 3, 3, 1)
    print nnet.dna
    print nnet.weights
