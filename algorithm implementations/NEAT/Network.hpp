#ifndef NETWORK_HPP
#define NETWORK_HPP

class Network
{

private:

    vector<Node>        nodes;      // vector of nodes in the network
    vector<Connection>  conns;      // vector of connections in the network

public:

    Network();                      // constructor
    double update();                // update the network and return output

};

#endif
