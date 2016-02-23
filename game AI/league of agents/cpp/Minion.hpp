#ifndef MINION_HPP
#define MINION_HPP

class Minion: public Character
{

private:

    int m_num;                      /* minion number for counting   */

public:

    Minion();

    ~Minion();

    int get_m_num();                /* return minion number         */
    void set_m_num(int m_counter);  /* set this.m_num to m_counter  */
};

class Melee: public Minion
{

public:

    Melee(int m_counter, int x, int y);

};

class Caster: public Minion
{

public:

    Caster(int m_counter, int x, int y);

};

class Siege: public Minion
{

public:

    Siege(int m_counter, int x, int y);

};

class Super: public Minion
{

public:

    Super(int m_counter, int x, int y);

};

#endif
