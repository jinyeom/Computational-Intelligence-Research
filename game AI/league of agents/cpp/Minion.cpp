#include "Minion.hpp"
#include "iostream"

Minion::Minion(int m_num, int x, int y)
{
    this.m_num = m_num;

    this.f_hp = 455;
    this.hp = f_hp;
    this.x = x;
    this.y = y;

    this.d_atk = 12;
    this.r_atk = 100;
    this.s_atk = 1.25;

    this.dir = 0.0;
    this.speed = 325;
}

bool Minion::is_dead()
{
    return (this.hp == 0);
}

void Minion::update()
{

}
