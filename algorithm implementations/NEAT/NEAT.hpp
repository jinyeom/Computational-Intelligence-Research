#include <vector>

class NEAT
{

private:

    int                     hist_mark;
    vector<Node>            nodes;
    vector<Connection>      conns;
    vector<Species>         species;

public:

    NEAT();
    ~NEAT();

    void mut_add_conn();
    void mut_add_node();

}
