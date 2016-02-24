#ifndef MINION_HPP
#define MINION_HPP

class Minion: public Character
{

private:

    int m_num;

    int f_hp;
    int hp;
    int x;
    int y;

    double atk_damage;
    double atk_range;
    double atk_speed;

    double dir;
    int speed;

public:

    Minion(int m_num, int x, int y);
    ~Minion();

    bool is_dead();
    void update();
};

#endif
