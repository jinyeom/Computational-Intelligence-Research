#ifndef CHAMPION_HPP
#define CHAMPION_HPP

class Champion
{

private:

    int         exp;
    int         f_hp;
    int         hp;
    int         x;
    int         y;

    double      d_atk;
    double      r_atk;
    double      s_atk;

public:

    Champion(int f_hp, double d_atk, double r_atk, double s_atk);

    void update();
};

#endif
