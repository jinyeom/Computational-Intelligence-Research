import math
import random

# evolutionary algorithm constants
P_WEIGHT = 7 # weight precision = 1 / 128

# neural network constants
BIAS = -1
RESPONSE = 1

class NNetwork:
    def __init__(self, n_input, n_output, n_h_layer, n_hl_neuron):
        self.l_data = self.getLayerData(n_h_layer, n_hl_neuron, n_output)
        self.n_weights = n_hl_neuron * (n_input + n_hl_neuron *
                            n_h_layer + n_output) + n_output
        self.weights = self.init_weights()

    # initialize weights based on DNA
    def init_weights(self, dna):
        weights = []
        for i in range(self.n_weights):
            dnaSlice = dna[i * P_WEIGHT:(i + 1) * P_WEIGHT]
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
