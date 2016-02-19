#include "Minion.hpp"
#include "iostream"

// constructor
Minion::Minion(char m_type)
{
    
}

// destructor
Minion::~Minion()
{
    std::cout
    << "Minion number "
    << this.m_num
    << " destroyed."
    << std::endl;
}

// check if this minion is dead
bool Minion::is_dead()
{
    return (this.hp == 0);
}

// move the minion to (x, y)
void Minion::move(int x, int y)
{
    // move until it reaches the destination
    while(this.x != x && this.y != y)
    {

    }
}

// getters
int get_f_hp()              {   return this.f_hp;   }
int get_atk()               {   return this.atk;    }
int get_hp()                {   return this.hp;     }
int get_x()                 {   return this.x;      }
int get_y()                 {   return this.y;      }
int get_dx()                {   return this.dx;     }
int get_dy()                {   return this.dy;     }
int get_t_x()               {   return this.t_x;    }
int get_t_y()               {   return this.t_y;    }

// setters
void set_f_hp(int f_hp)     {   this.f_hp = f_hp;   }
void set_atk(int atk)       {   this.atk = atk;     }
void set_hp(int hp)         {   this.hp = hp;       }
void set_x(int x)           {   this.x = x;         }
void set_y(int y)           {   this.y = y;         }
void set_dx(int dx)         {   this.dx = dx;       }
void set_dy(int dy)         {   this.dy = dy;       }
void set_t_x(int t_x)       {   this.t_x = t_x;     }
void set_t_y(int t_y)       {   this.t_y = t_y;     }
