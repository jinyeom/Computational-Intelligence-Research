#ifndef NEXUS_HPP
#define NEXUS_HPP

class Nexus
{

private:

    int x;      /* x coordinate         */
    int y;      /* y coordinate         */
    int hp;     /* Nexus health point   */

public:

    Nexus(int x, int y);

    bool is_collapsed();

};
