#include "Minion.hpp"
#include "iostream"

Minion::Minion(int m_num, int x, int y)
{
    this.m_num = m_num;

    this.f_hp = 455;
    this.hp = f_hp;
    this.x = x;
    this.y = y;

    this.atk_damage = 12
    this.atk_range = 100
    this.atk_speed = 1.25

    this.dir = 0.0;
    this.speed = 325;
}

Minion::~Minion()
{
    std::cout
    << "Minion number "
    << this.m_num
    << " destroyed."
    << std::endl;
}

bool Minion::is_dead()
{
    return (this.hp == 0);
}

void Minion::update()
{

}
