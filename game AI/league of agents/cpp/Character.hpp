#ifndef CHARACTER_HPP
#define CHARACTER_HPP

class Character: public Entity
{

protected:

    // character stats
    double atk_damage;
    double atk_range;
    double atk_speed;

    // character status
    double dir;
    int speed;

public:

    bool is_dead();

    double get_dir();
    double get_speed();
    double get_atk_damage();
    double get_atk_range();
    double get_atk_speed();

    void set_atk_damage(double atk_damage);
    void set_atk_range(double atk_range);
    void set_atk_speed(double atk_speed);
    void set_dir(double dir);
    void set_speed(int speed);
};

#endif
