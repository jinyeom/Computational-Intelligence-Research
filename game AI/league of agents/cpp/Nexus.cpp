#include "Nexus.hpp"

#define F_HP

Nexus::Nexus(int x, int y)
{
    this.x = x;
    this.y = y;
    this.hp = F_HP;
}

Nexus::is_collapsed()
{
    return (this.hp == 0);
}
