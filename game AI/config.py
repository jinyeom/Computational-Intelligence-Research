# config.py

# configuration for game
game = dict(
    width               = 400,          # game width
    height              = 400,          # game height
    n_agents            = 40,           # number of agents
    n_diamonds          = 20,           # number of diamonds
)

# configuration for neural network
nnet = dict(
    n_inputs            = 4,            # number of inputs
    n_outputs           = 2,            # number of outputs
    n_hidden_layers     = 3,            # number of hidden layers
    n_hl_neurons        = 4,            # number of neurons in a hidden layer
)

# configuration for genetic algorithm
ga = dict(
    s_dna               = 10,           # DNA size
    s_pop               = 20,           # population size
    n_gen               = 20,           # number of generations
    p_mut               = 0.1,          # probability of mutation
    p_xover             = 0.1,          # probability of crossover
    t_game              = 10000,        # game execution time
)
