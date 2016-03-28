#ifndef NODE_HPP
#define NODE_HPP

class Node
{

private:

    double input;       // sum of all the inputs
    int innov;          // global innovation number

public:

    Node();             // constructor
    double output();    // output a value according to sum of inputs
    double sigmoid();   // sigmoid function

};

#endif
