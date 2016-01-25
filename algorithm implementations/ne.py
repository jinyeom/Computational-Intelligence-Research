import math
import random

class NNetwork:
    def __init__(self, n_input, n_h_layer, n_hl_neuron, n_output):
        self.bias = -1
        self.response = 1
        self.p_weight = 7

        self.l_data = self.get_layer_data(n_h_layer, n_hl_neuron, n_output)
        self.n_weights = n_hl_neuron * (n_input + n_hl_neuron *
                            n_h_layer + n_output) + n_output
        self.weights = self.init_weights(self.gen_dna())

    def set_bias(b):
        self.bias = b

    def set_response(r):
        self.response = r

    def set_p_weight(p):
        self.p_weight = p

    def gen_dna(self):
        l_dna = self.n_weights * self.p_weight
        return [(r.random() > 0.5) for _ in range(l_dna)]

    def init_weights(self, dna):
        weights = []
        for i in range(self.n_weights):
            dna_slice = dna[i * self.p_weight:(i + 1) * self.p_weight]
            b_sum = 0.0

            for j, bit in enumerate(dna_slice):
                if bit == True:
                    b_sum += math.pow(2.0, p_weight - j)

            weight = b_sum / (math.pow(2.0, p_weight + 1) - 1)
            weights.append(weight)

        return weights

    # create list of number of neurons in each layer
    def get_layer_data(self, n_h_layer, n_hl_neuron, n_output):
        layerData = []
        for _ in range(n_h_layer):
            layerData.append(n_hl_neuron)
        layerData.append(n_output)

        return layerData

    # recursively update the neural network
    def update(self, inputs, counter=0, l_counter=0):
        if l_counter == len(self.l_data): return inputs
        else:
            outputs = []
            for _ in range(self.l_data[l_counter]):
                netInput = 0.0
                for val in inputs:
                    netInput += self.weights[counter] * val
                    counter += 1

                netInput += self.weights[counter] * bias
                counter += 1
                outputs.append(self.sigmoid(netInput, response))

            return self.update(outputs, counter, l_counter + 1)

    # sigmoid function
    def sigmoid(self, netInput, response):
        return 1.0 / (1.0 + math.exp(-netInput / response))
