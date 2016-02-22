#include "Minion.hpp"
#include "iostream"
#include "string"

// Melee constructor
Melee::Melee(int m_counter)
{
    m_num = m_counter;
    f_hp =
    atk_damage =
    atk_range =
    atk_speed =

    // character status
    hp = f_hp;
    int x;                          /* x coordinate                 */
    int y;                          /* y coordinate                 */
    int dx;                         /* x speed                      */
    int dy;                         /* y speed                      */
    int t_x;                        /* target x coordinate          */
    int t_y;                        /* target y coordinate          */
}

// Caster constructor
Caster::Caster(int m_counter)
{

}

// Siege constructor
Siege::Siege(int m_counter)
{

}

// Super constructor
Super::Super(int m_counter)
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
int get_atk()               {   return this.atk;    }
int get_dx()                {   return this.dx;     }
int get_dy()                {   return this.dy;     }
int get_t_x()               {   return this.t_x;    }
int get_t_y()               {   return this.t_y;    }

// setters
void set_atk(int atk)       {   this.atk = atk;     }
void set_dx(int dx)         {   this.dx = dx;       }
void set_dy(int dy)         {   this.dy = dy;       }
void set_t_x(int t_x)       {   this.t_x = t_x;     }
void set_t_y(int t_y)       {   this.t_y = t_y;     }
