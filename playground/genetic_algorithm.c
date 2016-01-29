#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define L_DNA 8
#define P_MUTATION 20

char mutate(char ch)
{
    unsigned char i, m_ch;

    srand((unsigned)time(NULL));

    m_ch = 0x00;

    for(i = 0x01; i > 0x00; i <<= 1)
    {
        if(rand() % 100 < P_MUTATION)
        {
            m_ch += i;
        }
    }

    ch ^= m_ch;

    return ch;
}

int main() {
    unsigned char dna, m_dna;

    dna = 0x5B;
    m_dna = mutate(dna);

    printf("original: %x\n", dna);
    printf("mutated: %x\n", m_dna);
}
