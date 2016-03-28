#ifndef NEAT_HPP
#define NEAT_HPP

class NEAT
{

private:

    int             gin_node;   // global innovation number for nodes
    int             gin_conn;   // global innovation number for connections
    vector<Species> species;    // vector of species of networks

public:

    NEAT();                         // constructor
    void xover();                   // crossover
    void mut_add_conn();            // mutation to add a connection
    void mut_add_node();            // mutation to add a node
    void speciation(Network* n);    // speciate a network

};

#endif
