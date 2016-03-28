#ifndef CONNECTION_HPP
#define CONNECTION_HPP

class Connection
{

private:

    bool    enabled;        // true if the connection is enabled
    double  weight;         // weight of the connection
    Node*   in_node;        // input node
    Node*   out_node;       // output node
    int     innov;          // global innovation number

public:

    Connection();           // constructor
    double update();        // transfer input to output node with weight

};

#endif
