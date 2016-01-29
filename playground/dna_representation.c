#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define L_DNA 8

/*
    Since a char in C is represented with 8 bits, it can be used a
    piece of DNA with an precision of (1 / 2^8).
*/
char mutate(char ch)
{
    int i;
    char c, m_ch;

    srand((unsigned)time(NULL));

    m_ch = 0x00;

    c = 0x01;

    for(i = 0; i < L_DNA; i++)
    {
        if(rand() % 10 < 5)
        {
            m_ch += c;
        }

        c <<= 1;

        printf("c = %x\n", c);
    }

    printf("m_ch = %x\n", m_ch);

    ch ^= m_ch;

    return ch;
}

int main() {
    char dna;

    dna = 0x5B;

    printf("original: %x\n", dna);
    printf("mutated: %x\n", mutate(dna));
    printf("original: %x\n", dna);
}
