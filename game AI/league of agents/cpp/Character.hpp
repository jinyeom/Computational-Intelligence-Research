#ifndef CHARACTER_HPP
#define CHARACTER_HPP

class Character: public Entity
{

protected:

    // character stats
    double atk_damage;              /* attack damage to enemy       */
    double atk_range;               /* attack range                 */
    double atk_speed;               /* attack speed                 */

    // character status
    double dir;                     /* moving direction (angle)     */
    int speed;                      /* moving speed                 */

public:

    // in-game functions
    bool is_dead();                 /* true if hp = 0               */
    void move(int x, int y);        /* move to (x, y)               */
    void target();                  /* target the closest enemy     */
    void attack();                  /* attack if close to target    */

    // getters
    double get_dir();               /* return moving direction      */
    double get_speed();             /* return moving speed          */
    double get_atk_damage();        /* return attack damage         */
    double get_atk_range();         /* return attack range          */
    double get_atk_speed();         /* return attack speed          */

    // setters
    void set_m_num();               /* set character
};

#endif
