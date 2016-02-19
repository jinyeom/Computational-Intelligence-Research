class Minion
{

private:

    // character stats
    int f_hp;                       /* full HP                      */
    int atk;                        /* attack damage to enemy       */

    // character status
    int hp;                         /* health point                 */
    int x;                          /* x coordinate                 */
    int y;                          /* y coordinate                 */
    int dx;                         /* x speed                      */
    int dy;                         /* y speed                      */
    int t_x;                        /* target x coordinate          */
    int t_y;                        /* target y coordinate          */

public:

    // constructor
    Minion(char m_type);            /* created with a given type    */

    // destructor
    ~Minion();                      /* destruct minion when it dies */

    // getters
    int get_f_hp();                 /* return full HP               */
    int get_atk();                  /* return attack damage         */
    int get_hp();                   /* return current HP            */
    int get_x();                    /* return x coordinate          */
    int get_y();                    /* return y coordinate          */
    int get_dx();                   /* return x speed               */
    int get_dy();                   /* return y speed               */
    int get_t_x();                  /* return target x coordinate   */
    int get_t_y();                  /* return target y coordinate   */

    // setters
    void set_hp(int hp);            /* set HP to hp                 */
    void set_x(int x);              /* set x coordinate to x        */
    void set_y(int y);              /* set y coordinate to y        */
    void set_dx(int dx);            /* set x speed to dx            */
    void set_dy(int dy);            /* set y speed to dy            */
    void set_t_x(int t_x);          /* set target x coord to t_x    */
    void set_t_y(int t_y);          /* set target y coord to t_y    */

    // in-game functions
    bool is_dead();                 /* true if hp = 0               */
    void move(int x, int y);        /* move to (x, y)               */
    void target();                  /* target the closest enemy     */
    void attack();                  /* attack if close to target    */

}
