import random
import math
import config as c

# evolutionary algorithm constants
P_WEIGHT = 7 # weight precision = 1 / 128

class NNetwork:
    def __init__(self):
        self.l_data = self.get_layer_data()
        self.weights = [random.random() for _ in range(self.get_n_weights())]

    # calculate the number of weights
    def get_n_weights(self):
        return c.nnet['n_hl_neurons'] * (c.nnet['n_inputs'] +
                c.nnet['n_hl_neurons'] * c.nnet['n_hidden_layers'] +
                c.nnet['n_outputs']) + c.nnet['n_outputs']

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
