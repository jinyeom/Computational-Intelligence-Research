import random
import math
import config

# evolutionary algorithm constants
P_WEIGHT = 7 # weight precision = 1 / 128

class NNet:
    def __init__(self):
        self.l_data = self.get_layer_data()
        self.n_weights = self.get_n_weights()
        self.weights = [random.random() for _ in range(self.n_weights)]

    # calculate the number of weights
    def get_n_weights(self):
        return config.nnet['n_hl_neurons'] * (config.nnet['n_inputs'] +
                config.nnet['n_hl_neurons'] * config.nnet['n_hidden_layers'] +
                config.nnet['n_outputs']) + config.nnet['n_outputs']

    # create list of number of neurons in each layer
    def get_layer_data(self):
        l_data = []
        for _ in range(config.nnet['n_hidden_layers']):
            l_data.append(config.nnet['n_hl_neurons'])
        l_data.append(config.nnet['n_outputs'])
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
                net_input += self.weights[counter] * config.nnet['bias']
                counter += 1
                outputs.append(self.sigmoid(net_input))
            return self.update(outputs, counter, l_counter + 1)

    # sigmoid function
    def sigmoid(self, net_input):
        return 1.0 / (1.0 + math.exp(-net_input / config.nnet['response']))
