#ifndef NEAT_HPP
#define NEAT_HPP

class NEAT
{

private:

    int                     hist_mark;
    vector<Node>            nodes;
    vector<Connection>      conns;
    vector<Species>         species;

public:

    NEAT();

    void mut_add_conn();
    void mut_add_node();

    void xover();
    void speciation();

};

#endif
