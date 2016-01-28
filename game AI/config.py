# config.py

# configuration for game
game = dict(
    width               = 400, # game width
    height              = 400, # game height
    g_name              = "GAME", # game name
    g_time              = 10000, # game time
    fps                 = 60, # frame per second
    delay               = 20, # terminal update delay
    n_best              = 5, # number of best agents
    n_agents            = 20, # number of agents
    n_targets           = 10, # number of targets
    s_agent             = 28, # size of an agent
    s_target            = 2, # size of a target
    l_track             = 2., # default speed of left track
    r_track             = 2., # default speed of right track
    r_min               = -0.3, # minimum rotation rate
    r_max               = 0.3, # maximum rotation rate
)

# configuration for image sources
image = dict(
    icon        = "asset/icon.png", # path of icon image file
    best        = "asset/best.png", # path of best image file
    agent       = "asset/agent.png", # path of agent image file
    target      = "asset/target.png", # path of target image file
)

# configuration for neural network
nnet = dict(
    p_weight            = 10, # precision of weights
    n_inputs            = 4, # number of inputs
    n_outputs           = 2, # number of outputs
    n_hidden_layers     = 4, # number of hidden layers
    n_hl_neurons        = 5, # number of neurons in hidden layers
    bias                = -1, # bias
    response            = 1, # response
)

# configuration for genetic algorithm
ga = dict(
    n_gen               = 30, # number of generations
    p_mut               = 0.1, # probability of mutation
    p_xover             = 0.1, # probability of crossover
    p_select            = 0.5, # probability of selection
)

# configurations that are variables

n_weights       = nnet['n_hl_neurons'] * (nnet['n_inputs'] +
                    nnet['n_hl_neurons'] * nnet['n_hidden_layers'] +
                    nnet['n_outputs']) + nnet['n_outputs']

l_dna           = n_weights * nnet['p_weight']
