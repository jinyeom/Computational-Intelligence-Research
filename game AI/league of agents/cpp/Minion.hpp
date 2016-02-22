#ifndef MINION_HPP
#define MINION_HPP
#endif

class Minion: public Entity
{

protected:

    // minion stats
    int m_num;                      /* minion number for counting   */
    double atk_damage;              /* attack damage to enemy       */
    double atk_range;               /* attack range                 */
    double atk_speed;               /* attack speed                 */

    // minion status
    int dx;                         /* x speed                      */
    int dy;                         /* y speed                      */
    int t_x;                        /* target x coordinate          */
    int t_y;                        /* target y coordinate          */

public:

    // constructor
    Minion();                       /* created with a given type    */

    // destructor
    ~Minion();                      /* destruct minion when it dies */

    // in-game functions
    bool is_dead();                 /* true if hp = 0               */
    void move(int x, int y);        /* move to (x, y)               */
    void target();                  /* target the closest enemy     */
    void attack();                  /* attack if close to target    */

    // getters
    int get_m_num();                /* return minion number         */
    double get_atk_damage();        /* return attack damage         */
    double get_atk_range();         /* return attack range          */
    double get_atk_speed();         /* return attack speed          */
    int get_dx();                   /* return x speed               */
    int get_dy();                   /* return y speed               */
    int get_t_x();                  /* return target x coordinate   */
    int get_t_y();                  /* return target y coordinate   */

    // setters
    void set_dx(int dx);            /* set x speed to dx            */
    void set_dy(int dy);            /* set y speed to dy            */
    void set_t_x(int t_x);          /* set target x coord to t_x    */
    void set_t_y(int t_y);          /* set target y coord to t_y    */
};

// derived class of Melee minion
class Melee: public Minion
{

public:

    // constructor
    Melee(int m_counter);

};

// derived class of Caster minion
class Caster: public Minion
{

public:

    // constructor
    Caster(int m_counter);

};

// derived class of Siege minion
class Siege: public Minion
{

public:

    // constructor
    Siege(int m_counter);

};

// derived class of Super minion
class Super: public Minion
{

public:

    // constructor
    Super(int m_counter);

};
