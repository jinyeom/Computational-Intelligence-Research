#ifndef MINION_HPP
#define MINION_HPP

class Minion
{

private:

    int         f_hp;        /* full health      */
    int         hp;          /* health point     */
    int         x;           /* x coordinate     */
    int         y;           /* y coordinate     */
    int         exp;         /* exp when killed  */

    double      d_atk;       /* attack damage    */
    double      r_atk;       /* attack range     */
    double      s_atk;       /* attack speed     */

    double      dir;         /* moving direction */
    int         speed;       /* moving speed     */

public:

    Minion(int x, int y);
    ~Minion();

    bool is_dead();
    void update();
};

#endif
