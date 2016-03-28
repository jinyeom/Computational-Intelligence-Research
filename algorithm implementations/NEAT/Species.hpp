#ifndef SPECIES_HPP
#define SPECIES_HPP

class Species
{

private:

    vector<Network> networks;       // networks in this species

public:

    Species();                      // constructor
    void add_network(Network* n);   // add a network

};

#endif
