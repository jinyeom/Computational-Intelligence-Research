#ifndef MINION_HPP
#define MINION_HPP

class Minion: public Character
{

private:

    int         m_num;       /* minion number    */

    int         f_hp;        /* full health      */
    int         hp;          /* health point     */
    int         x;           /* x coordinate     */
    int         y;           /* y coordinate     */

    double      d_atk;       /* attack damage    */
    double      r_atk;       /* attack range     */
    double      s_atk;       /* attack speed     */

    double      dir;         /* moving direction */
    int         speed;       /* moving speed     */

public:

    Minion(int m_num, int x, int y);
    ~Minion();

    bool is_dead();
    void update();
};

#endif
