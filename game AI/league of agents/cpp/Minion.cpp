#include "Minion.hpp"
#include "iostream"
#include "string"

// Minion constructor
Minion::Minion(int m_counter, int x, int y) { }

// Melee constructor
Melee::Melee(int m_counter, int x, int y)
{
    this.m_num = m_counter;
    this.f_hp = 455;
    this.atk_damage = 12
    this.atk_range = 100
    this.atk_speed = 1.25

    this.hp = f_hp;
    this.x = x;
    this.y = y;
    this.dir = 0.0;
    this.speed = 325;
}

// Caster constructor
Caster::Caster(int m_counter, int x, int y)
{
    this.m_num = m_counter;
    this.f_hp = 455;
    this.atk_damage = 12
    this.atk_range = 100
    this.atk_speed = 1.25

    this.hp = f_hp;
    this.x = x;
    this.y = y;
    this.dir = 0.0;
    this.speed = 325;
}

// Siege constructor
Siege::Siege(int m_counter, int x, int y)
{
    this.m_num = m_counter;
    this.f_hp = 455;
    this.atk_damage = 12
    this.atk_range = 100
    this.atk_speed = 1.25

    this.hp = f_hp;
    this.x = x;
    this.y = y;
    this.dir = 0.0;
    this.speed = 325;
}

// Super constructor
Super::Super(int m_counter, int x, int y)
{
    this.m_num = m_counter;
    this.f_hp = 455;
    this.atk_damage = 12
    this.atk_range = 100
    this.atk_speed = 1.25

    this.hp = f_hp;
    this.x = x;
    this.y = y;
    this.dir = 0.0;
    this.speed = 325;
}

// destructor
Minion::~Minion()
{
    std::cout
    << "Minion number "
    << this.m_num
    << " destroyed."
    << std::endl;
}
