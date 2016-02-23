#ifndef MINION_HPP
#define MINION_HPP

class Minion: public Character
{

private:

    int m_num;

public:

    Minion(int m_num, int x, int y);
    ~Minion();
};

#endif
