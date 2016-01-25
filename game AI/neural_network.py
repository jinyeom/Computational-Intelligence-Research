# neural_network.py
import math
import random as r
import config as c

class NNetwork:
    def __init__(self, dna):
        self.dna            = dna
        self.n_weights      = c.n_weights
        self.l_data         = self.get_layer_data()
        self.weights        = self.init_weights(self.dna)

    # initialize weights based on a given DNA
    def init_weights(self, dna):
        weights = []

        for i in range(self.n_weights):
            b_sum = 0.0
            dna_slice = dna[i * c.nnet['p_weight']:
                        (i + 1) * c.nnet['p_weight']]

            for j, bit in enumerate(dna_slice):
                if bit == "1":
                    b_sum += math.pow(2.0, c.nnet['p_weight'] - j)

            weight = b_sum / (math.pow(2.0, c.nnet['p_weight'] + 1) - 1)
            weights.append(weight)

        return weights

    # create list of number of neurons in each layer
    def get_layer_data(self):
        l_data = []
        for _ in range(c.nnet['n_hidden_layers']):
            l_data.append(c.nnet['n_hl_neurons'])
        l_data.append(c.nnet['n_outputs'])
        return l_data

    # recursively update the neural network
    def update(self, inputs, counter=0, l_counter=0):
        if l_counter == len(self.l_data):
            return inputs
        else:
            outputs = []
            for _ in range(self.l_data[l_counter]):
                net_input = 0.0
                for val in inputs:
                    net_input += self.weights[counter] * val
                    counter += 1
                net_input += self.weights[counter] * c.nnet['bias']
                counter += 1
                outputs.append(self.sigmoid(net_input))
            return self.update(outputs, counter, l_counter + 1)

    # sigmoid function
    def sigmoid(self, net_input):
        return 1.0 / (1.0 + math.exp(-net_input / c.nnet['response']))
