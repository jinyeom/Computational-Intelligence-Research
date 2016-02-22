#ifndef ENTITY_HPP
#define ENTITY_HPP
#endif

class Entity
{

protected:

    // entity stats
    int f_hp;                       /* full health point            */

    // entity status
    int hp;                         /* current health point         */
    int x;                          /* current x coordinate         */
    int y;                          /* current y coordinate         */

public:

    // getter
    int get_f_hp();                 /* return full health point     */
    int get_hp();                   /* return current health point  */
    int get_x();                    /* return current x coordinate  */
    int get_y();                    /* return current y coordinate  */

    // setter
    void set_f_hp(int f_hp);        /* set full health point        */
    void set_hp(int hp);            /* set current health point     */
    void set_x(int x);              /* set current x coordinate     */
    void set_y(int y);              /* set current y coordinate     */

}
