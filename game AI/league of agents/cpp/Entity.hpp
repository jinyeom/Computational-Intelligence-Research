#ifndef ENTITY_HPP
#define ENTITY_HPP
#endif

class Entity
{

protected:

    // entity stats
    bool team;
    int f_hp;

    // entity status
    int hp;
    int x;
    int y;

public:

    Entity();
    ~Entity();

    bool get_team();
    int get_f_hp();
    int get_hp();
    int get_x();
    int get_y();

    void set_team(bool team);
    void set_f_hp(int f_hp);
    void set_hp(int hp);
    void set_x(int x);
    void set_y(int y);

}
