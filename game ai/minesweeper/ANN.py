import numpy as np
from copy import deepcopy as copy

class ANN(object):
    def __init__(self, num_inputs, num_hidden_nodes, num_outputs, weights):
        num_hidden_weights = (num_inputs+1)*num_hidden_nodes
        self.num_inputs = num_inputs
        assert len(weights) == num_hidden_nodes*(num_inputs+1)+ (num_hidden_nodes+1)*num_outputs, 'invalid number of weights'
        self.hidden_weights = np.array(weights[:num_hidden_weights]).reshape(num_hidden_nodes,num_inputs+1)
        self.output_weights = np.array(weights[num_hidden_weights:]).reshape(num_outputs,num_hidden_nodes+1)

    def activation(self,x):
        return 1/(1+np.exp(-x))

    def evaluate(self,inputs):
        inputs = copy(inputs)
        assert len(inputs) == self.num_inputs, 'invalid number of inputs %s' %inputs
        inputs.append(1)
        inputs = np.array(inputs).T
        result = self.hidden_weights.dot(inputs)
        result = self.activation(result)
        result = np.hstack((result.T,np.array(1)))
        result = self.output_weights.dot(result)
        result = self.activation(result)
        return result.tolist()
        
