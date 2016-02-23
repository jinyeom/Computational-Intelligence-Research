#include "Character.hpp"

Character::Character()  { }

Character::~Character() { }

bool Character::is_dead()
{
    return (this.hp == 0);
}

// getters

double Character::get_atk_damage()
{
    return this.atk_damage;
}

double Character::get_atk_range()
{
    return this.atk_range;
}

double Character::get_atk_speed()
{
    return this.atk_speed;
}

double Character::get_dir()
{
    return this.dir;
}

int Character::get_speed()
{
    return this.speed;
}

// setters

void Character::set_atk_damage(double atk_damage)
{
    this.atk_damage = atk_damage;
}

void Character::set_atk_range(double atk_range)
{
    this.atk_range = atk_range;
}

void Character::set_atk_speed(double atk_speed)
{
    this.atk_speed = atk_speed;
}

void Character::set_dir(double dir)
{
    this.dir = dir;
}

void Character::set_speed(int speed)
{
    this.speed = speed;
}
